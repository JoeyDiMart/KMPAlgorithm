'''
Name: Joseph DiMartino and Zachary Swisher
Class: MAT-285
Program: KMP Algorithm
'''


def failureFunction(pattern):  # create the failure function
    length = len(pattern)  # keep track of the length of string
    table = [0] * length  # create a table (full of 0's for now
    i = 0
    j = 1

    while j < length:  # while loop, iterate over j until the end of the pattern is reached
        if pattern[i] == pattern[j]:  # compare pattern at index i and j
            table[j] = i+1
            i += 1  # increment
            j += 1  # increment
        elif i > 0:
            i = table[i-1]
        else:  # mismatch, no prefix = suffix so reset to 0
            table[j] = 0
            j += 1  # increment j

    return table


def KMP(text, pattern):  # KMP function
    pattern_len = len(pattern)
    text_len = len(text)
    table = failureFunction(pattern)  # call failure function to create prefix table
    first_index = -1  # initially -1 for not found
    i = 0
    j = 0

    while i < text_len:  # go through entire text length, use i to track index
        if text_len - j <= pattern_len - i:  # ensure there's enough text left for the pattern to fit
            if text[i] == pattern[j]:  # compare text and pattern
                first_index = i
                return first_index  # return the first index of the found pattern

        if text[i] == pattern[j]:  # compare the text at i and pattern at j
            j += 1  # increment both
            i += 1
            if j == pattern_len:  # if you've made it to the end of the pattern
                first_index = i-j  # subtract i by the length of pattern to get where the pattern began
                return first_index  # return the index

        else:  # no match
            if j > 0:  # pattern is not pointing at its first position
                j = table[j-1]  # reset j to the value in the previous spot in the table
            else:
                i += 1  # increment i since j is already at first position

    return first_index  # return outside of any loops (will return -1)


text = input("Enter a text to search through: ")  # Search through a String 'text'
pattern = input("Enter a pattern you'd like to search for: ")  # looks for this pattern
print(KMP(text, pattern))  # print the index found, or -1 if not found




