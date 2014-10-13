#print chr(65)

codefile = open("cipher1.txt")

#  65 XOR 42 = 107, then 107 XOR 42 = 65

# print 65 ^ 42

# print 107 ^ 42


def decode_file(code, key):
    # the file is in the format 0,45,6,3,11, etc.
    # first we convert the codefile to an array of numbers
    # then we iterate on that array, translating to the output via the key

    output = ""
    count = 0

    for i in code:
        if i == '':
            continue
        #print i
        #index = count % len(key)
        #print index
        output += chr( int(i) ^ ord(key[count % len(key)]) )
        count += 1

    return output


def iterate_key(key):
    if len(key) == 1:
        if key == 'z':
            return '0'
        else:
            return chr( ord(key) + 1 )
    if key[-1] == 'z':
        return iterate_key(key[:-1]) + 'a'
    else:
        return key[:-1] + chr( ord(key[-1]) + 1 )

key = "aaa"
code = codefile.read()[:-1].split(',')

while False:
#while not "0" in key:
    attempt = decode_file(code, key)
    if " the " in attempt or " THE " in attempt and not "{" in attempt and not "}" in attempt:
        print "success"
        print key
        print attempt
    key = iterate_key(key)

answer = decode_file(code,"god")

total = 0

for i in answer:
    total += ord(i)

print total