import requests
from constants import BASE_URL, HEADERS
from faker import Faker

def test_get():
    #Запрос несуществующего бронирования (неверный тип данныз)
    response = requests.get(f"{BASE_URL}/booking/black")
    data = response.text
    assert response.status_code == 404, f"Запрос принял неверный тип данных: string "

def test_post(auth_session,bad_reservation):
    #Создание без обязательного поля
    response = auth_session.post(f"{BASE_URL}/booking",json=bad_reservation)

    assert response.status_code == 400 or 500 , "Запрос выполнился без обязательного поля "

def test_put(auth_session,create_reservation):
    #Изменение брони без авторизации
    response = requests.put(f"{BASE_URL}/booking/{create_reservation}")

    assert response.status_code == 401 or 403, "Запрос выполнился без авторизации"

def test_patch(auth_session,create_reservation,booking_data_patch_bad):
    #
    response = auth_session.patch(f"{BASE_URL}/booking/{create_reservation}", json= booking_data_patch_bad)
    data = response.text

    assert response.status_code == 400, f"Запрос выполнился без обязательного поля  {response.status_code}"
