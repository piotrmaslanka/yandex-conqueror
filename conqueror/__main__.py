import random

if __name__ == '__main__':
    cities = ["Moscow", 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Kazan', 'Nizhny Novgorod', 'Chelyabinsk',
              'Samara','Omsk', 'Rostov-on-Don', 'Ufa', 'Krasnoyarsk', 'Voronezh', 'Perm', 'Volgograd',
              'Krasnodar', 'Saratov', 'Tyumen', 'Tolyatti', 'Izhevsk', 'Barnaul', 'Ulyanovsk', 'Irkutsk',
              'Khabarovsk', 'Makhachkala', 'Yaroslavl', 'Vladivostok', 'Orenburg', 'Tomsk', 'Kemerovo',
              'Novokuznetsk', 'Ryazan', 'Naberezhnye Chelny', 'Astrakhan', 'Kirov', 'Penza', 'Lipetsk',
              'Cheboksary', 'Kaliningrad', 'Tula', 'Sevastopol', 'Stavropol', 'Kursk', 'Ulan-Ude', 'Sochi',
              'Tver', 'Magnitogorsk', 'Ivanovo', 'Bryansk', 'Belgorod']

    chosen_cities = random.sample(cities, 10)

    print('Loading the target list for ', chosen_cities)
