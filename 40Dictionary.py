WeekDay = {
    "Mo": "Monday",
    "Tu": "Tuesday",
    "We": "Wednesday",
    "Th": "Thursday",
    "Fr": "Friday",
    "Sa": "Saturday",
    "Su": "Sunday",
}


print(WeekDay.get("Sa"))
print(WeekDay["Su"])
print(WeekDay.get("Mi", "You have enter an invalid Day"))