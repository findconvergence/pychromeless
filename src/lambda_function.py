import time

from webdriver_wrapper import WebDriverWrapper

def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.google.com/')

    driver.set_input_value('//input[@title="Search"]', '21 buttons')


    driver.click('//div[@class="VlcLAe"]//input[@value="Google Search"]')
    time.sleep(0.5)

    first_google_result_title = driver.get_inner_html('(//div[@class="rc"])[1]//div[@class="r"]//a//h3')

    print("--------------------------")
    print(first_google_result_title)
    print("--------------------------")

    driver.close()
