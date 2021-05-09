file = open("newfile.txt",mode="w")

context=file.write("hey dudedd u goona rock it")
file=open("newfile.txt",mode="r")
c=file.read()
print(c)
file.close()