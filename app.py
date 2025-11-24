#Step 1 : print welcome program
print("Welcome to my Python Program")
#Step 2: Ask user for number of study hours
study_hours = input("How many hours did you study today?")
#Step 3: convert hours into a float to estimate weekly number
study_hours = float(study_hours)
weekly_hours = study_hours * 7
#Step 4: Display Results
# use f-string
print(f"You are on track to study {weekly_hours} hours this week.")
#Step 5: add simple error handling

try:
    hours = float(study_hours)
except ValueError:
    print("Please enter a valid number.")
    exit()