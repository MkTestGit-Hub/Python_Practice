age =17
has_license=False
if age>=18:
    if has_license:
        print ("you can drive")
    else:
        print("you need am DL")
elif has_license:
    print("your dl is illegal")
else:    
    print("you are underage")

