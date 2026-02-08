import requests
from constants import BASE_URL, HEADERS
from faker import Faker
from requester import *
from conftest import *

class TestPut:
    def test_method_put(self,requesters,booking_data,create_reservation):
        #Изменяем полную информацию бронирования
        response = requesters.sends_req(
            method = "PUT",
            endpoint = f"/booking/{create_reservation}",
            data = booking_data

        )
        #Дергаем GET и проверяем что поменялось
        response = requests.get(f"{BASE_URL}/booking/{create_reservation}")
        data_get = response.json()
        assert response.status_code == 200, 'Что то не так пошло'
        #Проверка изменения данных
        assert response.status_code == 200, f"Статус код: {response.status_code}"
        assert data_get['lastname'] == booking_data['lastname'], "Фамилия не изменена"
        assert data_get['totalprice'] == booking_data['totalprice'], "Цена не изменена"
        assert data_get['firstname'] == booking_data['firstname'], "Имя не изменено "
        assert data_get['additionalneeds'] == booking_data['additionalneeds'], "Не изменено"

    def test_method_patch(self,requesters, auth_session,booking_data,create_reservation,booking_data_patch):
        #Patch
         response = requesters.sends_req(
             method="PATCH",
             endpoint=f"/booking/{create_reservation}",
             data=booking_data_patch,
         )

         #GET
         get_response = requests.get(f"{BASE_URL}/booking/{create_reservation}")
         data = get_response.json()
         #Проверка
         assert get_response.status_code == 200, f"Код: {get_response.status_code}"
         assert data["firstname"] == booking_data_patch["firstname"] , "Имя не изменено "
         assert data["lastname"] == booking_data_patch["lastname"], "Фамилия не изменена"

""" assert data["additionalneeds"] == create_reservation["additionalneeds"] , "Не изменено"
assert data["totalprice"] == create_reservation["totalprice"], "Цена не изменена"""
