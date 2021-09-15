import random

"""
The object is to start with a text message and produce 2 parts 
of an encrypted version: an encrypted message, plus a decryption key.
Either one is useless without the other. The random element is the non-
discoverable link between them.
"""
if __name__ == '__main__':
    """Using only capital letters, to keep things simple"""
    numletters = 26

    """Treat capital letters as starting at position 1"""
    letter_offset = 64

    letter_nums = []
    source_str = 'DIT IS DE TEKST BERICHT'
    print('source_str =', source_str)
    for letter in source_str:
        """Convert message to equivalent numbers 1 to 26"""
        if ord(letter) > letter_offset:
            letter_nums.append(ord(letter) - letter_offset)
        else:
            """space character will be 32"""
            letter_nums.append(ord(letter))
    print('letter_nums = ', letter_nums)
    cipher_keys = []
    print(cipher_keys)

    for i in range(0, len(source_str)):
        """make a parallel set of random keys for the message letters"""
        n = random.randint(1, numletters)
        cipher_keys.append(n)
    print('cipher_keys = ', cipher_keys)

    encrypt_keys = []
    cipher_text = []
    for i in range(len(source_str)):
        """
        now shift the message letters by the cipher distance
        to produce an encrypted message
        """
        encrypt_keys.append((letter_nums[i] - cipher_keys[i]))
        cipher_text.append(chr(cipher_keys[i] + letter_offset))
    print('encrypt keys', encrypt_keys)
    print('cipher text', cipher_text)
    
    decrypted_nums = []
    decrypted_text = []

    for i in range(len(source_str)):
        """
        example of using the cipher text, plus encrypted message, to 
        re-construct the original message
        """
        decrypted_nums.append((ord(cipher_text[i])-letter_offset) + encrypt_keys[i])
        decrypted_text.append(chr(decrypted_nums[i]+letter_offset))
    print('decrypted_nums =', decrypted_nums)
    print('decrypted_text =', decrypted_text)