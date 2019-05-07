def FindPalindrome(word):
    lst = []
    big = []
    i = 0
    while i < len(word):
        for j in range(len(word)-1, i, -1):
            if word[i] == word[j]:
                newword = word[i:j+1]
                if newword == newword[::-1]:
                    lst.append(newword)
        i += 1
    if len(lst) > 0:
        longest = lst[0]
        j = 1
        while j < len(lst):
            if len(longest) < len(lst[j]): longest = lst[j]
            j += 1
        big.append(longest)
        i = 0
        while i < len(lst):
            if len(lst[i]) == len(big[0]) and lst[i] not in big: big.append(lst[i])
            i+=1
        return big
    else:
        return "There is no palindrome in the word!"

word = input("Enter word to check for longest palindrome: ")
print(FindPalindrome(word))
