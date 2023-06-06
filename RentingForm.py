from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class RentingForm:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def fill_form(self, url, property_to_fill):
        self.driver.get(url=url)
        sleep(3)
        price_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i6 i7"]')
        price_input.send_keys(property_to_fill['price'])
        sleep(1)
        address_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i2 i3"]')
        address_input.send_keys(property_to_fill['address'])
        sleep(1)
        link_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i10 i11"]')
        link_input.send_keys(property_to_fill['link'])
        sleep(1)
        send_btn = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
        send_btn.click()

    # def create_sheet(self, url):
    #     self.driver.get(url=url)
    #     sheets_btn = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div')
    #     sheets_btn.click()
    #     sleep(3)
    #     self.driver.switch_to(self.driver.window_handles[1])
    #     create_btn = self.driver.find_element(By.XPATH, '/html/body/div[18]/div/div[2]/div[3]/div[2]/span/span')
    #     create_btn.click()
