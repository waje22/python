def string_test(s):
    d={"upper_case":0,"lower_case":0}
    for c in s:
        if c.isupper():
           d["upper_case"]+=1
        elif c.islower():
           d["lower_case"]+=1
    else:
         pass
    print("original string:",s)
    print("no.of upper case character:",d["upper_case"])
    print("no.of lower case character:",d["lower_case"])
    string_test("the quik brown fox")

