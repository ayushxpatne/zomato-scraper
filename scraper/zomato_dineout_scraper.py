
import driver.driver_setup as driver_setup
import scraper.zomato_dinout_scrape_parameters as parameters
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vars.xpaths import XPATHS
from vars.globals import OUTPUT

import time

def zomato_dine_out_scrape(city, more_info, images, scroll_count):
    print(f'zomato_dine_out_scrape: {city} ')
    driver = driver_setup.prepare_driver()
    driver.get(f'https://www.zomato.com/{city}/dine-out')
    output = [OUTPUT.output_ff]

    times_scroll = 0

    try:
        while times_scroll <= scroll_count :

            driver.execute_script(f'scrollBy(0, 1500)')
            time.sleep(0.5)
            
            elements = WebDriverWait(driver=driver, timeout=5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'jumbo-tracker'))
            )

            for element in elements:
                restaurant_name = element.find_element(By.XPATH, XPATHS.name).text
                restaurant_cuisines = element.find_element(By.XPATH, XPATHS.cuisines).text
                restaurant_prices = element.find_element(By.XPATH, XPATHS.prices).text
                restaurant_address = element.find_element(By.XPATH, XPATHS.address).text
                restaurant_link = element.find_element(By.XPATH, XPATHS.zomato_link).get_attribute('href')


                output.append([restaurant_name, restaurant_address, restaurant_prices, restaurant_cuisines, restaurant_link,])

            times_scroll += 1

    finally:
        if images == True and more_info == False:
            output[0] = OUTPUT.output_ft
            parameters.images_form_links(driver, output)
        elif more_info == True and images == False:
            output[0] = OUTPUT.output_tf
            parameters.more_info_from_links(driver, output)
        elif images == True and more_info == True:
            output[0] = OUTPUT.output_tt
            parameters.images_form_links(driver, output)
            parameters.more_info_from_links(driver, output)

        driver.close()

    return output

