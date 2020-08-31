from datetime import date, time

specialists = {
    "orthopedist": "Orthopedist",
    "cadiologist": "Cadiologist",
    "therapist": "Therapist"
}

medical_structure_address = " 4325 W. Palm Beach Rd., San Francisco, CA "

specialist_mapping={
    "leg": specialists["orthopedist"],
    "heart": specialists["cadiologist"]

}

AVAILABLE_TIMETABLE = {
    specialists['orthopedist'] : {
        'dates': [str(date(2020, 7, day).strftime("%d-%m-%Y")) for day in range(15, 21)],
        'time_slots': [time(hours, int(mins)) for hours, mins in zip(list(range(9,15)), ['30' for min_slot in range(9,15,1)])]
    },
    specialists['cadiologist']: {
        'dates': [str(date(2020, 7, day).strftime("%d-%m-%Y")) for day in range(15, 21)],
        'time_slots': [time(hours, int(mins)) for hours, mins in zip(list(range(11,17)), ['00' for min_slot in range(11,17,1)])]
    }
}



