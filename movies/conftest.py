import pytest
import requests
from faker import Faker
from Module_4.movies.constants import HEADERS, BASE_URL
from requester import *
faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    response = requests.post(
        f"{BASE_URL}/auth",
        headers=HEADERS,
        json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"
    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": faker.date(),
            "checkout": faker.date()
        },
        "additionalneeds": faker.text()
    }
@pytest.fixture
def old_user():
    return {
        "firstname": "Alexey",
        "lastname": "ARjdj",
        "totalprice": 63636363,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2034-04-05",
            "checkout": "2023-04-02"
        },
        "additionalneeds": "Wine"
    }
@pytest.fixture
def create_reservation(old_user):
    response = requests.post(f"{BASE_URL}/booking", json= old_user)
    data = response.json()
    book_id = data["bookingid"]
    assert response.status_code == 200, f"Бронирование не создано , код: {response.status_code}"
    return book_id

@pytest.fixture
def booking_data_patch():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name()
    }
@pytest.fixture
def bad_reservation():
    return {
            "lastname": "ARjdj",
            "totalprice": 63636363,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2034-04-05",
                "checkout": "2023-04-02"
            },
            "additionalneeds": "Wine"

    }

@pytest.fixture
def booking_data_patch_bad():
    return {
        "firstname": None,
        "lastname": faker.last_name()
    }

@pytest.fixture(scope="session")
def requesters(auth_session):
    session = requests.Session()
    return CustomRequester(session=auth_session,base_url=BASE_URL)


@pytest.fixture(scope="session")
def public_requester():
    session = requests.Session()
    session.headers.update(HEADERS)
    return CustomRequester(session=session, base_url=BASE_URL)