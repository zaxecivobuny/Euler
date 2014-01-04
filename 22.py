
def namescore(name, place):
	alphanum = 0
	for j in name:
		alphanum += (ord(j) - 64)
	return alphanum * place

f = open('c:\\lpthw\\euler\\names.txt')
text = f.read()
names = text.split('","')

for k in range(-1, 1):
	temp = ''
	for i in names[k]:
		if not i == '"':
			temp += i
	names[k] = temp

names.sort()
total = 0
count = 1
for i in names:
	total += namescore(i,count)
	count += 1

print total