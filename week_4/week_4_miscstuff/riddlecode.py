import string
alpha = list(string.ascii_uppercase)

def shift3(string):
    for letter in string:
        index = alpha.index(letter)
        index_shift = index - 3
        if index_shift > (len(alpha)-1):
            index_shift -= 26
        if index_shift < 0:
            index_shift += 26
        print(alpha[index_shift])

shift3("GHFLSKHU") # Worked! Answer was DECIPHER