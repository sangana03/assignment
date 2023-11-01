                 return is_balanced(expression[1:], stack)  
    if name == "main":
      input_expression = input("Enter an expression with brackets: ")
    if is_balanced(input_expression):
      print("Brackets are balanced.")
    else:
      print("Brackets are not balanced.")
