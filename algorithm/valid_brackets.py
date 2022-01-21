'''
    Given is a sequence of '{', '}', '(', ')', '[', ']' ;
    Find whether they form a valid expression/sequence (opening and closing)
'''

def is_valid(s) -> bool:
    if s[0] in ['}', ')', ']']:     # valid exp. doesn't start with closing brackets
        return False
    if len(s) % 2 == 1:             # odd-length exp. can't be valid
        return False
    stack = [] # we need stack to push opening brackets, and pop when faced closing ones
    for bracket in s:
        if bracket in ['{', '(', '[']:      # if bracket is opening
            stack.append(bracket)           # keep pushing into the stack
        else:
            opening = stack.pop()           # otherwise, pop and verify it makes valid with closing one
            if opening+bracket not in ['()', '{}', '[]']:
                return False
    return True     # if we are alive till the end, seems exp. is valid