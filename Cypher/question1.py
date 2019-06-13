#!/bin/python2.7

data = open("message1.txt","r")
text = data.read()
key = input ("Enter # key. only # 1-26 accepted: ")


def encrypt(text,key):
	result = ""
	
	while 0 <  key <= 26:
		#traverse text
		for i in range(len(text)):
			char = text[i]
		
			if char == ' ':
				result += ' '
		
			#encrypt uppercase characters
			elif (char.isupper()):
				result += chr((ord(char) + key-65) % 26 +65)

			#encrpty lowercase characters
			else:
				result += chr((ord(char) + key-97) % 26 + 97)
	
		return result

#check the above function

shiftKey = str(key)
cipher = encrypt(text.strip(),key)
print "Text:" + text
print "Shift Key: " + shiftKey
print "Cipher: " + cipher.lower()
OF=open("outputFile.txt","w")
OF.write(cipher.lower())
