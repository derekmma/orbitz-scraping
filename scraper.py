# Initialize web driver
# Download chrome driver
import time
from selenium import webdriver

path_to_chromedriver = '/Users/derek/Downloads/chromedriver'
url = 'https://www.orbitz.com'

def init_driver():
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    return driver

def lookup():
    # go to the main page url
    driver.get(url)
    # click the tab to only select flight
    flighttab = driver.find_element_by_id("tab-flight-tab") 
    flighttab.click() 
    # get indicator for 4 inputs
    origin = driver.find_element_by_id("flight-origin")
    dest = driver.find_element_by_id("flight-destination")
    dateDepart = driver.find_element_by_id("flight-departing")
    dateReturn = driver.find_element_by_id("flight-returning")
    # input values for 4 inputs
    origin.send_keys("Hong Kong")
    dest.send_keys("Beijing")
    dateDepart.send_keys("01/11/2018")
    dateReturn.send_keys("01/13/2018")
    # start search
    submitButton = driver.find_element_by_id("search-button") 
    submitButton.click() 
    time.sleep(5)
    # find all flight info module
    results = driver.find_elements_by_xpath('//li[@class="flight-module segment offer-listing"]')
    print('found ',len(results),'flight records')
    for result in results: # for each flight information module
        # get flightinfo from the id attribute in the save element
        flightinfo = result.get_attribute('id')
        # get price
        pricediv = result.find_element_by_xpath('.//div[2]/div/div[2]/div/div')
        price = pricediv.get_attribute('data-test-price-per-traveler')
        print("{} ({})".format(flightinfo, price))

if __name__ == "__main__":
    driver = init_driver()
    lookup()
    time.sleep(5)
    driver.quit()