import os
import re
import logging
import time
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from functools import wraps
from typing import List, Dict

# Tải các biến môi trường từ file .env
load_dotenv()
HTML_FILE = os.getenv('HTML_FILE')
DEBUG_MODE = os.getenv('DEBUG') == 'True'
DATA_FILE = os.getenv('DATA_FILE')

def setup_logging():
    """Cài đặt logging"""
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG if DEBUG_MODE else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

def log_function_call(func):
    """Decorator để ghi log các tham số của hàm"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if DEBUG_MODE:
            logging.debug(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            if DEBUG_MODE:
                logging.debug(f'{func.__name__} returned {result}')
        except Exception as e:
            logging.error(f'Error in {func.__name__}: {e}')
            raise
        end_time = time.time()
        logging.info(f'{func.__name__} executed in {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@log_function_call
def read_html_file(html_file):
    """Đọc nội dung file HTML"""
    with open(html_file, 'r', encoding='utf-8') as file:
        return file.read()

@log_function_call
def parse_html(content):
    """Phân tích cú pháp HTML"""
    return BeautifulSoup(content, 'html.parser')

@log_function_call
def extract_a_tags(soup) -> List[Dict[str, str]]:
    """Lấy URL và title của tất cả các thẻ a"""
    links = []
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        title = a_tag.get_text(strip=True)
        if href and title:
            links.append({'url': href, 'title': title})
    return links

@log_function_call
def save_links_to_file(links: List[Dict[str, str]], file_path: str):
    """Lưu các link vào file JSON"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(links, file, ensure_ascii=False, indent=4)

@log_function_call
def load_links_from_file(file_path: str) -> List[Dict[str, str]]:
    """Đọc các link từ file JSON"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@log_function_call
def update_links(file_path: str, new_links: List[Dict[str, str]]):
    """Cập nhật các link trong file JSON"""
    existing_links = load_links_from_file(file_path)
    updated_links = existing_links + new_links
    save_links_to_file(updated_links, file_path)

def main():
    setup_logging()
    content = read_html_file(HTML_FILE)
    soup = parse_html(content)
    links = extract_a_tags(soup)
    update_links(DATA_FILE, links)
    print(f"Links have been saved to {DATA_FILE}")

if __name__ == '__main__':
    main()
