char=input("Enter a single character")
if char.isdigit():
    print("char is digit")
elif char.isalpha():
    if char.lower() in 'aeiou':
        print ("char is vowel")
    else :
        print("char is consonant")
else:
    print("char is special symbol")