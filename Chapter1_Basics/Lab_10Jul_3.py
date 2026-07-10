def check (age):
    if age<0:
        return "age can't be in negative"
    if age<18:
        return "minor"
    return "adult"
print (check (-10))
print (check (10))
print (check (20))
print (check (100))