# Postfix Expression 
# Algorithm
# 1. Evaluate for each character in postfix expression
# 2. If operand is encountered push into stack 
# 3. If operator is encountered pop 2 characters from stack which were already filled in stack. 
# first = top element from stack
# second = second element from stack
# 4. Check for operator & push into stack after operation 
#  second operator first
# 5. return top element from stack.  

a = ["2", "1", "+", "3", "*"]


