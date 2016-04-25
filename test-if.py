#! /usr/bin/python

if __name__ == "__main__":

	value = 2

	if value == 1:
		print "value is 1"
	elif value  == 2:
		print "value is 2"
	elif value  == 3:
		print "value is 3"
	else:
		print "value is the others"

	value_1 = "python"
	value_2 = "izm"

	if value_1 == "Python":
		pass
	elif value_1 == "python" and value_2 == "izm":
		print "second if is true"
	elif value_1 == "IZM" and value_2 == "PYTHON":
		print "third if is true"


