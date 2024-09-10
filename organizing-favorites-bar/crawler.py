import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread, Lock
from queue import Queue
from typing import List, Dict

# Tải các biến môi trường từ file .env
load_dotenv()
DATA_FILE = os.getenv('DATA_FILE')
DEBUG_MODE = os.getenv('DEBUG') == 'True'

def setup_logging():
    """Cài đặt logging"""
    logging.basicConfig(
        filename='crawler.log',
        level=logging.DEBUG if DEBUG_MODE else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

def log_function_call(func):
    """Decorator để ghi log các tham số của hàm"""
    def wrapper(*args, **kwargs):
        if DEBUG_MODE:
            logging.debug(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        if DEBUG_MODE:
            logging.debug(f'{func.__name__} returned {result}')
        return result
    return wrapper

@log_function_call
def load_links_from_file(file_path: str) -> List[Dict[str, str]]:
    """Đọc các link từ file JSON"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@log_function_call
def save_links_to_file(links: List[Dict[str, str]], file_path: str):
    """Lưu các link vào file JSON"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(links, file, ensure_ascii=False, indent=4)

def download_html(url: str) -> Dict[str, str]:
    """Tải file HTML từ URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {'url': url, 'html': response.text}
    except requests.RequestException as e:
        logging.error(f'Error downloading {url}: {e}')
        return {'url': url, 'html': ''}

def worker_download(queue: Queue, results: List[Dict[str, str]]):
    """Worker thread tải HTML"""
    while not queue.empty():
        url = queue.get()
        result = download_html(url)
        results.append(result)
        queue.task_done()

def worker_save(queue: Queue, file_path: str, lock: Lock):
    """Worker thread lưu dữ liệu"""
    while True:
        links = queue.get()
        if links is None:
            break
        with lock:
            existing_links = load_links_from_file(file_path)
            updated_links = existing_links + links
            save_links_to_file(updated_links, file_path)
        queue.task_done()

def main():
    setup_logging()
    links = load_links_from_file(DATA_FILE)
    urls = [link['url'] for link in links]

    download_queue = Queue()
    save_queue = Queue()
    results = []
    lock = Lock()

    for url in urls:
        download_queue.put(url)

    # Tạo và bắt đầu các thread tải HTML
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(worker_download, download_queue, results) for _ in range(5)]
        for future in as_completed(futures):
            future.result()

    # Bắt đầu thread lưu dữ liệu
    save_thread = Thread(target=worker_save, args=(save_queue, DATA_FILE, lock))
    save_thread.start()

    # Đẩy kết quả tải HTML vào queue lưu dữ liệu
    save_queue.put(results)

    # Đóng queue lưu dữ liệu
    save_queue.put(None)
    save_thread.join()

    logging.info("Crawling and saving completed.")

if __name__ == '__main__':
    main()
