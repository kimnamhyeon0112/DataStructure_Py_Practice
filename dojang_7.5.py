# year, month, day, hour, minute, second = input().split()
# print(year, month, day, sep = '-', end = '')
# print('T', end='')
# print(hour, minute, second, sep = ':')

# kor, eng, math, sci = map(int, input().split())
# print(kor >= 90 and eng > 80 and math > 85 and sci >= 80)

# s = '''\'Python\' is a \"programming language\" 
# that lets you work quickly
# and
# integrate systems more effectively.'''
# print(s)

step = int(input())
a = tuple(range(-10, 9, step))
print(a)