# TASK:
# Using the following list of cities per country,

#  India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#  USA = ["New York","Chicago","Las Vegas", "San Francisco"]
#  UK = ["London", "Manchester", "Liverpool", "Nottingham"]

# Write a program that asks the user to enter a city name, and it should tell which country the city belongs to

# Write a program that asks users to enter two cities, and it tells you if they both are in the same country or not
# For example:
# If I enter Mumbai and Chennai, it will print "Both cities are in India" but if I enter Mumbai and New York it should print:
# "They don't belong to the same country"India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

# Storing 2 city name as city1 and city2 and making them title. For ex: nEw yOrk --> New York
city1=input("Enter 1st city name: ").title()
city2=input("Enter 2nd city name: ").title()


if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in USA and city2 in USA:
    print("Both cities are in USA")
elif city1 in UK and city2 in UK:
    print("Both cities are in UK")
else:
    print("They don't belong to the same country")

