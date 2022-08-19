sequence = input()

are_balanced = True

opening_brackets = []

for ch in sequence:
    if ch in '({[':
        opening_brackets.append(ch)

    elif not opening_brackets:
        are_balanced = False
        break
    else:
        last_opening_bracket = opening_brackets.pop()
        if f"{last_opening_bracket}{ch}" not in '(){}[]':
            are_balanced = False
            break

if are_balanced and not opening_brackets:
    print("YES")
else:
    print("NO")


# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
#
# Input:
# • On a single line, you will receive a sequence of parentheses.
#
# Output:
# • For each test case, print on a new line "YES" if the parentheses are balanced.
# • Otherwise, print "NO"
#
# Constraints:
# • 1 ≤ lens ≤ 1000, where the lens is the length of the sequence
# • Each character of the sequence will be one of {, }, (, ), [, ]
