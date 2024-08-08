import requests
from bs4 import BeautifulSoup
import threading
import queue
from concurrent.futures import ThreadPoolExecutor
import logging
import time
from dotenv import load_dotenv
import os
from functools import wraps

# Tải các biến môi trường từ file .env
load_dotenv()

# Lấy các biến môi trường
base_url = os.getenv('BASE_URL')
output_file = os.getenv('OUTPUT_FILE')
num_chapters = int(os.getenv('NUM_CHAPTERS'))
num_workers = int(os.getenv('NUM_WORKERS'))
debug_mode = os.getenv('DEBUG') == 'True'

# Cài đặt logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG if debug_mode else logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if debug_mode:
            logging.debug(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def fetch_webpage(url):
    """
    Gửi yêu cầu HTTP để lấy nội dung trang web.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logging.error(f'Error fetching {url}: {e}')
        return None

def parse_html(content):
    """
    Phân tích cú pháp HTML và trả về BeautifulSoup object.
    """
    return BeautifulSoup(content, 'html.parser')


def find_div_content(soup, itemprop_value):
    """
    Tìm thẻ div có thuộc tính itemprop cụ thể.
    """
    return soup.find('div', itemprop=itemprop_value)


def extract_paragraphs(div_content):
    """
    Lập qua các thẻ <p> bên trong thẻ div và trả về danh sách các dòng text.
    """
    paragraphs = []
    for p in div_content.find_all('p'):
        paragraphs.append(p.get_text())
    return paragraphs

@log_function_call
def write_to_file(base_filename, q, max_words=500000):
    """
    Ghi danh sách các dòng text vào file từ queue, tạo file mới khi số từ vượt quá max_words.
    """
    file_index = 1
    word_count = 0
    current_file = f"{base_filename}_{file_index}.txt"
    file = open(current_file, 'a', encoding='utf-8')

    while True:
        paragraphs = q.get()
        if paragraphs is None:
            q.task_done()
            break
        for line in paragraphs:
            words = line.split()
            word_count += len(words)
            if word_count > max_words:
                file.close()
                file_index += 1
                current_file = f"{base_filename}_{file_index}.txt"
                file = open(current_file, 'a', encoding='utf-8')
                word_count = len(words)
            file.write(line + '\n')
        q.task_done()
    file.close()
    logging.info(f'Nội dung đã được xuất ra file {current_file}')

@log_function_call
def process_chapter(url, q):
    """
    Lấy nội dung chương và thêm vào queue.
    """
    content = fetch_webpage(url)
    if content:
        soup = parse_html(content)
        div_content = find_div_content(soup, 'articleBody')
        if div_content:
            paragraphs = extract_paragraphs(div_content)
            q.put(paragraphs)
        else:
            logging.warning(f'Không tìm thấy thẻ div có itemprop="articleBody" ở {url}')
    else:
        logging.warning(f'Không thể lấy nội dung ở {url}')

@log_function_call
def main():
    q = queue.Queue()

    # Tạo và bắt đầu thread ghi file
    writer_thread = threading.Thread(target=write_to_file, args=(output_file, q))
    writer_thread.start()

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(1, num_chapters + 1):  # Lập qua số chương
            url = f'{base_url}{i}'
            executor.submit(process_chapter, url, q)

    # Đánh dấu kết thúc queue
    q.put(None)
    q.join()
    writer_thread.join()

    end_time = time.time()
    logging.info(f'Tổng thời gian chạy: {end_time - start_time} seconds')

if __name__ == '__main__':
    main()
