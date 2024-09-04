import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://facerecognitionwithrealt-507bc-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

date = {
    "100000":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "100002":
            {
                "name": "Elon Musk",
                "major": "Science",
                "starting_year": 2020,
                "total_attendance": 0,
                "standing": "G",
                "year": 2,
                "last_attendance_time": "2022-12-11 00:54:34"
            }
    
}

for key, value in date.items():
    ref.child(key).set(value)
