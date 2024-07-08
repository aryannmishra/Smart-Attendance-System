import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-72e73-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "595959":
        {
            "name": "Aryan",
            "major": "English",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "606060":
        {
            "name": "Aryan Mishra",
            "major": "Maths",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "656565":
        {
            "name": "Avinash Dua",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
