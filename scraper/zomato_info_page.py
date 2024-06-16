from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vars.xpaths import XPATHS


def get_more_info(driver, more_info_url):
    driver.get(more_info_url)
    raw_text = r''
    more_info_xpath = '//*[@id="root"]/div/main/div/section[4]/section/section/article[1]/section[1]/h3[3]'
    try:
        element = WebDriverWait(driver=driver, timeout=1).until(
                    EC.presence_of_element_located((By.XPATH, "//*[text()='More Info']"))
                )
        xpath_more_info = get_xpath(element)
        more_info_content_element =  WebDriverWait(driver=driver, timeout=5).until(
                    EC.presence_of_element_located((By.XPATH, f'{xpath_more_info}/following-sibling::div'))
                )
        raw_text += more_info_content_element.text
        return raw_text.split('\n')
    except:
        return ['None']
    

def get_xpath(element: WebElement) -> str:
    n = len(element.find_elements(By.XPATH, "./ancestor::*"))
    path = ""
    current = element
    for _ in range(n):
        tag = current.tag_name
        lvl = len(current.find_elements(By.XPATH, f"./preceding-sibling::{tag}")) + 1
        path = f"/{tag}[{lvl}]{path}"
        current = current.find_element(By.XPATH, "./parent::*")
    return f"/{current.tag_name}{path}"


def get_images(driver, more_info_url):
    driver.get(more_info_url)
    images = []

    xpath_array = [XPATHS.image_1, XPATHS.image_2, XPATHS.image_3, XPATHS.image_4]

    for xpath in xpath_array:
        return_value = get_an_image(driver=driver, timeout=10, image_xpath=xpath)

        if return_value == -1:
            attempt = get_an_image(driver=driver, timeout=10, image_xpath=xpath)
        
        images.append(return_value)
    
    
    return images

    
def get_an_image(driver, timeout, image_xpath):
    try:
        image = WebDriverWait(driver = driver, timeout= timeout).until(
            EC.presence_of_element_located((By.XPATH, image_xpath))
        )
        href = image.get_attribute('src')
        if len(href) != 0:
            output_index = href.find('?output')
            href = href[:output_index]
            return href
        
        return -1
            
    except:
        pass