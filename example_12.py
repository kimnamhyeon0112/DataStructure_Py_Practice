# 각 알파벳(a, b, ...)으로 시작하는 단어들을 찾기
# 같은 단어는 중복해서 사용하지 않기
# a로 시작하는 단어 : an, and, attempt....
# b로 시작하는 단어 : be, binary...

import re

str= "Hello, World, Python"
result= re.sub(",", "", str)
print(result)

s1 = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object-oriented programming. Python elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."
s1 += "The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation."
s1 += "This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python most noteworthy features, and will give you a good idea of the language flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library."

char = ".'!?"

s1 = s1.lower()
for c in char:
    s1 = s1.replace(c,"")

strlist = set(s1.split())
print(strlist)

# 0: a, 1: b  .... 25:z

wordlist = [[] for _ in range(26)]

for w in strlist:
    #print(ord(w[0]) - ord('a'))
    wordlist[ord(w[0]) - ord('a')].append(w)
    #print(wordlist[ord(w[0]) - ord('a')])

# print(wordlist)

for i in range(len(wordlist)):
    if len(wordlist[i]) != 0:
        print(chr(ord('a')+i),"로 시작한 단어 모음", wordlist[i])


char = ".,'!?"

# print(s1)
s1 = s1.lower()
# print(s1)
for c in char:
    s1 = s1.replace(c,"")
# print(s1)

strlist = s1.split()

wordlist = {}
for w in strlist:
    if w[0] in wordlist:
        wordlist[w[0]].add(w)
    else:
        wordlist[w[0]] = set()
        wordlist[w[0]].add(w)
    print(wordlist)


keylist = list(wordlist.keys())
keylist.sort()

for w in keylist:
    print(w,"로 시작한 단어 모음", wordlist[w])
print("-"*100)
char = ".,'!?"

# print(s1)
s1 = s1.lower()
# print(s1)
for c in char:
    s1 = s1.replace(c,"")
# print(s1)

strlist = set(s1.split())

wordlist = {}
for w in strlist:
    if w[0] in wordlist:
        wordlist[w[0]].append(w)
    else:
        wordlist[w[0]] = []
        wordlist[w[0]].append(w)
    print(wordlist)


keylist = list(wordlist.keys())
keylist.sort()

for w in keylist:
    print(w,"로 시작한 단어 모음", wordlist[w])