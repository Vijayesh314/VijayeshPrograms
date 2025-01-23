encod = "vijayeshnandavasanthakumar"
alpha = "abcdefghijklmnopqrstuvwxyz"

ciphertext = str(input("What is the string you want to decode: "))
plaintext = ""

def differences(char, encod, alpha):
    possibilities = []
    for index in range (len(encod)): 
        if encod[index] == char:
            possibilities.append(alpha[index])
    return possibilities

decodings = []
for i in ciphertext.lower():
    if i in encod:
        possibilities = differences(i, encod, alpha)
        decodings.append(possibilities)
    elif i == " ":
        plaintext += " "
    else:
        plaintext += i

print(plaintext)
