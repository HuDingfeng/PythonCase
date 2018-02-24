name = input('please enter your name: ')
print('hello,', name)
print('True and True->',True and True)
print('True and False->',True and False)
print('True or False->',True or False)
print('not True->',not True)
print('not False->',not False)

a = 123 #a是整数
print(a)

b = 'ABC'#b是字符串
print(b)

print('除法9/3->',9/3)
print('整除9//3->',9//3)


#数组操作
classmates = ['Michael','Bob','Tracy']

print(classmates)

print('classmates length ->',len(classmates))

print (classmates[0])

print (classmates[1])

print (classmates[2])

print (classmates[-1])

print (classmates[-2])

print (classmates[-3])

classmates.append('Adam')

print('classmates.append',classmates)

classmates.insert(1,'Jack')

print('classmates.insert',classmates)

classmates.pop()

print('classmates.pop',classmates)

classmates.pop(1)

print('classmates.pop1',classmates)


L = ['Apple', 123, True]

s = ['python', 'java', L, 'scheme']

print(s)

#tuple不可变有序集合 但是tuple内部有list的元素可变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
