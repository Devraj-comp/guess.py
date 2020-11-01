import random
#Get guess
def get_guess():
    return list(input("What is your guess?"))
x = get_guess()
print(x)

#Generate computer code
def genetate_code():
    digits = [str(num) for num in range(10)]

    #shuffle the digits
    random.shuffle(digits)
    #then grab the first three
    return digits[:3]

#Generate the clues
def generate_clues(code,user_guess):
    if user_guess == code:
        return "Code Cracked!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["nope"]

    else:
        return clues

#Game logic
print("welcome code breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "Code Cracked!":
    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)
    for clue in clue_report:
        print(clue)
