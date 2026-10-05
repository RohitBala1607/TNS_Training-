# Valid Parentheses - Stack
s = "({[]})"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

valid = True

for char in s:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack or stack.pop() != pairs[char]:
            valid = False
            break

if stack:
    valid = False

print(valid)
