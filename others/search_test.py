import requests

WEATHER_URL = 'http://localhost:8000/es1/weather/?city={}'

city_array = ['北京','上海','广州','滨州','厦门','沈阳','威海','大连','哈尔滨','成都','深圳']
city_many = city_array*10

def test1():
    for i in range(len(city_many)):
        r = requests.get(WEATHER_URL.format(city_many[i]))
        print(str(i) + 'finished!')

test1()