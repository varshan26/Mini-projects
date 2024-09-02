alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("encode or decode: ").lower()
text = input("Enter the text: ").lower()
shift = int(input("Enter the shift: "))


def encrypt(original_word,shifted_number):
    encoded_word = ""
    for i in original_word:
        index_number = alphabet.index(i) + shifted_number
        index_number %= len(alphabet)
        encoded_word += alphabet[index_number]
    print("Encoded result: ",encoded_word)

#encrypt(text,shift)

def decrypt(original_word,shifted_number):
    decoded_word = ""
    for i in original_word:
        index_number = alphabet.index(i) - shifted_number
        index_number %= len(alphabet)
        decoded_word += alphabet[index_number]
    print("Decoded Result: ",decoded_word)

#decrypt(text,shift)

def ceasar(original_word,shifted_number,director):
    if director == "encode":
        encoded_word = ""
        for i in original_word:
            index_number = alphabet.index(i) + shifted_number
            index_number %= len(alphabet)
            encoded_word += alphabet[index_number]
        print("Encoded result: ",encoded_word)
    elif director == "decode":
        decoded_word = ""
        for i in original_word:
            index_number = alphabet.index(i) - shifted_number
            index_number %= len(alphabet)
            decoded_word += alphabet[index_number]
        print("Decoded Result: ",decoded_word)
    else:
        print("wrong input!")

ceasar(text,shift,direction)
