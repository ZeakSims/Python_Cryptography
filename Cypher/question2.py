#/bin/python2.7
data = open("ceaser1.txt","r")
text = data.read()

def count_dict(text):
    d = {}
    
# count occurances of character
    for w in text: 
        d[w] = text.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))


def dcrypt(text,key):
        result = ""

        while 0 <  key <= 26:
                #traverse text
                for i in range(len(text)):
                        char = text[i]

                        if char == ' ':
                                result += ' '
	
                        elif char == '.':result += '.'
                        
                        elif char == '!':result += '!'
                        
                        elif char == '"':result += '"'
                        
                        elif char == ',':result += ','
                        
                        elif char == ';':result += ';'
		

                        #encrypt uppercase characters
                        elif (char.isupper()):
                                result += chr((ord(char) - key-65) % 26 +65)

                        #encrpty lowercase characters
                        else:
                                result += chr((ord(char) - key-97) % 26 + 97)

                return result

#check the above function

count_dict(text.replace(" ", ""))

key = input ("Enter # key. only # 1-26 accepted: ")
cipher = dcrypt(text.strip(),key)
shiftKey = str(key)
print "Text:" + text
print "Shift Key: " + shiftKey
print "Cipher: " + cipher.lower()
OF=open("outputFile2.txt","w")
OF.write(cipher.lower())
