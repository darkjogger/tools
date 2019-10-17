import string

## the name of file you want to count words inside.
f = open("file_name.txt")
lines = [line.rstrip('\n') for line in f]

dict = {}

for line in lines:
    list = line.split(" ")
    for word in list:
        word = word.rstrip(string.punctuation).lower()
        if word not in dict.keys():
            dict[word] = 0
        dict[word] += 1

for key, value in dict.items():
    print(f"'{key}' appears {value} time(s) in the file")
