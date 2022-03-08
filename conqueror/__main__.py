import sys
import time
import random

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conqueror.msg_generator.messages import generate_message_client

url = None
akceptuje_off = False


def login_into_yandex(driver, yandex_login: str, yandex_password: str):
    # logujemy sie
    driver.find_element_by_class_name("login-dialog-view__button").click()

    time.sleep(1)

    # login
    login_tb = driver.find_element_by_id('passp-field-login')
    login_tb.send_keys(yandex_login)

    # przycisk logowania
    logib_btn = driver.find_element_by_id('passp:sign-in')
    logib_btn.click()

    time.sleep(1)

    # haslo
    login_tb = driver.find_element_by_id('passp-field-passwd')
    login_tb.send_keys(yandex_password)

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

    t2x = "business-rating-edit-view"
    t2 = driver.find_element_by_class_name(t2x)
    t3 = t2.find_elements_by_class_name("business-rating-edit-view__star")
    t3[-1].click()

    print("Zalogowano")
    return True


def spam(url, driver, yandex_login: str, yandex_password: str):
    logged: bool = False

    global akceptuje_off

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

        if not logged:
            logged = login_into_yandex(yandex_login, yandex_password, driver)

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

        time.sleep(0.5)
    except Exception as ex:
        print(ex)


def setup_driver():
    options = Options()
    options = webdriver.ChromeOptions()
    if '--headless' in sys.argv:
        options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver


def chose_random_cites():
    cities = [city['name'] for city in requests.get('https://yandex.henrietta.com.pl/v1/view-cities').json()]
    print("Miasta:", cities)
    random_cites = random.sample(cities, 10)
    return random_cites


def check_what_cites_are_reachable(random_cites) -> tp.List[str]:
    reachable_cites = []
    for city in random_cites:
        resp = requests.get(f'https://yandex.henrietta.com.pl/v1/view-businesses/{city}')
        resp.raise_for_status()
        j = resp.json()
        print("RESP:", j)
        reachable_cites.extend(j)

    return reachable_cites


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('''The correct way to load this script is to'
python -m conqueror <login to yandex> <password to yandex>
''')
        sys.exit(1)

    driver = setup_driver()
    random_cites = chose_random_cites()
    reachable_cites = check_what_cites_are_reachable(random_cites)

    yandex_login, yandex_password = sys.argv[1:3]
    print('Login=', yandex_login, 'password=', yandex_password)
    random.shuffle(target_list)
    print("Pomieszano cele")

    for i in target_list:
        print("Cel:", i)
        spam(f'https://yandex.ru/maps/org/itle/{i}', driver, yandex_login, yandex_password)
    driver.close()
