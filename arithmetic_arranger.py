def arithmetic_arranger(problems, answers=False):
  amount = len(problems)
  if amount > 5: return "Error: Too many problems."

  arranged_problems = ""
  line = ["","","",""]
  rounds = 1

  for problem in (problems):
    problem = problem.split(" ")
    num1_str = problem[0]
    num2_str = problem[2]
    operation = problem[1]

    try:
      num1_int = int(num1_str)
      num2_int = int(num2_str)
    except ValueError:
      return "Error: Numbers must only contain digits."

    if len(num1_str) > 4 or len(num2_str) > 4:
      return "Error: Numbers cannot be more than four digits."

    if operation == "+":
      answer = num1_int + num2_int
    elif operation == "-":
      answer = num1_int - num2_int
    else:
      return "Error: Operator must be '+' or '-'."

    longest_val = max(len(num1_str), len(num2_str))
    width = longest_val + 2
    width_num2 = width - 1
    space = " " * 4

    if rounds == amount: space = ""
    else: rounds += 1

    line[0] += f"{num1_str:>{width}}{space}"
    line[1] += f"{operation}{num2_str:>{width_num2}}{space}"
    line[2] += f"{'-'*width}{space}"
    line[3] += f"{str(answer):>{width}}{space}"

  body = f"{line[0]}\n{line[1]}\n{line[2]}"
  arranged_problems = f"{body}\n{line[3]}" if answers == True else body

  return arranged_problems
