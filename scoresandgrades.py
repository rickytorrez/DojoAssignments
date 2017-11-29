import random

def grades(iterations):
    print "Your grade is below:"

    for i in range (0, iterations):
        score = random.randint(50, 101)

        if score >= 90 and score <=100:
            print "Your score is: ", score, "You got an A"
        elif score >=80 and score <90:
            print "Your score is: ", score, "You got a B"
        elif score >=70 and score <80:
            print "Your score is: ", score, "You got a C"
        elif score >=60 and score <70:
            print "Your score is: ", score, "You got a D"
        elif score <60:
            print "Your score is: ", score, "You failed, KYS"
        else:
            "Good bye"

grades(10)