import selenium.webdriver


from selenium.webdriver.chrome.options import Options
def get():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = selenium.webdriver.Chrome(options=chrome_options)


    driver.get("http://finra-markets.morningstar.com")
    cookies = driver.get_cookies()
    driver.close()
    return cookies