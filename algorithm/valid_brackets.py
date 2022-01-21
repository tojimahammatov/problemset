'''
    Given is a sequence of '{', '}', '(', ')', '[', ']' ;
    Find whether they form a valid expression/sequence (opening and closing)
'''

def is_valid(s) -> bool:
    if s[0] in ['}', ')', ']']:
        return False
    if len(s) % 2 == 1:
        return False
    stack = [] # we need stack to push opening brackets, and pop when faced closing ones
    for bracket in s:
        if bracket in ['{', '(', '[']:
            stack.append(bracket)
        else:
            opening = stack.pop()
            if opening+bracket not in ['()', '{}', '[]']:
                return False
    return True