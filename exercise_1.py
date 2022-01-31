str1 = "P@#yn26at^&i5ve"
alphabets = 0
digits = 0
special = 0

for i in range(len(str1)):
    if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')):
        alphabets = alphabets + 1
    elif(str1[i] >= '0' and str1[i] <= '9'):
        digits = digits + 1
    else:
        special = special + 1

print("Chars:  ", alphabets)
print("Digits:  ", digits)
print("Symbol:  ", special)