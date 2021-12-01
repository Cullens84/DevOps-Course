print("Welcome to my quiz")
answer = input("do you want to play? (yes/no):")
score = 0
total_questions = 5

if answer.lower() == "yes":
    answer = input(
        " Question 1 : what year did the England football club win the world cup")
    if answer.lower() == "1966":
        score += 1
        print("Correct")
    else:
        print("wrong - 1966 ")

    answer = input("Question 2 : what is the name of liverpools fc's ground")
    if answer.lower() == "anfield":
        score += 1
        print("Correct")
    else:
        print("Wrong anfiel ")

    answer = input(
        "Question 3 : how many miles did the proclaimers claim to walk")
    if answer.lower() == "500":
        score += 1
        print("Correct")
    else:
        print("Wrong - 500 ")

    answer = input("Question 4 : who wrote the lord of the rings")
    if answer.lower() == "jrr tolkien":
        score += 1
        print("Correct")
    else:
        print("Wrong jrr tolkien")

    answer = input("Question 5 : what year was the battle of hastings")
    if answer.lower() == "1066":
        score += 1
        print("Correct")
    else:
        print("wrong 1066 ")

print('Thankyou for Playing this small quiz game, you attempted',
      score, "questions correctly!")
mark = (score/total_questions)*100
print('Marks obtained:', mark)
print('BYE!')
