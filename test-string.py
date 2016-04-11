#! /usr/bin/python

# copied from http://www.python-izm.com/contents/introduction/syntax.shtml

print 'python-izm'
print "python-izm"

test_str = """
test_1
test_2
"""
print test_str

test_str2 = "python"
test_str2 = test_str2 + "-"
test_str2 = test_str2 + "izm"
print test_str2

test_str3 = "012"
test_str3 += "345"
test_str3 += "678"
test_str3 += "9"
print test_str3


test_integer = 100
print str(test_integer) + " yen"

test_str4 = "python-izm"
print test_str4.replace("izm", "ism")

test_str5 = "python-izm"
print test_str5.split("-")
