'''
9. Write a function named get_daily_temps that prompts the user for the average temperature for each day of the week and returns a dictionary containing the information the user entered.

'''

# Function to get daily average temperatures from the user
def get_daily_temps():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temps = {}  # Empty dictionary to store temperatures

    for day in days:
        temp = float(input(f"Enter the average temperature for {day}: "))
        temps[day] = temp  # Storing temperature in the dictionary

    return temps


# Main program
weekly_temperatures = get_daily_temps()

# Displaying the final dictionary
print("\nAverage temperatures for the week:")
for day in weekly_temperatures:
    print(day + ": " + str(weekly_temperatures[day]) + "°C")
