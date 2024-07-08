print("Welcome to my U.S history and Government knowledge quiz game \nI bet You will like it \nWhat is your name?")
name = input()
print("Welcome to my Quiz game " + name + "." + " Would you like to play " + name +"?")

playing = input()

if playing.lower() == "yes" or playing.lower() == "y":
    print("Good! Let's play")
else:
    quit()

score = 0

answer = input("What year the USA declare independence? ")
if answer == "1776":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is 1776")

answer = input("Who wrote the Declaration of Independence? ")
if answer.upper() == "THOMAS JEFFERSON" or answer.upper() == "THOMAS" or answer.upper() == "JEFFERSON":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is THOMAS JEFFERSON")

answer = input("Who was the first president of the United States? ")
if answer.upper() == "GEORGE WASHINGTON" or answer.upper() == "WASHINGTON" or answer.upper() == "GEORGE":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is GEORGE WASHINGTON")

answer = input("How many states are there in the USA? ")
if answer.upper() == "50 STATES" or answer.upper() == "FIFTY STATES" or answer.upper() == "50" or answer.upper() == "fifty":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is 50 STATES")

answer = input("Which branch of the U.S government makes federal laws? ")
if answer.upper() == "CONGRESS":
        print("Correct!")
        score += 1
else: 
    print("Incorrect! The correct answer is Congress")

answer = input("The passage/ratification of what did the federalist papers support? ")
if answer.upper() == "THE U.S CONSTITUTION" or answer.upper() == "THE CONSTITUTION" or answer.upper() == "CONSTITUTION" or answer.upper() == "US CONSTITUTION":
    print("Correct")
    score += 1
else:
    print("Incorrect! The correct answer is The U.S Constitution")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score / 6) * 100) + "%. Well done for playing")