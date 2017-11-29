import random 

def coinToss(number):
    attempt = 1
    heads = 0
    tails = 0
    outcome = ''
    
    for i in range(1, number):
        flip = random.randint(0,1)

        
        if (flip == 0):
            heads +=1
            outcome = "Heads"
            print "Attempt #", attempt, "flip", outcome, "Heads count", heads, "Tails count", tails

        else: 
            tails += 1
            outcome = "Tails"
            print "Attempt #", attempt, "flip", outcome, "Tails count", tails, "Heads count", heads
        attempt +=1

print coinToss(5000)