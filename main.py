def encryption(plainText, keyWord):
    pText = plainText.upper()
    pText = pText.replace(" ", "")
    pText = list(pText)

    keyOrder = getKeyOrder(keyWord)  # to get the order of the keyword

    completeRow = len(pText) // len(keyWord)  # to get the number of complete rows

    if len(pText) % len(keyWord) != 0:  # checking if we have partial rows
        completeRow = completeRow + 1  # if we do, adding additional row

    cipherText = ""  # an empty string to store the ciphertext

    encryptionList = [["-1"] * len(keyWord) for i in range(completeRow)] # creating 2D list and give it initial value -1

    plainTextCounter = 0  # counter for plaintext characters
    for row in range(completeRow):  # loop for the rows
        for column in range(len(keyWord)):  # loop for the column
            try:
                encryptionList[row][column] = pText[plainTextCounter]  # adding the letter to the 2D list
                plainTextCounter += 1  # moving to the next letter

            except IndexError:  # if it reaches the end of the plaintext
                break

    for column in keyOrder:  # accessing the columns in order of the keyword
        for row in range(completeRow):  # reading the row
            if str(encryptionList[row][column]) != "-1":  # checking if it was an empty cell
                cipherText = cipherText + str(encryptionList[row][column])  # adding it to a string to return it

    return cipherText


def decryption(cipherText, keyWord):
    cText = str(cipherText).replace(" ", "")
    cText = cText.upper()

    keyOrder = getKeyOrder(keyWord)  # to get the order of the keyword

    plainText = ""  # an empty string to store the plaintext

    completeRow = len(cText) // len(keyWord)  # to get the number of complete rows
    emptyCells = 0

    if len(cText) % len(keyWord) != 0:  # checking if we have partial rows
        completeRow = completeRow + 1  # if we do, adding additional row
        emptyCells = len(keyWord) - len(cText) % len(keyWord)  # to get the number of empty cells in the last row

    decryptionList = [[-1] * len(keyWord) for i in range(completeRow)]  # creating 2D list and give it initial value -1

    emptyCellsIndex = []  # list to avoid filling empty cells
    for i in range(len(keyWord) - 1, len(keyWord) - 1 - emptyCells, -1):  # go through the 2D list in reverse
        emptyCellsIndex.append(i)  # add the empty cells into the list

    emptyCellsIndex = tuple(emptyCellsIndex)

    if len(cText) % len(keyWord) != 0:  # checking if we have partial rows
        for i in emptyCellsIndex:  # if we do, go through every empty cell by its index
            decryptionList[completeRow - 1][i] = "-2"  # fill empty cells with 0 to avoid reading

    z = 0
    for column in keyOrder:  # loop for the columns
        for row in range(completeRow):  # loop for the rows
            try:
                if decryptionList[row][column] == "-2":  # if it was an empty cell
                    continue  # skip the iteration

                decryptionList[row][column] = cText[z]  # adding the letter to the 2D list
                z = z + 1  # moving to the next letter
            except IndexError:
                break

    for readingRow in range(completeRow):  # selecting the row
        for readingColumn in range(len(keyWord)):  # selecting the column
            if str(decryptionList[readingRow][readingColumn]) != "-1" \
                    and str(decryptionList[readingRow][readingColumn]) != "-2":  # check the empty cells

                plainText = plainText + str(decryptionList[readingRow][readingColumn])  # adding it to a string
                                                                                        # to return it
    return plainText


def getKeyOrder(keyWord):
    keyWord = keyWord.upper()
    orderedKey = sorted(keyWord)  # sort the keyword
    couples = {}  # empty dictionary to add pairs of index and the associated letter

    for i in keyWord:  # go through each letter in the keyword
        index = orderedKey.index(i)  # get the index of the letter according to the ordered keyword
        couples[index] = orderedKey[index]  # adding the letter to its index according
        orderedKey[index] = "-1"  # changing the letter in the ordered keyword to -1 which mean used

    orderedLetterInedex = []  # list to add the order of reading
    indexes = list(couples.keys())  # the indexes of the ordered letters
    for e in range(len(indexes)):  # to go through the number of indexes
        orderedLetterInedex.append(indexes.index(e))  # adding the index to its correct position

    return orderedLetterInedex


def getInput():
    while True:  # if the input was not valid repeat
        text = input("Enter your text: ")
        key = input("Enter your keyword: ")
        key = key.replace(" ","")  # removing spaces

        # check the length of the input and check for numbers and spaces
        if len(text) >= 2 and len(key) >= 2 and key.isalnum():
            break
        else:
            print("Text and key should have at least 2 letters\n"
                  "Text should not contain special characters")

    return text, key


while True:  # menu loop
    print("1- Encryption\n"
          "2- Decryption\n"
          "3- Exit")

    option = input("Choose option: ")
    try:
        option = int(option)
    except ValueError:
        print("ERROR. Please enter a valid option.")

    if option == 1:
        text, key = getInput()
        print("The ciphertext is: " + encryption(text, key))

    elif option == 2:
        text, key = getInput()
        print("The plaintext is: " + decryption(text, key))

    elif option == 3:
        print("Goodbye")
        break
