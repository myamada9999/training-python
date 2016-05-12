#! /usr/bin/python

def exception_test(value_1, value_2):
	print "--- start ---"
	result = 0
	try:
		result = value_1 + value_2
	except:
		print "cannot calculation"
	finally:
		print "finish"

	return result

if __name__ == "__main__":
	print exception_test(100, 200)
	print exception_test(100, "200")
