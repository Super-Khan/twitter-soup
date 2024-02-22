from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://x.com/iga_swiatek/status/1447348840164564994')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tweet_content = soup.find('p', class_='title').get_text() if soup.find('p', class_='title') else 'Content not found'

    print (tweet_content)