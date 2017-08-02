#!/usr/bin/python3
import urllib.request

studentPresent = set()

url = str(input("Enter url of log"))
with urllib.request.urlopen(url) as attendanceList:
	for line in attendanceList:
		line = line.decode('utf-8')
		data = line.split()
		data[1] = data[1].strip('<>')
		studentPresent.add(data[1])
studentPresent.remove('CLASS----')

nick = input("Enter a nick to check attendence")
if nick in studentPresent:
	print("YES " + nick + " is present")
else:
	print(nick + " is not present")

print("list of all the student present today is:")
print(studentPresent)		



 
