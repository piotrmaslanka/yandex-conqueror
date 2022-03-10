import typing as tp
import sys
import time
import random
import urllib

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conqueror.msg_generator.messages import generate_message_client

driver = None
url = None
zalogowano = False
akceptuje_off = False


def spam(login, haslo, url):
    global driver, zalogowano, akceptuje_off

    try:
        print("Spam dla URL:", url)
        driver.get(url)

        # klikamy ciasteczka
        if not akceptuje_off:
            time.sleep(2)
            try:
                a = driver.find_elements_by_xpath("//*[contains(text(), 'Akceptuj')]")
                for i in a:
                    i.click()
                akceptuje_off = True
            except Exception as ex2:
                print(ex2)

        # klikamy recenzje
        driver.execute_script("window.scrollTo(0, 600)")
        driver.execute_script("window.scrollTo(0, 600)")
        t1x = "_name_reviews"
        t1 = driver.find_element_by_class_name(t1x)
        t1.click()
        print("Kliknieto przycisk Recenzje")

        # klikamy 5 gwiazdek
        time.sleep(2)
        t3 = driver.find_elements_by_class_name("business-rating-edit-view__star")
        t3[-1].click()
        print("Kliknieto 5 gwiazdek")
        time.sleep(1)
    
        if not zalogowano:
            # logujemy sie
            driver.find_element_by_class_name("login-dialog-view__button").click()

            time.sleep(1)

            # login
            login_tb = driver.find_element_by_id('passp-field-login')
            login_tb.send_keys(login)

            # przycisk logowania
            logib_btn = driver.find_element_by_id('passp:sign-in')
            logib_btn.click()

            time.sleep(1)

            # haslo
            login_tb = driver.find_element_by_id('passp-field-passwd')
            login_tb.send_keys(haslo)

            time.sleep(0.7)

            # przycisk logowania 2
            driver.find_element_by_class_name("Button2_type_submit").click()

            time.sleep(1)

            # przy pierwszym logowaniu ever chce telefon
            try:
                driver.find_element_by_class_name("Button2_view_pseudo").click()
                time.sleep(1)
            except Exception as ex3:
                print(ex3)

            driver.execute_script("window.scrollTo(0, 600)")

            time.sleep(1)

            # klikemy 5 gwiazdek
            t2x = "business-rating-edit-view"
            t2 = driver.find_element_by_class_name(t2x)
            t3 = t2.find_elements_by_class_name("business-rating-edit-view__star")
            t3[-1].click()

            zalogowano = True
            print("Zalogowano")

        # losujemy wiadomosc
        msg = generate_message_client()
        print("Wylosowany komunikat:", msg)

        # wpisujemy wiadomosc
        t4 = driver.find_element_by_class_name("textarea__control")
        print("Zlokalizowano element textarea dla wiadomosci")
        t4.send_keys(msg)
        print("Wpisano wiadomosc")

        # wysylamy recenzje
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        driver.find_element_by_class_name("business-review-form__controls").find_elements_by_tag_name("div")[0].click()

        print('OK for url: ', url)
        try:
            login_encoded = urllib.parse.quote_plus(login)
            requests.get(f'https://yandex.henrietta.com.pl/v1/add-review/{login_encoded}')
        except (requests.RequestException, IOError, OSError):
            print('Could not update the coordinator!')
        time.sleep(0.5)
    except Exception as ex:
        print(ex)


def get_target_list() -> tp.List[str]:
    cities = [city['name'] for city in requests.get('https://yandex.henrietta.com.pl/v1/view-cities').json()]

    chosen_cities = random.sample(cities, 10)

    for city in chosen_cities:
        resp = requests.get(f'https://yandex.henrietta.com.pl/v1/view-businesses/{city}')
        resp.raise_for_status()
        j = resp.json()
        print("RESP:", j)
        target_list.extend(j)

    random.shuffle(target_list)
    return target_list


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('''The correct way to load this script is to'
python -m conqueror <login to yandex> <password to yandex>
''')
        sys.exit(1)

    target_list = []

    options = Options()
    options = webdriver.ChromeOptions()
    if '--headless' in sys.argv:
        print('The software will not function correctly in headless mode, ignoring the command')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    print("Pomieszano cele")
    login, haslo = sys.argv[1:3]
    print('Login=', login, 'password=', haslo)

    try:
        while True:
            for i in get_target_list()[:100]:
                print("Cel:", i)
                spam(login, haslo, f'https://yandex.ru/maps/org/itle/{i}')
    except KeyboardInterrupt:
        print('Aborting')
    driver.close()

