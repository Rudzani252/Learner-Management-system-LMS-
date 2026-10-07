from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_invalid_learner_email():

    data = {"learner_id": 1,
        "learner_email": "doesnotexist@gmail.com",
        "course_id": 1}

    response = client.post(
        "/registration",
        json=data)

    assert response.status_code == 200

    result = response.json()

    assert "message" in result
    print(response.json())

def test_missing_email_validation():

    data = {
        "course_id": 1}

    response = client.post(
        "/registration",
        json=data)

    assert response.status_code == 422


def test_missing_course_validation():

    data = {
        "learner_email": "test@gmail.com"}

    response = client.post(
        "/registration",
        json=data)

    assert response.status_code == 422


def test_duplicate_registration():

    data = {"learner_id": 129,
        "learner_email": "rg@gmail.com",
        "course_id": 1
    }

    response = client.post(
        "/registration",
        json=data
    )

    assert response.status_code == 200

    result = response.json()

    assert "already" in result["message"].lower()
    print(response.json())
def has_course_capacity(
    current_registrations,
    capacity=500
):

    return current_registrations < capacity

def test_course_has_capacity():

    result = has_course_capacity(
        499,
        500
    )

    assert result is True


def test_course_is_full():

    result = has_course_capacity(
        500,
        500
    )

    assert result is False