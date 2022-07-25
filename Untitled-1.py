"""from tracemalloc import start


def compute_gpa(grades, points={'A+':4.5,'A':4.0,'A-':3.67,
        'B+':3.33,'B':3.0,'B-':2.67,
        'C+':2.33,'C':2.0,'C-':1.67,
        'D+':1.33,'D':1.0,'F':0.0,}):
        num_courses=0
        total_points=0
        for g in grades:
            if g in points:
                num_courses+=1
                total_points+=points[g]
        return total_points/num_courses

def range(start, stop = None, step = 1):
    if stop is None:
        stop=start
        start=0"""
        
"""year = int(input('In what year were you born?'))
reply = input('Enter x and y, separated by spaces: ')
pieces = reply.split()
x=float(pieces[0])
y=float(pieces[1])"""

age=int(input('Enter yoyr age in years: '))
max_heart_rate=206.9-(0.67*age)
target=0.65*max_heart_rate
print('Your targe fat-burning heart rate is' , target)