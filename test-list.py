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


