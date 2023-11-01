def isBalanced(expr):
  stack=[]
  for char in expr:
  if char in ["(","[","{"]
  stack.apphend(char)
else:
if not stack:
return false
current_char=stack.pop()
if current_char=='(' :
