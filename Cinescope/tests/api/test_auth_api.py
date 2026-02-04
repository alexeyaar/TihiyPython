import pytest
import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT


class TestAuthAPI:
    def test_register_user(self, test_user):
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
        response = requests.post(register_url, json=test_user, headers=HEADERS)

        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_login_user(self,new_user):
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        response = requests.post(login_url, json=new_user, headers=HEADERS)
        assert response.status_code == 200 or 201 , "Ошибка авторизации пользователя"
        response_data = response.json()
        print(response_data)
        assert "accessToken" in response_data, "Отсутствует токен в ответе"
        assert response_data["user"]["email"] ==  new_user["email"], "Некорректный email"
        #Негативные
    def test_login_bad_user(self,new_user):
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        response = requests.post(login_url,
        json={
            "email": new_user['email'],
            "password":"123341"
            }
         )
        data = response.json()
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        assert response.status_code == 401, "Пользователь авторизован с неверным паролем"
        assert "message" in data, "Нет сообщения об ошибке"
    def test_login_not_registration_user(self):
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        response = requests.post(login_url,
        json={
            "email": "v33anTo@gmail.com",
             "password": "123341"
             }
        )
        data = response.json()
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        assert response.status_code == 401, "Авторизация незарегистрированного пользователя"
        assert "message" in data, "Нет сообщения об ошибке"
    def test_login_not_registration_user(self):
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        response = requests.post(login_url,
        json={
             "email": "",
             "password": "123341"
             }
         )
        data = response.json()
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        assert response.status_code == 401, "Авторизация c незаполненным полем email"
        assert "message" in data, "Нет сообщения об ошибке"



