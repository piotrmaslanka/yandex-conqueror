import sys
import time
import random

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conqueror.msg_generator.messages import generate_message_client

driver = None
url = None
zalogowano = False


def spam(url):
    global driver, zalogowano

    try:
        print("URL:", url)
        driver.get(url)

        time.sleep(2)

        try:
            a = driver.find_elements_by_xpath("//*[contains(text(), 'Akceptuj')]")
            for i in a:
                i.click()
        except Exception as ex2:
            print(ex2)

        driver.execute_script("window.scrollTo(0, 600)")

        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 600)")

        t1x = "_name_reviews"

        t1 = driver.find_element_by_class_name(t1x)

        t1.click()

        time.sleep(3)

        t3 = driver.find_elements_by_class_name("business-rating-edit-view__star")

        for i in t3:
            print(i.get_attribute('innerHTML'))

        t3[-1].click()

        time.sleep(3)

        if not zalogowano:

            driver.find_element_by_class_name("login-dialog-view__button").click()

            time.sleep(1)


            login_tb = driver.find_element_by_id('passp-field-login')
            login_tb.send_keys(login)

            logib_btn = driver.find_element_by_id('passp:sign-in')
            logib_btn.click()

            time.sleep(1)

            login_tb = driver.find_element_by_id('passp-field-passwd')
            login_tb.send_keys(haslo)

            time.sleep(1)


            driver.find_element_by_class_name("Button2_type_submit").click()

            time.sleep(2)

            try:
                driver.find_element_by_class_name("Button2_view_pseudo").click()
                time.sleep(1)
            except Exception as ex3:
                print(ex3)

            driver.execute_script("window.scrollTo(0, 600)")

            time.sleep(1)

            t2x = "business-rating-edit-view"
            t2 = driver.find_element_by_class_name(t2x)
            t3 = t2.find_elements_by_class_name("business-rating-edit-view__star")
            print("T3")
            t3[-1].click()

            zalogowano = True

        t4 = driver.find_element_by_class_name("textarea__control")
        msg = generate_message_client()
        print('Spaming forth with', msg)
        t4.send_keys(msg)

        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 300)")

        time.sleep(1)

        driver.find_element_by_class_name("business-review-form__controls").find_elements_by_tag_name("div")[0].click()

        print('''OK
OK
OK
OK
OK
OK
OK
OK
OK
OK
OK
OK
OK for url''', url)

        time.sleep(1)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    cities = [city['name'] for city in requests.get('https://yandex.henrietta.com.pl/v1/view-cities').json()]

    if len(sys.argv) < 3:
        print('''The correct way to load this script is to'
python -m conqueror <login to yandex> <password to yandex>
''')

    chosen_cities = random.sample(cities, 10)

    target_list = []

    chosen_cities = [["Kazan", 43]]
    print('Loading the target list for ', chosen_cities)

    options = Options()
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for city in chosen_cities:
        resp = requests.get(f'https://yandex.henrietta.com.pl/v1/view-businesses/{city[0]}')
        resp.raise_for_status()
        target_list.extend(resp.json())

    #print('Tne entire target list looks like now: ', target_list)

    login, haslo = sys.argv[1:3]
    print('Login=', login, 'password=', haslo)
    zalogowano = False

    spam('https://yandex.ru/maps/org/itle/1055926052')
    sys.exit(0)

    for i in random.sample(target_list, 20):
        spam(f'https://yandex.ru/maps/org/itle/{i}')
    driver.close()

