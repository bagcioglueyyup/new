
# Description: This program is simple guessing name works by only in 3 digit numbers. First, first player must write a number and second player should guess what the number is. In every guess step, the program says how many digits of player's number is correct or incorrect

# First player's number input
number_1 = int(input("First Player's Number:"))

# Validate first player's input
while number_1 < 100 or number_1 > 999:
    print("Invalid, try again")
    number_1 = int(input("First Player's Number:"))

# breaks the first player's number into digits
hundreds_1, tens_1, ones_1 = (number_1 // 100), ((number_1 // 10) % 10), (number_1 % 10)

# second player's guess input
number_2 = int(input("Second Player's Guess:"))

# checks if the second player's number is valid or not
while number_2 < 100 or number_2 > 999:
    print("Invalid, try again")
    number_2 = int(input("Second Player's Guess:"))

# start guessing loop
equivalence = False
while not equivalence:
    # if the guess is correct directly cuts loop
    if number_1 == number_2:
        print("3 correct, 0 incorrect")
        equivalence = True
    else:
        # breaks the second player's number into digits
        hundreds_2 = number_2 // 100
        tens_2 = (number_2 // 10) % 10
        ones_2 = number_2 % 10

        # counts correct positions
        correct_position = 0
        if hundreds_1 == hundreds_2:
            correct_position += 1
        if tens_1 == tens_2:
            correct_position += 1
        if ones_1 == ones_2:
            correct_position += 1
        incorrect_position= 3 - correct_position
        
        # print feedback
        print(f"{correct_position} correct, {incorrect_position} incorrect, try again")

        # take a new guess from the second player
        number_2 = int(input("Second Player's Guess:"))

        # checks if the second player's number is valid or not
    while number_2 < 100 or number_2 > 999:
        print("Invalid, try again")
        number_2 = int(input("Second Player's Guess:"))

# congratulate the winner
print("Congrats, you win!")
