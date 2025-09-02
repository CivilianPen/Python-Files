api_key = '595f5267b8148143014da033953c51bb'
import requests
city_name = 'Moscow'
r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&appid={api_key}').text
r2 = requests.get(f'https://api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={7}&appid={api_key}')
