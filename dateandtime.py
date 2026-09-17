#Part 1
city = input("Enter the city name: ")
temp = float(input("Enter the temperature in C: "))


#Part 2
if temp > 35:
    print("Warning: It is very hot today!")


#Part 3
if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")

#Part 4

if temp > 35:
    print("Weather: Scorching Hot")
elif temp > 25:
    print("Weather: Warm and sunny")
elif temp > 15:
    print("Weather: Cool and breezy")
else:
    print("Weather: Cold - stay warm!")


#Part 5 - datetime module
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))