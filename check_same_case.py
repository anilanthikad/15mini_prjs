def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1
# =====================

def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1

# ======================

def same_case(a, b):
    upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower = set('abcdefghijklmnopqrstuvwxyz')
    if a in upper and b in upper:
        return 1
    elif a in lower and b in lower:
        return 1
    elif a in upper and b in lower:
        return 0
    elif a in lower and b in upper:
        return 0
    else:
        return -1

# =====================


def same_case(a, b):
    upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower = set('abcdefghijklmnopqrstuvwxyz')
    if a in upper and b in upper or a in lower and b in lower:
        return 1
    elif a in upper and b in lower or a in lower and b in upper:
        return 0
    else:
        return -1

# =====================

same_case('C', 'B')
same_case('b', 'a')
same_case('d', 'd')
same_case('A', 's')
same_case('c', 'B')
same_case('b', 'Z')
same_case('\t', 'Z')
same_case('H', ':')
same_case('H', '0')
