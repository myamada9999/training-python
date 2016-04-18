#! /usr/bin/python

test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print test_dict_1

print '------------------------------------------------------------'

for i in test_dict_1:
	print i
	print test_dict_1[i]
	print '------------------------------------------------------------'

print test_dict_1['YEAR']

print '------------------------------------------------------------'
print test_dict_1.get('YEAR')
print test_dict_1.get('YEARS')

print '------------------------------------------------------------'
print test_dict_1.get('YEAR', 'NOT FOUND')
print test_dict_1.get('YEARS', 'NOT FOUND')


print '------------------------------------------------------------'

test_dict_2 = {}
test_dict_2['YEAR'] = '2010'
test_dict_2['MONTH'] = '1'
test_dict_2['DAY'] = '20'
print test_dict_2

print '------------------------------------------------------------'
del test_dict_2['DAY']
print test_dict_2

print '------------------------------------------------------------'
print test_dict_2.keys()

print '------------------------------------------------------------'
print test_dict_2.has_key('YEAR')
print test_dict_2.has_key('DAY')

print 'YEAR' in test_dict_2
print 'DAY' in test_dict_2
