def solution(cards1, cards2, goal):
    cur1 = 0
    cur2 = 0
    for g in goal:
        if cur1 < len(cards1) and cards1[cur1] == g:
            cur1 += 1
        elif cur2 < len(cards2) and cards2[cur2] == g:
            cur2 += 1
        else:
            return "No"

    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "No"
print(solution(["i", "to", "drink"], ["want", "water"], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "want", "to", "drink", "water"], [], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "want", "to", "drink"], ["water"], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "want", "to", "water"], ["drink"], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "want", "water"], ["to", "drink"], ["i", "want", "to", "drink", "water"])) # "Yes"
print(solution(["i", "want", "water"], ["drink", "to"], ["i", "want", "to", "drink", "water"])) # "No"