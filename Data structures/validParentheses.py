def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Invalid character
            return False

    return not stack

# Test cases
print(is_valid("({[]})"))  # True
print(is_valid("({[})"))   # False
print(is_valid("()[]{}"))  # True
