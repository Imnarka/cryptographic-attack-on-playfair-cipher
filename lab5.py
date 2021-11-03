import numpy as np
import itertools

def matrix_with_key(key, plain_text):
    keylist = [c for c in key]
    for c in range(97, 123):
        if len(keylist) == 25:
            break
        if chr(c) not in keylist:
            if chr(c) == 'q':
                if chr(c) not in plain_text:
                    continue
            keylist.append(chr(c))
    k_matrix = np.array(keylist).reshape((5, 5))
    return k_matrix

def get_row_col(char1, char2, matrix):
    global row1, row2, column1, column2
    first, second = False, False
    for i in range(5):
        if char1 in matrix[i] or char2 in matrix[i]:
            for j in range(5):
                if matrix[i][j] == char1:
                    row1, column1 = i, j
                    first = True
                elif matrix[i][j] == char2:
                    row2, column2 = i, j
                    second = True
            if first and second:
                break

def encryption(text, matrix):
    encrypted_text = ''
    global row1, row2, column1, column2

    for k in range(0, len(text), 2):
        get_row_col(text[k], text[k+1], matrix)

        if row1 == row2:
            encrypted_text += matrix[row1][(column1 + 1) % 5] + matrix[row2][(column2 + 1) % 5]
        elif column1 == column2:
            encrypted_text += matrix[(row1 + 1) % 5][column1] + matrix[(row2 + 1) % 5][column2]
        else:
            encrypted_text += matrix[row1][column2] + matrix[row2][column1]
        
        row1, column1, row2, column2 = 0, 0, 0, 0
    return encrypted_text

def decryption(text, key, matrix):
    decrypted_text = ''
    global row1, row2, column1, column2

    for k in range(0, len(text), 2):
        get_row_col(text[k], text[k+1], matrix)

        if row1 == row2:
            decrypted_text += matrix[row1][(column1 - 1) % 5] + matrix[row2][(column2 - 1) % 5]
        elif column1 == column2:
            decrypted_text += matrix[(row1 - 1) % 5][column1] + matrix[(row2 - 1) % 5][column2]
        else:
            decrypted_text += matrix[row1][column2] + matrix[row2][column1]

        row1, column1, row2, column2 = 0, 0, 0, 0
    return decrypted_text

def main():
    dictionary = ['pasword', 'lost', 'through', 'home', 'data', 'lost']
    al = 'abcdefghiklmnopqrstuvwxyz'
    key = input("Enter key: ").replace(" ", "").lower()
    plain_text = 'if you lost or missing something at home'.replace(" ", "").lower()
    if len(plain_text)  % 2 == 1:
        plain_text += 'a'
    row1, column1, row2, column2 = 0, 0, 0, 0
    matrix = matrix_with_key(key, plain_text)
    cipher_text = encryption(plain_text, matrix)
    loop = True
    while loop:
        combinations = np.array(list(map("".join, itertools.permutations(al, 3))))
        count = 0
        for keyWord in combinations:
            keyTest = matrix_with_key(keyWord, cipher_text)
            resultString = decryption(cipher_text, keyTest, matrix)
            for word in dictionary:
                uslovie = (word in resultString)
                if uslovie:
                    count = count + 1
                if count > 0:
                    print(f'Зашифрованный текст: {cipher_text}\n')
                    print('Расшифрованный текст: ', resultString)
                    return resultString

main()