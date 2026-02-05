import requests
from constants import BASE_URL, HEADERS
from faker import Faker

def test_method_put(auth_session,booking_data,create_reservation):
        #Изменяем полную информацию бронирования
        resp_put = auth_session.put(f"{BASE_URL}/booking/{create_reservation}", headers=HEADERS, json=booking_data, )
        #Дергаем GET и проверяем что поменялось
        get_response = requests.get(f"{BASE_URL}/booking/{create_reservation}")
        data_get = get_response.json()
        assert get_response.status_code == 200, 'Что то не так пошло'
        #Проверка изменения данных
        assert resp_put.status_code == 200, f"Статус код: {resp_put.status_code}"
        assert data_get['lastname'] == booking_data['lastname'], "Фамилия не изменена"
        assert data_get['totalprice'] == booking_data['totalprice'], "Цена не изменена"
        assert data_get['firstname'] == booking_data['firstname'], "Имя не изменено "
        assert data_get['additionalneeds'] == booking_data['additionalneeds'], "Не изменено"

def test_method_patch(auth_session,booking_data,create_reservation,booking_data_patch):
    #Patch
    response = auth_session.patch(f"{BASE_URL}/booking/{create_reservation}", json= booking_data_patch)
    print(response.status_code)
    print("Запрос", response.request.body)
    print(response.status_code)
    nn = response.text
    print("Ответ",nn)
    #GET
    get_response = requests.get(f"{BASE_URL}/booking/{create_reservation}")
    data = get_response.json()
    print(data)
    #Проверка
    assert get_response.status_code == 200, f"Код: {get_response.status_code}"
    assert data["firstname"] == booking_data_patch["firstname"] , "Имя не изменено "
    assert data["lastname"] == booking_data_patch["lastname"], "Фамилия не изменена"

""" assert data["additionalneeds"] == create_reservation["additionalneeds"] , "Не изменено"
assert data["totalprice"] == create_reservation["totalprice"], "Цена не изменена"""
