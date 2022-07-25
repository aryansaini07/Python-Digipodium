# create a function for adding value
# create a function for substracting value
#  create a function for multiplying  value
#  create a function for dividing value
def add(a,b):
    sum = a+b
    return sum

def subtract(p,q):
    difference = p-q
    return difference

def multiply(c,d):
    product = c*d
    return product

def division(e,f):
    divide = e/f
    return divide

if __name__=="__main__" :
    print("add =>",add(10,5))
    print("subtract =>",subtract(10,5))
    print("multiply =>",multiply(10,5))
    print("division =>",division(10,5))