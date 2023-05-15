# def pr(num):
    # return num
    # print("hey")
    # yield num
    # print("hey12")
    # yield 2

# print(pr(1))
# x = pr(1)
# print(x)

# print(x.__next__())
# print(x.__next__())
# for i in x:
    # print(i)



s = "absc"
# print(dir(s))
# print(next(s))
s_obj = iter(s)
print(next(s_obj))