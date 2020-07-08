print('hello world')
'''
string constant
'''

'''
syntax ruling, structure verbs, adj, objs
symantics  meaning  a=b+c c adding to b equals a. the + and = are the syntax

'''
num = 123
name = 'laura'
line = "hello " + name
print(num)
print(line)


lst = [ 1, 4, 10, "cat", 50, 23] 
print(lst[3])

lst.append(3.5)
print(lst)

lst.append([100, 200, 300])
lst.insert(2, "hello")
print(lst)

lst.remove(10)
print(lst)


for element in lst:
    print(element)

for i in range(6):
    print(lst[i])

''' 
dictonary key value pairs 
{} define dictory 
[] select value from key, also arrays 
foo, boo, moo, indexes 
'''
dic = {
    "foo": 12,
    "boo": "Casper",
    "moo": "Boss"
} 

print(dic)

val = dic["foo"]
print(val)

lst = [1, 4, 10, 10, "cat", 10, 23]
#print(lst)
lst.append(3.5)
lst.append([100, 200, 300])


'''
format string, "f" string 
f'{}'  interpolation
'''
print(f'garabage {val}')

num = 101
print(f'value {num}')



