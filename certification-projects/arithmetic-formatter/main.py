## Errors
# limit of problem per call is 5, exceeding will return an error 'Error: Too many problems'
# addition and subtraction only, other operators will return an error "Error: Operator must be '+' or '-'."
# each operands must only contain digits, or it will return an error 'Error: Numbers must only contain digits.'
# 4 digits max per problem, exceeding will return an error 'Error: Numbers cannot be more than four digits.'

# same order, first number = top, 2nd number = bottom. 
# there should be a single space between the operator and the longest of the 2 operands
# the operator should be on the same side of the second operand
# numbers should be right aligned
# 4 spaces between each problem
# the dashes should run along the entire problem from the last digit to the operator

def arithmetic_arranger(problems=[], show_answer=False):
    errors = set()

    # Error Handling
    if len(problems) > 5:
        errors.add('Error: Too many problems')

    for problem in problems:
        # Parse
        try:
            left, op, right = problem.split()
        except ValueError:
            errors.add('Error: Must enter two operands.')
        # Operator Check
        for operator in ['+', '-', '*', '/']:
            if operator in problem:
                left, right = problem.split(operator)
                op = operator
            else:
                errors.add("Error: Operator must be '+' or '-'.")

        # Digit Check
        if not left.isdigit() or not right.isdigit():
            errors.add('Error: Numbers must only contain digits.')

        # Length Check
        if len(left) > 4 or len(right) > 4:
            errors.add('Error: Numbers cannot be more than four digits')
        
    if errors:
        print("\n".join(errors))
    
arithmetic_arranger(["23s * 52", "62 + 1", "1 + 1", "5212 / 52", "62 + 1", "12 + 1"])