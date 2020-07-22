import hashlib #importing the library

def sha3_256(str): 
    message=hashlib.sha3_256(str.encode()) #encoding
    return message.hexdigest()     #result in hexadecimal
def sha3_224(str):
    message=hashlib.sha3_224(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format
def sha3_384(str):
    message=hashlib.sha3_384(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format
def sha3_512(str):
    message=hashlib.sha3_512(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format

def main():
    message = input ("\nWhat do you want to hash?: \n")
    decision=input("Select which instance of SHA-3 do you want to use:\n 1. SHA3-224 \n 2. SHA3-256 \n 3. SHA3-384\n 4. SHA3-512. \n")
    if (decision=="1"):
        output = sha3_224(message)  #calling function, result calculation
        print('Selected SHA3-224. Your coded message is: \n' + str(output)) #printing coded output
        main()
    elif (decision == "2"):
        output = sha3_256(message)  #calling function, result calculation
        print("Selected SHA3-256. Your coded message is:  \n" +str(output)) #printing coded output
        main()
    elif (decision =="3"):
        output = sha3_384(message)
        print("Selected SHA3-384. Your coded message is: \n" +str(output))
        main()
    elif(decision == "4"):
        output = sha3_512(message)
        print("Selected SHA3-512. Your coded message is:  \n" +str(output))
        main()
    else:
        print("You may enter only 1, 2, 3 or 4! ")
        main()

main()





import hashlib #importing the library

def sha3_256(str): 
    message=hashlib.sha3_256(str.encode()) #encoding
    return message.hexdigest()     #result in hexadecimal
def sha3_224(str):
    message=hashlib.sha3_224(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format
def sha3_384(str):
    message=hashlib.sha3_384(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format
def sha3_512(str):
    message=hashlib.sha3_512(str.encode()) #encoding
    return message.hexdigest() #result in hexadecimal format

def main():
    message = input ("What do you want to hash?: \n")
    decision=input("Select which instance of SHA-3 do you want to use:\n 1. SHA3-224 \n 2. SHA3-256 \n 3. SHA3-384\n 4. SHA3-512. \n")
    if (decision=="1"):
        output = sha3_224(message)  #calling function, result calculation
        print('Selected SHA3-224. Your coded message is: \n' + str(output)) #printing coded output
    elif (decision == "2"):
        output = sha3_256(message)  #calling function, result calculation
        print("Selected SHA3-256. Your coded message is:  \n" +str(output)) #printing coded output
    elif (decision =="3"):
        output = sha3_384(message)
        print("Selected SHA3-384. Your coded message is: \n" +str(output))
    elif(decision == "4"):
        output = sha3_512(message)
        print("Selected SHA3-512. Your coded message is:  \n" +str(output))
    else:
        print("You may enter only 1, 2, 3 or 4! ") #just tin case
        main()

main()

