"""
>>> x=10
>>> x
10

>>> y='Hello, world'
>>> y
'Hello, world'

>>> type(x)
<class 'int'>
>>> type(y)
<class 'str'>       #변수 자료형 판별

>>> x,y,z=10,20,30
>>> x
10
>>> y
20
>>> z
30                  

>>> x=y=z=10
>>> x
10
>>> y
10
>>> z
10

>>> x,y=10,20
>>> x,y=y,z
>>> x
20
>>> y
10
"""             #변수 여러개 한번에 만들기