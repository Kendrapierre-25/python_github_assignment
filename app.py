print("Welcome to my Python Program")
study_hours = input("How many hours did you study today?")
study_hours = float(study_hours)
weekly_hours = study_hours * 7
print(f"You are on track to study {weekly_hours} hours this week.")
try:
    hours = float(study_hours)
except ValueError:
    print("Please enter a valid number.")
    exit()