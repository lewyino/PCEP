def przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        return True
    return False

print(przestepny(2000))
print(przestepny(2004))
print(przestepny(1900))
print(przestepny(1987))
