# ===============================
#    My Daily Mood Advisor
# ===============================

# PART 1 - USER INPUT
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/tired/stressed/excited): ")
energy = int(input("Enter your energy level from 1 to 10: "))


#PART 2 - IF STATEMENTS
if energy < 3:
    print("Alert: Your energy seems low today. Take some rest if needed.")

if energy >= 5:
    print("You Have enough energy to do something productive today!")
else:
    print("Take it slow today and do something relaxing.")

#PART 3 - IF-ELIF-ELSE STATEMENTS

if mood == "happy":
    advice = "Keep spreading your positive energy!"
elif mood == "sad":
    advice = "Talkto someone you trust or do something that makes you feel better."
elif mood == "tired":
    advice = "Drink water, take a short break, and rest your mind."
elif mood == "stressed":
    advice = "Try deep breathing or make a small to-do list."
else:
    advice = "Every Mood is okay! Take care of yourself"

#PART 4 - DATETIME MODULE
import datetime

today = datetime.datetime.now()

#PART 5 - OUTPUT
print("\n===============================")
print("DAILY MOOD ADVISOR REPORT")
print("===============================")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("===============================")

