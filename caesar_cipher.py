# C = E(P) = (P+K) mod 26
# P = D(C) = (C+K) mod 26

# KETERANGAN
# C = Cipher text
# E = Enkripsi
# K = Key
# P = Plain text
# D = Dekripsi


def enkripsi(text, shift):
    result = ""

    for x in range(len(text)):
        char = text[x]

        if(char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
            
    return result


text = input("enter text : ")
shift = int(input("enter shift : "))



print("Plain Text : ", text)
print("Pergeseran : ", str(shift))
print("Chiper text: ", enkripsi(text,shift))