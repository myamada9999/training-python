#! /usr/bin/python

if __name__ == "__main__":

	for_sample = []
	for_sample.append("python")
	for_sample.append("-")
	for_sample.append("izm")
	for_sample.append("for")
	for_sample.append("statement")
	for_sample.append("sample")

	for value in for_sample:
		print value

	counter = 0
	while counter < 10:
		counter += 1
		print counter

	for num in range(100):
		print num
		if num == 10:
			break;

	for num in range(100):
		if num % 10:
			continue

		print num
