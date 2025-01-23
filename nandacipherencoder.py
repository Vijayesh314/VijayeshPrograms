encoder = "vijayeshnandavasanthakumar"
alphabet = "abcdefghijklmnopqrstuvwxyz"

plaintext = str(input("What is the string you want to encode: "))
ciphertext = ""

for i in plaintext:
    if i in alphabet:
        newindex = alphabet.index(i)
        newchar = encoder[newindex]
        ciphertext += newchar
    elif i == " ":
        ciphertext += " "
    else:
        ciphertext += i

print(ciphertext)
