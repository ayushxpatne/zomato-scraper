from selenium import webdriver
from selenium_stealth import stealth

def prepare_driver():

        chrome_options = webdriver.ChromeOptions()
        # proxy = "180.183.157.159:8080"
        # chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options= chrome_options)

        stealth(driver,
                user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
                languages= ["en-US", "en"],
                vendor=  "Google Inc.",
                platform=  "Win32",
                webgl_vendor=  "Intel Inc.",
                renderer=  "Intel Iris OpenGL Engine",
                fix_hairline= False,
                run_on_insecure_origins= False,
        )

        return driver