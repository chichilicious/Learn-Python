import math
def area_circle(radius):
    temp= 2*math.pi*radius**2
    return temp

area_circle(5)

#1 if x > y , 0 if x == y , and -1 if x < y
def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

compare(5,6)
compare(7,7)

#Distance between 2 points 
def dist_two_points(x1,x2,y1,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    distance = math.sqrt(dsquared)
    print(distance)
    return distance

dist_two_points(2,4,3,6)

#hypotenus
def hypotenus(a,b):
    hypo = a**2 + b**2
    hypot = math.sqrt(hypo)
    print(hypot)
    return hypot
    
hypotenus(3,4)

#area of circle with center and perimeter points
def area(xc,xp,yc,yp):
    radius = dist_two_points(xc,xp,yc,yp)
    result = area_circle(radius)
    print("Area is %f"%(result))
    return result

    #or
def area_easy(xc,xp,yc,yp):
    result=area_circle(dist_two_points(xc,xp,yc,yp))
    print(result)
    return result

area(2,4,3,6)
area_easy(2,4,3,6)

#is_between(x, y, z) that returns True if x ≤ y ≤ z or False
def is_between(x,y,z):
    if x <= y <= z:
        return True
    else:
        return False

is_between(2,3,4)

#factorial
def factorial(n):
    if not isinstance(n,int):
        print("we print only integers.sorry")
    elif n<0:
        print("sorry boss. no negetive vibes.")
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse 
        return result

factorial(3)
factorial(-3)
factorial("hey")

def factorial_withstyle(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

factorial_withstyle(5)

#fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(20):
    print(fibonacci(i))

#palindrome
def first(word):
    """Returns the first character of a string."""
    print(word[0])
    return word[0]


def last(word):
    """Returns the last character of a string."""
    print(word[-1])
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    print(word[1:-1])
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome("asddsa"))

#GCD
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter number:"))
b=int(input("2nd no.:"))
GCD=gcd(a,b)
print(GCD)

