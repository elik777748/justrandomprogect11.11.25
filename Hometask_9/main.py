import random
def round_float(ndigits=0):
        def a(func):
            def b(*args, **kwargs):
                result = func(*args, **kwargs)
                if isinstance(result, (int, float)) and not isinstance(result, bool):
                    r = round(result, ndigits)
                    if ndigits == 0:
                        r = int(r)
                    return r
                return result  
            return b
        return a

d = 12

@round_float(d)
def float_number():
    return random.uniform(0, 1000)

@round_float()
def float_number_no_d():
    return random.uniform(0, 1000)

@round_float(d)
def string():
    return "hi"

@round_float(d)
def my_bool():
    return True

@round_float(d)
def add(a, b):
    return a / b

print(float_number())
print(string())
print(my_bool())
print(add(5, 3))
print(float_number_no_d())