from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
        )
    return age

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day: "))

birthdate = date(year, month, day)
age = calculate_age(birthdate)
print("You are:", age, "years old.")
