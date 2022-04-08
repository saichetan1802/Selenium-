from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    'https://beebom.com/category/news/'
)

titles = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div[3]/div/div[1]/div/article[1]/div/h3/a")
print(titles.get_attribute('title'))
driver.close()
