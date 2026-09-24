def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)(4)
print(f)