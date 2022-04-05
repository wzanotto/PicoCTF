file = open('file.txt','r')
Lines = file.readlines()
s = ""
for line in Lines:
	s += chr(int(line))
print(s)
