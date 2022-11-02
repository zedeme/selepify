from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

class Selepify():
    def login(self):
        driver = webdriver.Chrome()

        driver.get("https://" + self.credentials["GMAIL"] + ".myshopify.com/admin/")

        driver.find_element(By.XPATH, self.x_path["GMAIL"]).send_keys(self.credentials["GMAIL"])
        driver.find_element(By.XPATH, self.x_path["GMAIL_BUTTON"]).click()

        driver.find_element(By.XPATH, self.x_path["PASSWORD"]).send_keys(self.credentials["PASSWORD"])
        driver.find_element(By.XPATH, self.x_path["PASSWORD_BUTTON"]).click()

        driver.find_element(By.XPATH, self.x_path["ANALYTICS_BUTTON"]).click()

        s = driver.find_element(By.XPATH, self.x_path["SESSIONS"]).text()
        c_r = driver.find_element(By.XPATH, self.x_path["CONVERSION_RATE"]).text()
        c_r1 = driver.find_element(By.XPATH, self.x_path["CONVERSION_RATE_1"]).text()
        c_r2 = driver.find_element(By.XPATH, self.x_path["CONVERSION_RATE_2"]).text()
        c_r3 = driver.find_element(By.XPATH, self.x_path["CONVERSION_RATE_3"]).text()

        r_c = driver.find_element(By.XPATH, self.x_path["R_CLIENTS"]).text()

        driver.find_element(By.XPATH, self.x_path["TS_VIEW_REPORT_BUTTON"]).click()

        t_s = driver.find_element(By.XPATH, self.x_path["SALES"]).text()
        d = driver.find_element(By.XPATH, self.x_path["DISCOUNT"]).text()


        

    def __init__(self, x_path_config={}, credentials):
        if x_path_config == {}:
            self.x_path = {"GMAIL": "//*[@id='account_email']",
                           "GMAIL_BUTTON": "//*[@id='body-content']/div[2]/div/div[2]/div/div/div[2]/div/form/button",
                           "PASSWORD": "//*[@id='account_password']",
                           "PASSWORD_BUTTON": "//*[@id='login_form']/div[2]/ul/button",
                           "ANALYTICS_BUTTON": "//*[@id='AppFrameNav']/div/nav/div[2]/div[1]/ul/li[5]/div[1]/a/span",
                           "TS_VIEW_REPORT_BUTTON": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a",
                           "SALES": "//*[@id='AppFrameMain']/div/div/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/table/thead/tr[2]/td[2]/div/span",
                           "DISCOUNT": "//*[@id='AppFrameMain']/div/div/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/table/thead/tr[2]/td[3]/div/span",
                           "SESSIONS": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/p",
                           "CONVERSION_RATE": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/p",
                           "CONVERSION_RATE_1": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[3]/table/tbody[1]/tr[1]/td[2]",
                           "CONVERSION_RATE_2": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]",
                           "CONVERSION_RATE_3": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[3]/table/tbody[3]/tr[1]/td[2]",
                           "R_CLIENTS": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/p",
                           "ORDERS": "//*[@id='AppFrameMain']/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/p"}
        self.credentials = credentials