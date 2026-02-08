import pytest
import requests
from constants import BASE_URL, HEADERS
from faker import Faker
from requester import *
from conftest import *
class Test_Negavtive:

    def test_get(self,requesters):
        #Запрос несуществующего бронирования (неверный тип данныз)
        response = requesters.sends_req(
            method="GET",
            endpoint="/booking/black",
            expected_status=404
        )
        data = response.text
        assert response.status_code == 404, f"Запрос принял неверный тип данных: string {response.text}"

    def test_post(self,requesters,bad_reservation):
        #Создание без обязательного поля
        response = requesters.sends_req(
            method="POST",
            endpoint="/booking",
            data=bad_reservation,
            expected_status=400
        )
        assert response.status_code == 400,  "Запрос выполнился без обязательного поля "

    def test_put(self,auth_session,create_reservation,public_requester,booking_data_patch):
        #Изменение брони без авторизации
        response =public_requester.sends_req(
            method="PUT",
            endpoint= f"/booking/{create_reservation}",
            data=booking_data_patch,
            expected_status=403
        )

        assert response.status_code == 401 or 403, "Запрос выполнился без авторизации"

    def test_patch(self, auth_session,create_reservation,booking_data_patch_bad,requesters):

        response =requesters.sends_req(
            method="PATCH",
            data=booking_data_patch_bad,
            endpoint="/booking",
            expected_status=404
        )
        data = response.text

        assert response.status_code == 404, f"Запрос выполнился без обязательного поля firstname в body"
