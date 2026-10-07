import cProfile
import pstats
import requests


def profile_registration():

    data = {
        "learner_id": 129,
        "learner_email": "rg@gmail.com",
        "course_id": 1
    }

    response = requests.post(
        "http://127.0.0.1:8000/registration",
        json=data,
        timeout=10
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":

    profiler = cProfile.Profile()

    profiler.enable()

    for i in range(10):
        profile_registration()

    profiler.disable()

    profiler.dump_stats("registration_profile.prof")

    stats = pstats.Stats(profiler)

    stats.sort_stats("cumulative")

    stats.print_stats(20)