#First Python project
print("Welcome to my Quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play the game!")
score = 0

answer = input("What is the capital of Ohio? ")
if answer.lower() == "columbus":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of Alabama? ")
if answer.lower() == "montgomery":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of Florida? ")
if answer.lower() == "tallahassee":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of California? ")
if answer.lower() == "sacramento":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of New York? ")
if answer.lower() == "albany":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of Kentucky? ")
if answer.lower() == "frankfort":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What is the capital of Michigan? ")
if answer.lower() == "lansing":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/7) * 100) + "%" + " correct!")