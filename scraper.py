# Initialize web driver
# Download chrome driver
import time
from selenium import webdriver

path_to_chromedriver = '/Users/derek/Downloads/chromedriver'
url = 'https://www.orbitz.com/Flights-Search?trip=roundtrip&leg1=from:Hong%20Kong%2C%20Hong%20Kong%20(HKG-Hong%20Kong%20Intl.),to:Beijing%2C%20China%20(BJS-All%20Airports),departure:01/11/2018TANYT&leg2=from:Beijing%2C%20China%20(BJS-All%20Airports),to:Hong%20Kong%2C%20Hong%20Kong%20(HKG-Hong%20Kong%20Intl.),departure:01/11/2018TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search'

def init_driver():
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    return driver

def lookup():
    driver.get(url)
    results = driver.find_elements_by_xpath('//div[@class="yt-lockup-content"]')
    print(len(results))
    for result in results:
        video = result.find_element_by_xpath('.//h3/a')
        title = video.get_attribute('title')
        url = video.get_attribute('href')
        print("{} ({})".format(title, url))

if __name__ == "__main__":
    driver = init_driver()
    lookup()
    time.sleep(5)
    driver.quit()