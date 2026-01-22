# def f_name():
#     print("hello")
# f_name()

def multi(a , b , *args , **kwargs):
    print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}")
    return a*b
res = multi(3, 4, 5, 7, e=5,y=8)
print(res)
