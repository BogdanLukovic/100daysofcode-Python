import requests
import datetime
import os
import math


def get_exercise_list():
    nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    # os.environ.get("NUTRITIONIX_API_KEY")
    # os.environ.get("NUTRITIONIX_API_KEY")

    nutritionix_headers = {
        "x-app-id": "6fea14f7",
        "x-app-key": "501bbeb0bcbfe3764361878d1e936279",
    }

    nutritionix_params = {
        "query": input("What was your workout? "),
        "gender": "male",
        "weight_kg": 72.5,
        "height_cm": 167.64,
        "age": 30,
    }

    exercise_response = requests.post(url=nutritionix_endpoint,
                                      headers=nutritionix_headers,
                                      json=nutritionix_params)

    exercise_list = exercise_response.json()["exercises"]

    return exercise_list


def get_date_and_time_tuple():
    import datetime

    now = datetime.datetime.now()

    exercise_date = now.strftime("%d/%m/%Y")
    exercise_time = now.strftime("%H:%M:%S")

    return (exercise_date, exercise_time)


def write_workout_to_sheet():
    date_and_time_tuple = get_date_and_time_tuple()

    sheety_endpoint = "https://api.sheety.co/0f16e517c727094072c91490887ed96d/myWorkouts/workouts"

    sheety_headers = {
        "Authorization": os.environ.get("SHEETY_WORKOUT_TOKEN")
    }

    exercise_list = get_exercise_list()

    for exercise in exercise_list:
        exercise_name = exercise["name"]
        exercise_duration = exercise["duration_min"]
        exercise_calories = exercise['nf_calories']

        print(exercise_name, exercise_duration, exercise_calories)

        sheety_json = {
            "workout": {
                'date': date_and_time_tuple[0],
                'time': date_and_time_tuple[1],
                'exercise': exercise_name,
                'duration': math.floor(exercise_duration),
                'calories': math.floor(exercise_calories),
            }
        }

        sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_json)
        print(sheety_response.status_code, sheety_response.text)

write_workout_to_sheet()





# i ran 3 miles and walked 2 miles
