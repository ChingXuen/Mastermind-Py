
#import random module for randomizing colours
import random

#User Interface and instruction of game
print('--------------------------------------------------------------------')
print('                     Welcome To Mastermind Game!                    ')
print('--------------------------------------------------------------------')
print()
print('There are a total of 6 colours:')
print('red = r, green = g, blue = b, yellow = y, purple = p, white = w')
print('Try to arrange 4 colours in the correct positions based on feedback.')
print('Type "ENTER" after each guess.')
print('The colours can be repeated.')
print('Please use the initials like "r" as shown above.')
print('There are no limits to the number of attempts you can make.')
print('Starting...')
print()

#while loop to ask user if they want to play again after they guess the code correctly
start_game = 'y'
while start_game.lower() == 'y':

    #Count the number of attempts to get correct answer    
    count = 0    
    #Enter the colours into a list, and then randomize the colours using random.choices
    colours = ['r', 'g', 'b', 'y', 'p', 'w']
    length = 4
    answer = random.choices(colours, k = length)
    guess = []
    print('--------------------------------------------------------------------')
    print('actual answer =', answer)

    #Enter while loop as long as user guess not equal to answer
    while guess != answer:
        #Defined function to ask user for input, then return user guess
        def guess_colour():
            print('red = r, green = g, blue = b, yellow = y, purple = p, white = w')
            guess = []
            
            #Ask user input for each position 
            for count in range(1,5):
                user_guess = input('Enter your guess in position ' + str(count) + ' : ')
                user_guess = user_guess.lower()
                
                #If user enters wrong colour, inform them and ask them to retry
                while user_guess not in colours:
                    print('********************************************************************')
                    print('      ERROR! The colour you entered is not in the game.')
                    print('********************************************************************')
                    print('red = r, green = g, blue = b, yellow = y, purple = p, white = w')
                    user_guess = input('Enter your guess in position ' + str(count) + ' : ')
                    user_guess = user_guess.lower()
                    
                #If user enters correct colour, append into guess list
                guess.append(user_guess)
                    
            #Display user guess in a list after an attempt
            print()
            print('                --------------------')
            print('Your guess is :', guess)
            print('                --------------------')
            return guess
        
        #Define guess + call guess_colour() function
        count += 1
        guess = guess_colour()

        #Nested while loop to ensure feedback is only given if user guess is incorrect
        while guess != answer:        
            #Defined function to check user guess with actual answer
            def check_colour(guess):
                correct_position = 0
                correct_both = []

                #For loop to check if correct colour in correct position, then increment counter
                for position in range(0,4):
                    if guess[position] == answer[position]:
                        correct_position += 1
                        #Append correct colour in correct position into list called correct_both
                        correct_both.append(answer[position])

                #Clone answer using string slicing        
                answer_clone = answer[:]
                wrong_position = 0
                correct_colour = []

                #For loop to check if correct colour but in wrong position
                for position in range(0,4):
                    #If statement to check if correct colour is present. If not present, check next position
                    if guess[position] in answer_clone:
                        
                        #If correct colour in correct position, remove the colour from correct_both and answer_clone, then repeat process
                        #Slowly, correct_both would become empty set
                        if guess[position] in correct_both:
                            correct_both.remove(guess[position])
                            answer_clone.remove(guess[position])
                            
                        #If correct colour but in wrong position, increment counter, and append the colour into 
                        #new list called correct_colour. This is to prevent double counting the colours.
                        elif guess[position] not in correct_colour:
                            wrong_position += 1
                            correct_colour.append(guess[position])
                            
                #Return the counter of correct_position and wrong_position
                return [correct_position, wrong_position]

            #Call check_colour() function and hold the value of correct_position and incorrect_position
            feedback = check_colour(guess)
            #Print feedback based on user guess
            print('Correct colour in correct position:', feedback[0])
            print('Correct colour in wrong position:  ', feedback[1])
            print()
            #Break out of the inner most while loop and ask for user input again
            break

    #If user guess = answer, print message and display the number of attempts
    print()
    print('Congratulations! You took', count, 'attempt(s) to guess the code.')
    print('The correct answer is', answer)
    print()

    #Ask user if they want to play again
    start_game = input('Do you wish to play again? [y/n]: ')

    #While loop in case user inputs wrong selection
    while start_game.lower() != 'y':
        if start_game.lower() == 'n':
            break
        else:
            start_game = input('ERROR! Do you wish to play again? [y/n]: ')
    print()

#Final message after user quit playing
print('Thank you for playing. Have a good day!')
print('--------------------------------------------------------------------')











