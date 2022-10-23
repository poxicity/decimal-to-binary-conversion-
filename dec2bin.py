#Tells you what the program does as well as establishes our Integers.

print ("Enter The Ip Address You Want The Binary Of:")
print (" ")
network1 = int(input ('First Number: '))
network2 = int(input ('Second Number: '))
network3 = int(input ('Third Number: '))
host = int(input ('Fourth Number: '))

#This Section Converts the Decimal into Binary For Each Integer in the first command.  The Second command formats the Integer to 8 places and removes the 0b prefix

network1binary = bin(network1)
network1binaryformated = format(network1, "08b")

network2binary = bin(network2)
network2binaryformated = format(network2, "08b")

network3binary = bin(network3)
network3binaryformated = format(network3, "08b")

hostbinary = bin(host)
hostbinaryformated = format(host, "08b")

#Prints Out Our Results

print (" ")
print ("You Entered: ")
print (network1)
print ("It's Binary Equivalent Is: ")
print (network1binaryformated)

print (" ")
print ("You Entered: ")
print (network2)
print ("It's Binary Equivalent Is: ")
print (network2binaryformated)

print (" ")
print ("You Entered: ")
print (network3)
print ("It's Binary Equivalent Is: ")
print (network3binaryformated)

print (" ")
print ("You Entered: ")
print (host)
print ("It's Binary Equivalent Is: ")
print (hostbinaryformated)
