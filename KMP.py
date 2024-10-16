'''
Name: Joseph DiMartino and Zachary Swisher
Class: MAT-285
Program: KMP Algorithm
'''


def failureFunction(pattern):
    length = len(pattern)
    table = [0] * len(pattern)  # Initialize table with zeros
    i = 0
    j = 0

    while i < length:
        if pattern[i] == pattern[j]:
            table[j] = i + 1
            i += 1
            j += 1
        elif i > 0:
            i = table[i-1]
        else:
            table[j] = 0
            j += 1

    return table


def KMP(text, pattern):
    pattern_len = len(pattern)
    text_len = len(text)
    table = failureFunction(pattern)
    first_index = -1
    i = 0
    j = 0
    while i < text_len-1:
        print(i, j)
        if text_len - i <= pattern_len - j:
            if text[i] == pattern[j]:
                first_index = i
                return first_index

        if text[i] == pattern[j]:
            j += 1
            i += 1
            if i == pattern_len:
                first_index = i-j
                return first_index

        else:
            if j > 0:
                j = table[j-1]
            else:
                i += 1

    return first_index


text = input("Enter a text to search through: ")
pattern = input("Enter a pattern you'd like to search for: ")

KMP(text, pattern)




