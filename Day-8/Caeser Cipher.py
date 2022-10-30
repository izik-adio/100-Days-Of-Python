from string import printable

art = """
   ###    ######     ##      ####    ######   #####
  #   #   #         #  #    #    #   #        #    #
 #        #        #    #   #        #        #    #
 #        ####     ######    ####    ####     #####
 #        #        #    #        #   #        #  #
  #   #   #        #    #   #    #   #        #   #
   ###    ######   #    #    ####    ######   #    #
   
              #           #
                          #
      ####   ##    ####   ####    ###   # ##
     #        #    #   #  #   #  #   #  ##
     #        #    #   #  #   #  #####  #
     #        #    #   #  #   #  #      #
      ####   ###   ####   #   #   ###   #
                   #
                   #

"""

def ceaser(direction,text,shift):
    # generate the alphabet a-z
    characters = list(printable) * 2
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for i in range(len(text)):
        if text[i] not in characters:
            cipher_text += text[i]
        else:
            text_index = printable.index(text[i])
            new_index = text_index + shift
            cipher_text += printable[new_index]
    print(f"The {direction}d text is {cipher_text}")      

while True:
    print(art)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip()
    if direction == "encode" or direction == "decode":
        text = input("Type your message: ").strip()
        shift = int(input("Type the shift number: ")) % 100
        ceaser(direction,text,shift)
    else:
        print("Invalid Input")

    opt = input("Would you like to go again.Reply with 'yes' or 'no': ").lower().strip()
    if opt == 'yes':
        True
    else:
        print("Good Bye")
        break
