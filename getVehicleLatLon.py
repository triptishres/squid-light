from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def VehicleLatLon():
    driver=webdriver.Chrome()
    driver.get('http://192.168.228.217/')

    a=((driver.find_element(By.TAG_NAME, 'p').text).split())
    print(a)
    coordinates=a[3]
    print(coordinates)
    b=coordinates.split(',')
    print(b)

    driver.close()

    return b




# print(lat)
# print(long)
# print(lat,long)
    

# driver.close()


