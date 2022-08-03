"""
>>> input()
Hello world!
'Hello world!'

>>> x=input()
Hello, world!
>>> x
'Hello, world!'

>>> x=input('문자열을 입력하세요: ')
문자열을 입력하세요: Hello, world!
>>> x
'Hello, world!'

>>> a=input('첫 번째 숫자를 입력하세요: ')
첫 번째 숫자를 입력하세요: 10
>>> b=input('두 번째 숫자를 입력하세요: ')
두 번째 숫자를 입력하세요: 20
>>> print(a+b)
1020

>>> a=input()
10
>>> type(a)
<class 'str'>

>>> a=input('첫 번째 숫자를 입력하세요: ')
첫 번째 숫자를 입력하세요: 10
>>> b=input('두 번째 숫자를 입력하세요: ')
두 번째 숫자를 입력하세요: 20
>>> print(a+b)
1020                #input은 항상 string으로 입력받기 때문에 두 수를 계산하기 위해선 int사용
>>> a=input()
10
>>> type(a)
<class 'str'>

>>> a=int(input('첫 번째 숫자를 입력하세요: '))
첫 번째 숫자를 입력하세요: 10
>>> b=int(input('두 번째 숫자를 입력하세요: '))
두 번째 숫자를 입력하세요: 20
>>> print(a+b)
30
"""