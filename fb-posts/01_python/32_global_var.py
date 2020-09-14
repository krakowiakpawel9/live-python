var1 = 0


def increment():
    global var1
    var1 += 1


increment()
increment()
print(var1)
