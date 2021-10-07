

def arithmetic_arranger(problems, show_results = False):
  results = list()
  first_operands = list()
  second_operands = list()
  operators = list()
  op1 = ""
  op2 = ""
  op = ""
  problemParts = list()
  widthList = list()
  dashList = list()

  for problem in problems:
        parts = problem.split()
        op1 = parts[0]
        op = parts[1]
        op2 = parts[2]
        if len(problems)>5:
          return "Error: Too many problems."
        if op is "/" or op is "*": 
          return "Error: Operator must be '+' or '-'."
        if op1.isdigit() is False or op2.isdigit() is False:
          return "Error: Numbers must only contain digits."
        if len(op1) >4 or len(op2) >4:
          return "Error: Numbers cannot be more than four digits."
        if op == "+":
            result = str(int(op1) + int(op2))
        else:
            result = str(int(op1) - int(op2))
        parts.append(result)
        problemParts.append(parts)
        results.append(result)
        first_operands.append(op1)
        second_operands.append(op2)
        operators.append(op)
  
  for part in problemParts:
        op1 = part[0]
        op2 = part[2]
        result = part[3]
        op1Length = len(op1)
        op2Length = len(op2)
        resultLength = len(result)
        maxLengthProblem = (max(op1Length, op2Length)+2)
        widthList.append(maxLengthProblem)

  for width in widthList:
        dash = "-" * width
        dashList.append(dash)
  spacer = " " * 4
  line1 = ""
  line2 = ""
  dashes = ""
  line3 = ""
  for index in range(len(first_operands)):
    t1 = first_operands[index]
    op = operators[index]
    t2 = second_operands[index]
    result = results[index]
    width = max(len(t1), len(t2))
    dash = dashList[index]

    line1 +=  " " + " " + t1.rjust(width) + " " + " " + " " + " "
    line2 += op + " " + t2.rjust(width)  + " " + " " + " " + " "
    dashes += dash + " " + " " + " " + " "    
    line3 += result.rjust(width+2) + " " + " " + " " + " "

  output = line1 + "\n" + line2 + "\n" + dashes + "\n"
  if show_results:
    output += line3 + "\n"
  return output


    
