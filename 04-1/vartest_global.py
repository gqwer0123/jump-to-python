a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)