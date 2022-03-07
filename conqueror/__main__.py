import requests

import random, time
from selenium import webdriver

def loguj(driver, login, haslo):
    login_url = 'https://passport.yandex.ru/auth/welcome?origin=maps'
    driver.get(login_url)
    print(driver.title)
    print(driver.page_source)

    login_tb = driver.find_element_by_id('passp-field-login')
    login_tb.send_keys(login)

    logib_btn = driver.find_element_by_id('passp:sign-in')
    logib_btn.click()

    time.sleep(40)



    #driver.close()



if __name__ == '__main__':
    cities = ["Moscow", 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Kazan', 'Nizhny Novgorod', 'Chelyabinsk',
              'Samara', 'Omsk', 'Rostov-on-Don', 'Ufa', 'Krasnoyarsk', 'Voronezh', 'Perm', 'Volgograd',
              'Krasnodar', 'Saratov', 'Tyumen', 'Tolyatti', 'Izhevsk', 'Barnaul', 'Ulyanovsk', 'Irkutsk',
              'Khabarovsk', 'Makhachkala', 'Yaroslavl', 'Vladivostok', 'Orenburg', 'Tomsk', 'Kemerovo',
              'Novokuznetsk', 'Ryazan', 'Naberezhnye Chelny', 'Astrakhan', 'Kirov', 'Penza', 'Lipetsk',
              'Cheboksary', 'Kaliningrad', 'Tula', 'Sevastopol', 'Stavropol', 'Kursk', 'Ulan-Ude', 'Sochi',
              'Tver', 'Magnitogorsk', 'Ivanovo', 'Bryansk', 'Belgorod']

    chosen_cities = random.sample(cities, 10)

    
    target_list = []

    chosen_cities = [["Kazan", 43]]
    print('Loading the target list for ', chosen_cities)

    driver = webdriver.Chrome()

    for city in chosen_cities:
        resp = requests.get(f'https://yandex.henrietta.com.pl/v1/view-businesses/{city[0]}')
        resp.raise_for_status()
        target_list.extend(resp.json())

    #print('Tne entire target list looks like now: ', target_list)

    for i in target_list:
        url = f'https://yandex.ru/maps/org/itle/{i}'

        loguj(driver, "+48664770776", "test")
        
        driver.get(url)
        print(driver.title)
        print(driver.page_source)



        driver.close()



