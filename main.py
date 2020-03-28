import math 
  
# Main
def main():
 
 choice = 0
 
 while choice != 3:
  choice = int(input('Choose \n 1- Encryption \n 2- Decryption \n 3- exit \n'))

  if choice == 1:
     key = input("Enter key: ")
     message = input("Enter a message: ")
     cipher = encrypt(message, key)
     print("Encrypted message: ", cipher)

  elif choice == 2:
     key = input("Enter key: ")
     message = input("Enter a message: ")
     plainText = decrypt(message, key)
     print("Decrypted message: ",plainText)

  elif choice == 3:
   exit()
  else:
    print("Invalid entry, please try again.")
 
# Encryption 
def encrypt(msg, key): 

    msgLength = len(msg)
    msgList = list(msg) 
    
    cols = len(key) 
      
    rows = int(math.ceil(msgLength / cols)) 
   
    empty = int((rows * cols) - msgLength) 
    msgList.extend('x' * empty) 

    cipher = [''] * cols

    for col in range(cols):
      i = col
      while i < len(msgList):
        cipher[col] += msgList[i]
        i += cols
    #print(cipher)

    keyPointer = 0
    keyList = sorted(list(key))
    cipherText = "" 

    for i in range(cols):
      curr = key.index(keyList[keyPointer])
      cipherText += ''.join(cipher[curr])
      keyPointer += 1

   
  
    return cipherText 
  
# Decryption 
def decrypt(cipher, key): 
    
    msgLength = len(cipher)
    msgList = list(cipher) 
  
    cols = len(key) 
     
    rows = int(math.ceil(msgLength / cols)) 
  
    decipher = [] 
    for i in range(rows):
      decipher += [[''] * cols]
    
    keyPointer = 0
    msgPointer = 0
    keyList = sorted(list(key))
  
    for i in range(cols): 
      curr = key.index(keyList[keyPointer])
      for j in range(rows):
        decipher[j][curr] = msgList[msgPointer]
        msgPointer += 1
      keyPointer += 1

    msg = ""

    for i in range(rows):
      msg += ''.join(decipher[i])
  
    emptyCounter = msg.count('x') 
  
    if emptyCounter > 0: 
        return msg[: -emptyCounter] 
  
    return msg 
  
main()