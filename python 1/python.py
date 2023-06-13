# def fun(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)
        
# print(fun(5))

# x = [7,1,6,2,8,3,'hee',7,2,'jll',7,33,'hello']
# y = x.count(5)
# print(y)

x = [1,1,2,2,2]
unq   = set()
dup = []
for i in x:
    if i not in unq:
        unq.add(i)
    else:
        dup.append(i)
print("unq ",unq)
print("dup  ",dup)