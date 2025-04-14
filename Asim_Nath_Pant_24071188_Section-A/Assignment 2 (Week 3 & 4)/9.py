'''
8. Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if it does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.

'''

# Function to add daily temperature to the dictionary
def add_daily_temp(temp_dict, temp_value, day):
    # Only adding the temperature if the day is not already in the dictionary
    if day not in temp_dict:
        temp_dict[day] = temp_value
    else:
        print("Temperature for", day, "is already recorded.")
    
    return temp_dict

# Main Program
# Empty dictionary to hold daily temperatures
weekly_temps = {}

# List of all days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Asking user to enter temperature for each day
for day in days:
    temp = float(input("Enter the average temperature for " + day + ": "))
    weekly_temps = add_daily_temp(weekly_temps, temp, day)

# Displaying the final temperature record
print("\nFinal temperature record:")
for day in weekly_temps:
    print(day + ": " + str(weekly_temps[day]) + "°C")
