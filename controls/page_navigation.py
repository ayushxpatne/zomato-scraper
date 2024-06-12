import time

def scroller(driver,function, user_set_scroll_number):
    
    while scroll_number <= user_set_scroll_number:

        # driver.execute_script('window.scrollTo(0, 1500);')
        driver.execute_script(f'scrollBy(0, 1500)')
        time.sleep(0.5)
        scroll_number += 1