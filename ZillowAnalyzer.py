from selenium import webdriver
from selenium.webdriver.common.by import By


class ZillowAnalyzer:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def get_properties(self, url):
        self.driver.get(url=url)
        prices_list = self.driver.find_elements(By.CSS_SELECTOR, 'article span[data-test="property-card-price"')
        prices_list = [item.text for item in prices_list]
        addresses_list = self.driver.find_elements(By.CSS_SELECTOR, 'article address')
        addresses_list = [item.text for item in addresses_list]
        links_list = self.driver.find_elements(By.CSS_SELECTOR, 'article a')
        links_list = [item.get_attribute('href') for item in links_list]

        # self.driver.close()

        properties_list = [{'price': prices_list[i],
                            'address': addresses_list[i],
                            'link': links_list[i]}
                           for i in range(len(prices_list))]

        return properties_list
