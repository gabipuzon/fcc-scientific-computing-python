def arithmetic_arranger(problems=[], show_answer=False):
    errors = []

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    # Error Handling
    if len(problems) > 5:
        errors.append('Error: Too many problems.')

    for problem in problems:
        # Parse
        try:
            left, operator, right = problem.split()
        except ValueError:
            errors.append('Error: Invalid problem format.')
            continue

        # Operator Check
        if operator not in ['+', '-']:
            errors.append("Error: Operator must be '+' or '-'.")
            continue

        # Digit Check
        if not left.isdigit() or not right.isdigit():
            errors.append('Error: Numbers must only contain digits.')
            continue

        # Length Check
        if len(left) > 4 or len(right) > 4:
            errors.append('Error: Numbers cannot be more than four digits.')
            continue
        else:
            width = max(len(left), len(right)) + 2
            top = left.rjust(width)
            bottom = operator + right.rjust(width - 1)
            dash = '-' * width

            if operator == '+':
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))

            formatted_answer = answer.rjust(width)
            answer_line.append(formatted_answer)
            top_line.append(top)
            bottom_line.append(bottom)
            dash_line.append(dash)

    if errors:
        return '\n'.join(errors)

    joined_top = '    '.join(top_line)
    joined_bottom = '    '.join(bottom_line)
    joined_dash = '    '.join(dash_line)
    joined_answer = '    '.join(answer_line)

    output = [joined_top, joined_bottom, joined_dash]

    if show_answer:
        output.append(joined_answer)
        return '\n'.join(output)
    else:
        return '\n'.join(output)