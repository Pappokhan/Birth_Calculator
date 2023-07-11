from datetime import date

while True:
    def calculate(birthdate):
        today = date.today()
        age = today.year-birthdate.year-((today.month, today.day)<(birthdate.month, birthdate.day))
        return age
    
    year = int(input("Enter your birth year----------: "))
    month = int(input("Enter your birth month (1-12)--: "))
    day = int(input("Enter your birth day-----------: "))
    birthdate = date(year, month, day)
    age = calculate(birthdate)
    print("You age is:", age)
    
    if age>18:
        print("You are adult...")
    else:
        print("You are not adult...")

    next = input("You want to see more? yes/no: ")
    if next == "no":
        break
    else:
        pass
