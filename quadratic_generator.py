import random
import sys
import pdb
import re

possible_roots = [-x for x in range(1,10)] + [x for x in range(1,10)]

def generate_roots():
    '''Return tuple (a,b) of positive or negative ints with absolute value between 1 and 9'''
    return (random.choice(possible_roots), random.choice(possible_roots))

def format_quadratic(a,b,c):
    a_term = ('{0}x^2'.format(a) if a != 1 else 'x^2')
    if b == 0:
        b_term = ''
    elif b == -1:
        b_term = '- x'
    elif b < 0:
        b_term = '- {0}x'.format(-b)
    elif b == 1:
        b_term = '+ x'
    else:
        b_term = '+ {0}x'.format(b)
    
    if c == 0:
        c_term = ''
    elif c == -1:
        c_term = '- 1'
    elif c < 0:
        c_term = '- {0}'.format(-c)
    elif c == 1:
        c_term = '+ 1'
    else:
        c_term = '+ {0}'.format(c)
    quadratic = ' '.join([a_term, b_term, c_term])
    quadratic = re.sub(' +', ' ', quadratic)
    return quadratic
    

def generate_question(has_quad_coeff):
    '''
    Return tuple of 2 elements
    First element is a string representing the quadratic
    Second element is a tuple of the two roots
    '''
    (x_1, x_2) = generate_roots()
    a = 1
    if has_quad_coeff:
        a = random.randint(1,10)
    b = a * (x_1 + x_2)
    c = a * (x_1 * x_2)
    return (format_quadratic(a,b,c), (x_1,x_2))

def generate_problems(num_without_quad_coeff, num_with_quad_coeff):
    '''
    Generate list of problem tuples
    specifies number with and without coefficients in front of quadratic term
    '''
    x = num_without_quad_coeff + num_with_quad_coeff
    problem_list = [0]*x
    for num in range(num_without_quad_coeff):
        problem_list[num] = generate_question(False)
    for num in range(num_without_quad_coeff, num_without_quad_coeff + num_with_quad_coeff):
        problem_list[num] = generate_question(True)
    return problem_list

def main():
    if len(sys.argv) != 3:
        print('Usage: python problem_generator.py '
              'num_with_quadratic_coefficients '
              'num_without_quadratic_coefficients')
    num_without_quad_coeff = int(sys.argv[1])
    num_with_quad_coeff = int(sys.argv[2])
    num_problems = num_without_quad_coeff + num_with_quad_coeff
    problems = generate_problems(num_without_quad_coeff, num_with_quad_coeff)
    with open('problems.txt','w') as problems_file:
        for x in range(num_problems):
            problems_file.write('{0}) {1}\n'.format(x+1, problems[x][0]))
        problems_file.write('\n')
        for x in range(num_problems):
            problems_file.write('Solution to {0}: x = {1} or x = {2}\n'\
                               .format(x+1, problems[x][1][0], 
                               problems[x][1][1]))

if __name__ == '__main__':
    main()