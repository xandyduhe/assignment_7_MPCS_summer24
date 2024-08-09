# problem 3
# week 7


import problem2
import math 
import random

def rand_operations():
    operations = ['+', '*', '/', '-']
    return random.choice(operations)

def rand_fraction():
    # random number from 1-9
    numerator = random.randint(1, 9)
    denominator = random.randint(1, 9)
    #simplify 
    return problem2.Fraction(numerator, denominator)

def user_solve_fract():
    '''Solve randomly generated operation on two randomly generated fractions'''

    operation = rand_operations()

    # generate fractions 
    frac1 = rand_fraction()
    frac2 = rand_fraction()

    # addition operation 
    if operation == '+':
        solution = frac1 + frac2

    # multiplication 
    elif operation == '*':
        solution = frac1 * frac2

    # division
    elif operation == '/':
        solution = frac1 / frac2

    # subtraction 
    elif operation == '-':
        solution = frac1 - frac2

    else:
        print('Error. Could not generate operation')

    user_ans = input(f"What is {frac1}  {operation}  {frac2}?\n\t> ")

    if user_ans == str(solution):
        print('Correct!')
        return True
    else:
        print(f'Incorrect! The solution is: {solution}')
        return False 
    
def try_again():
    '''Generate 1 more fraction problem for suer to solve'''

    user_try_again = input("Would you like another problem [y/n]?\n\t> ")

    if user_try_again == 'y': # or 'Y' or '[y]':
        return True 

    elif user_try_again == 'n': # or 'N' or '[n]':
        exit
    
    # invalid input 
    else:
        print('Please enter a "y" for yes, or an "n" for no')
        try_again()
    


def count_trials():
    ''' Count number of trials for user. return total and correct'''

    frac_problem = user_solve_fract()

    # count number of times user answered a question
    if frac_problem is True:
        total_trials = 1
        correct_trials = 1
    elif frac_problem is False:
        total_trials = 1
        correct_trials = 0

    # try again prompt 
    ta = try_again()

    while ta is True:
        frac_problem = user_solve_fract()
            #user ans was true 
        if frac_problem:
            total_trials +=1
            correct_trials += 1

        # user ans false 
        else:
            total_trials += 1

        ta = try_again()

    return correct_trials, total_trials


def main():
        # initial prompt
    print("Welcome to Action Fractions!\n")

    correct, total = count_trials()
    #total_simplified = problem2.Fraction(correct, total)
    print(f'You answered {correct}/{total} prblems correctly. Keep up the good work!')

if __name__ == '__main__':
    main()
