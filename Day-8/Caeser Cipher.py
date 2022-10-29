from string import ascii_lowercase

alphabet = list(ascii_lowercase)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
text = input("Type your message: ").strip().lower()
shift = int(input("Type the shift number: "))

def encrypt(text,shift):
    text = list(text)
    cipher_text = ""
    for i in range(len(text)):
        text_index = alphabet.index(text[i])
        new_index = text_index + shift
        text[i] = alphabet[new_index]
    for letter in text:
        cipher_text += letter
    print(f"The encoded text is {new_text}")

encrypt(text,shift)    
    
