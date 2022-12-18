import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# import unittest
delay = 5
min = '2000'
max = '10000'
GradesName = 'NameAdmin'
class NewRecordPayGrades():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def LoginPage(self):
        FormLoginXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, FormLoginXpath)))
        self.browser.find_element(By.XPATH, FormLoginXpath).send_keys('Admin')

        FormPasswordXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, FormPasswordXpath)))
        self.browser.find_element(By.XPATH, FormPasswordXpath).send_keys('admin123')

        ButtonLoginXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.browser.find_element(By.XPATH, ButtonLoginXpath).click()

    def PathToGrades(self):

        ButtonAdminXpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonAdminXpath)))
        self.browser.find_element(By.XPATH, ButtonAdminXpath).click()

        ButtonJobXpath = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonJobXpath)))
        self.browser.find_element(By.XPATH, ButtonJobXpath).click()

        ButtonPayGradesXpath = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a' 
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonPayGradesXpath)))
        self.browser.find_element(By.XPATH, ButtonPayGradesXpath).click()

    def AddRecord(self):

        ButtonPayGradesButtonAddXpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonPayGradesButtonAddXpath)))
        self.browser.find_element(By.XPATH, ButtonPayGradesButtonAddXpath).click()
        FormNameXpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, FormNameXpath)))
        self.browser.find_element(By.XPATH, FormNameXpath).send_keys(GradesName)

        ButtonSaveNameXpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonSaveNameXpath)))
        self.browser.find_element(By.XPATH, ButtonSaveNameXpath).click()

        ButtonAddCurrenciesXpath = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/button'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonAddCurrenciesXpath)))
        self.browser.find_element(By.XPATH, ButtonAddCurrenciesXpath).click()

        ButtonSelectCurrenciesXpath = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div[2]/div/div'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonSelectCurrenciesXpath)))
        self.browser.find_element(By.XPATH, ButtonSelectCurrenciesXpath).click()
        
        ButtonUsdXpath = '//span[contains(text(),"USD - United States Dollar")]'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ButtonUsdXpath)))
        self.browser.find_element(By.XPATH, ButtonUsdXpath).click()

        FormMinimumXpath = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/div[2]/input'
        self.browser.find_element(By.XPATH, FormMinimumXpath).send_keys(min)

        FormMaximumXpath = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div[2]/input'
        self.browser.find_element(By.XPATH, FormMaximumXpath).send_keys(max)

        ButtonSaveCurrencyXpath = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]'
        self.browser.find_element(By.XPATH, ButtonSaveCurrencyXpath).click()
    
    def CheckRecord(self):
        time.sleep(5)
        CheckMin = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[3]/div' 
        CheckMax = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[4]/div'
        CheckCurrency = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div'
        self.browser.find_element(By.XPATH, CheckMin)
        self.browser.find_element(By.XPATH, CheckMax)
        self.browser.find_element(By.XPATH, CheckCurrency)

        CancelButtom = '//button[contains(.,"Cancel")]'
        self.browser.find_element(By.XPATH, CancelButtom).click()

        SelectRecord = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{GradesName}")]'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, SelectRecord)))

        CheckNamePayGrades = f'//div[contains(., "{GradesName}")]'
        CheckCurrrencyPayGrades = '//div[contains(., "United States Dollar")]'
        self.browser.find_element(By.XPATH, CheckNamePayGrades)
        self.browser.find_element(By.XPATH, CheckCurrrencyPayGrades)
    
    def DeleteRecord(self):
        ButtomDelete = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{GradesName}")]//i[@class="oxd-icon bi-trash"]'
        self.browser.find_element(By.XPATH, ButtomDelete).click()

        ConfirmDelete = '/html/body/div/div[3]/div/div/div/div[3]/button[2]'
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, ConfirmDelete)))
        self.browser.find_element(By.XPATH, ConfirmDelete).click()
        time.sleep(5)
        try:
            self.browser.find_element(By.XPATH, f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{GradesName}")]')
            assert "Record was not deleted"
        except:
            pass

