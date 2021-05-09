import random
def randInt(min=0, max=100):
    if min==0:
        num = random.random() * max
        return int(num)
    elif max < 0: #second bonus part
        return("Max is less than zero, enter another number that is higher than zero")
    elif min > 0:
        num = random.random() * (max - min) + min
        return int(num)
    elif min > max: #first bonus part
        placeholder = min
        min = max
        max = placeholder
        if min==0:
            num = random.random() * max
            return int(num)
        elif min > 0:
            num = random.random() * (max - min) + min
            return int(num)
    else:
        pass
# print(randInt())
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#BONUS: account for any edge cases (eg. min > max, max < 0)
# print(randInt(min=500, max=-5))

