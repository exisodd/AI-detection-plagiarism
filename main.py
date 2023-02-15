import csv
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python main.py text_file url_file")

    content = read_content(sys.argv[1])
    urls = read_urls(sys.argv[2])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    selectors = {
        'CLASS_NAME': By.CLASS_NAME,
        'CSS_SELECTOR': By.CSS_SELECTOR,
        'ID': By.ID,
        'LINK_TEXT': By.LINK_TEXT,
        'NAME': By.NAME,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'TAG_NAME': By.TAG_NAME,
        'XPATH': By.XPATH,
    }

    for i, url in enumerate(urls):
        link = url['url']
        driver.switch_to.window(driver.window_handles[i])
        driver.get(link)
        sleep(2)

        # Send text
        text = driver.find_element(selectors[url['text_selector']], url['text'])
        text.send_keys(content)
        sleep(2)

        # Click button
        if url.get('scroll'):
            driver.execute_script("window.scrollTo(0, 400)")
            sleep(1)
        if link == 'https://gptzero.me/':
            driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
            sleep(1)
        if url.get('button'):
            button = driver.find_element(selectors[url['button_selector']], url['button'])
            button.click()
        sleep(1)
        driver.execute_script("window.open('');")

    input()


def read_content(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            try:
                content = content.encode("utf-8")
            except UnicodeDecodeError:
                content = content.encode("ISO-8859-1")
            content = content.decode("utf-8")
            return content

    except:
        print("An error occurred while reading the file.")


def read_urls(file_path):
    try:
        data = []
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except:
        print("An error occurred while reading the file.")


if __name__ == "__main__":
    main()
