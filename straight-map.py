import random


if __name__ == '__main__':
    numletters = 26

    letter_nums = []
    source_str = 'DIT IS DE TEKST BERICHT'
    print('source_str =', source_str)
    for letter in source_str:
        if ord(letter) > 64:
            letter_nums.append(ord(letter) - 64)
        else:
            letter_nums.append(ord(letter))
    print('letter_nums = ', letter_nums)
    cipher_keys = []
    print(cipher_keys)

    for i in range(0, len(source_str)):
        n = random.randint(1, numletters)
        cipher_keys.append(n)
    print('cipher_keys = ', cipher_keys)

    encrypt_keys = []
    cipher_text = []
    for i in range(len(source_str)):
        encrypt_keys.append((letter_nums[i] - cipher_keys[i]))
        cipher_text.append(chr(cipher_keys[i] + 64))
    print('encrypt keys', encrypt_keys)
    print('cipher text', cipher_text)
    
    decrypted_nums = []
    decrypted_text = []

    for i in range(len(source_str)):
        decrypted_nums.append((ord(cipher_text[i])-64) + encrypt_keys[i])
        decrypted_text.append(chr(decrypted_nums[i]+64))
    print('decrypted_nums =', decrypted_nums)
    print('decrypted_text =', decrypted_text)