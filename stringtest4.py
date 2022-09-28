str1 = "Hey! What's up? Hello World."
char = ".'!?"

print(str1)
for c in char:
    print(c)
    str1 = str1.replace(c,"")

print(str1)
