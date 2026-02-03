import requests
"""# Делаем GET запрос к API
response = requests.get('https://restful-booker.herokuapp.com/booking')
data = response.json()
# Смотрим, что нам пришло
print(f"Статус ответа: {response.status_code}")
print(f"Тело ответа: {data}")"""




"""
response = requests.get(f'https://restful-booker.herokuapp.com/booking',
                        params={'firstname': 'Josh'})
data = response.json()
# Тело ответа в словаре
print(f"Тело ответа: {data}")"""

"""
import requests


# отправляем наш запрос
def test_booking():
    url = 'https://restful-booker.herokuapp.com/booking/'
    # делаем словарь для отправки
    data = {
        "firstname": "Alex",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-04",
            "checkout": "2025-01-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{url}", json=data)
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]

    get_response = requests.get(f"{url}{booking_id}")
    response2 = get_response.json()
    assert get_response.status_code == 200
    assert response2["firstname"] == "Alex"

    return data["bookingid"]
"""


"""
url = 'https://restful-booker.herokuapp.com/booking'
# делаем словарь для отправки
data = {
    "firstname": "Alex",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-04",
        "checkout": "2025-01-15"
    },
    "additionalneeds": "Breakfast"
}
response = requests.post(url, json=data)
data = response.json()
print(data["bookingid"])
"""
import requests
"""
def ayload():
    url = 'https://restful-booker.herokuapp.com/booking'
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-04",
            "checkout": "2025-01-15"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, data=payload)
    data = response.text
    print(response.status_code)
    print(response.request.body)
    print(data)
ayload()"""


"""
url = "https://httpbin.org/post"
data = {"key1": "value1", "key2": "value2"}
response = requests.post(url, data=data) # requests сам кодирует словарь в x-www-form-urlencoded
print(response.request.body) # Показывает закодированное тело запроса
print(response.text)"""
"""import requests

REFRESH_TOKEN_URL = "https://example.com/api/token/refresh"

refresh_token = "YOUR_REFRESH_TOKEN"

def refresh_access_token(refresh_token):

    data = {"refresh_token": refresh_token}
    response = requests.post(REFRESH_TOKEN_URL, json=data)

    if response.status_code == 200:
        new_access_token = response.json().get("access_token")
        new_refresh_token = response.json().get("refresh_token")
        return new_access_token, new_refresh_token
    else:
        print(f"Ошибка обновления токена: {response.status_code}")
        return None, None

# Получаем оба токена
new_access_token, new_refresh_token = refresh_access_token(refresh_token)

if new_access_token:
    print(f"Новый access токен: {new_access_token}")
    if new_refresh_token:
        print(f"Новый refresh токен: {new_refresh_token}")

    # Дальше суем в заголовок/куки - в зависимости от реализации
    headers = {"Authorization": f"Bearer {new_access_token}"}
    response = requests.get("https://example.com/api/protected", headers=headers)
    # ..."""

def process_data(data):
    processed_data = transform_data(data)
    result = calculate_result(processed_data)
    return result

def transform_data(data):
    return [x * 2 for x in data]

def calculate_result(data):
    return sum(data)

data = [1, 2, 3]
final_result = process_data(data)
print(final_result)