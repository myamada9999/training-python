#! /usr/bin/python

test_list_1 = ['python', '-', 'izm', '.', 'com']
print test_list_1

print '------------------------------------------------------------'

for i in test_list_1:
	print i

test_list_2 = []
print test_list_2

print '------------------------------------------------------------'

test_list_2.append('python')
test_list_2.append('-')
test_list_2.append('izm')
test_list_2.append('.')
test_list_2.append('com')

print test_list_2

test_list_3 = ['python', 'izm', 'com']
print test_list_3

print '------------------------------------------------------------'

test_list_3.insert(1, '-')
test_list_3.insert(3, '.')

print test_list_3

test_list_3.insert(0, 'http://www.')

print test_list_3

test_list_4 = ['1', '2', '3', '2', '1']
print test_list_4

print '------------------------------------------------------------'

test_list_4.remove('2')

print test_list_4

test_list_5 = ['1', '2', '3', '2', '1']
print test_list_5

print '------------------------------------------------------------'

print test_list_5.pop(1)
print test_list_5

print test_list_5.pop()
print test_list_5


test_list_6 = ['1', '2', '3', '2', '1']
print test_list_6

print '------------------------------------------------------------'

print test_list_6.index('2')

test_list_7 = ['1', '2', '3', '2', '1']
print test_list_7

print '------------------------------------------------------------'

print test_list_7.count('2')

for i in range(test_list_7.count('2')):
	test_list_7.remove('2')

print test_list_7
