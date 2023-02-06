from selenium import webdriver
from selenium.webdriver.common.by import By


#Function to get vehicle's coordinates from the local host
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
