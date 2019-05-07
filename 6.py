def EnglishtoMorse(a):
    lst = []
    word = ""
    for i in range(0, len(a)):
        for j in a[i]:
            j = j.lower()
            if j == 'a': lst.append(".-")
            elif j == 'b': lst.append("-...")
            elif j == 'c': lst.append("-.-.")
            elif j == 'd': lst.append("-..")
            elif j == 'e': lst.append(".")
            elif j == 'f': lst.append("..-.")
            elif j == 'g': lst.append("--.")
            elif j == 'h': lst.append("....")
            elif j == 'i': lst.append("..")
            elif j == 'j': lst.append(".---")
            elif j == 'k': lst.append("-.-")
            elif j == 'l': lst.append(".-..")
            elif j == 'm': lst.append("--")
            elif j == 'n': lst.append("-.")
            elif j == 'o': lst.append("---")
            elif j == 'p': lst.append(".--.")
            elif j == 'q': lst.append("--.-")
            elif j == 'r': lst.append(".-.")
            elif j == 's': lst.append("...")
            elif j == 't': lst.append("-")
            elif j == 'u': lst.append("..-")
            elif j == 'v': lst.append("...-")
            elif j == 'w': lst.append(".--")
            elif j == 'x': lst.append("-..-")
            elif j == 'y': lst.append("-.--")
            elif j == 'z': lst.append("--..")
    for i in lst:
        word += i + ' '
    return word

def MorsetoEnglish(a):
    lst = []
    word = ""
    for j in a:
        if j == '.-': lst.append("a")
        elif j == '-...': lst.append("b")
        elif j == '-.-.': lst.append("c")
        elif j == '-..': lst.append("d")
        elif j == '.': lst.append("e")
        elif j == '..-.': lst.append("f")
        elif j == '--.': lst.append("g")
        elif j == '....': lst.append("h")
        elif j == '..': lst.append("i")
        elif j == '.---': lst.append("j")
        elif j == '-.-': lst.append("k")
        elif j == '.-..': lst.append("l")
        elif j == '--': lst.append("m")
        elif j == '-.': lst.append("n")
        elif j == '---': lst.append("o")
        elif j == '.--.': lst.append("p")
        elif j == '--.-': lst.append("q")
        elif j == '.-.': lst.append("r")
        elif j == '...': lst.append("s")
        elif j == '-': lst.append("t")
        elif j == '..-': lst.append("u")
        elif j == '...-': lst.append("v")
        elif j == '.--': lst.append("w")
        elif j == '-..-': lst.append("x")
        elif j == '-.--': lst.append("y")
        elif j == '--..': lst.append("z")
        elif j == '/': lst.append(" ")
        else:
            print("You have entered an invalid Morse Code")
            break
    for i in lst:
        word += i
    word = word.capitalize()
    return word

print("Enter English sentence with a space between each word or Morse code with a '/' between each word: ")
a = input().split()
if a[0].isalpha():
    print(EnglishtoMorse(a))
else:
    print(MorsetoEnglish(a))

