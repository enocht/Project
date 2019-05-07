def ToPigLatin(a):
    word = ""
    for i in range(0, len(a)):
        a[i] = a[i].lower()
        a[i] = a[i][1:] + a[i][0] + "ay"
    for i in a:
        word += i + " "
    word = word.capitalize()
    return word

def ToEnglish(b):
    word = ""
    for i in range(0, len(b)):
        b[i] = b[i].lower()
        b[i] = b[i][-3] + b[i][:-3]
    for i in b:
        word += i + " "
    word = word.capitalize()
    return word

a = input("Enter text: ").split()
while True:
    print("Enter 'P' to convert to Pig Latin or 'E' to convert to English")
    language = input().lower()
    if language == "p":
        print(ToPigLatin(a))
        break
    elif language == "e":
        print(ToEnglish(a))
        break
    else:
        print("You have entered an invalid input")