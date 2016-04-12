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

test_str6 = "1234"
print test_str6.rjust(10, "0")
print test_str6.rjust(10, "!")
print test_str6.zfill(10)
print test_str6.zfill(3)

test_str7 = "python-izm"
print test_str7.startswith("python")
print test_str7.startswith("izm")
print "z" in test_str7
print "s" in test_str7

test_str8 = "PyThon-Izm"
print test_str8.upper()
print test_str8.lower()

test_str8 = "    python-izm.com"
print test_str8
test_str8 = test_str8.lstrip()
print test_str8
test_str8 = test_str8.lstrip("python")
print test_str8

test_str9 = "python-izm.com    "
print test_str9 + "/"
test_str9 = test_str9.rstrip()
print test_str9 + "/"
test_str9 = test_str9.rstrip("com")
print test_str9
