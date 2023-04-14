def checksum(s):
    words = s.split()
    for i in words:
        num = ord(i)[0] + ord(i)[1:]
    return num
s = str(input())
checksum(s)