import os,requests          #first install the requests in the system


def get_data(haystack, needle):
	a = haystack.split(needle)
	b = a[1].split("</span>")
	return b[0]

f1 = open("result.txt", 'w+')
final = []
print "Enter the roll number range (eg : 16616001001 12616001189) : "
start, end = raw_input().split()
print "Enter the sem number (eg : 1 or 2) : "
sem = int(input())
print "Enter your choice : "
print "1. Get Results sorted alphabetically"
print "2. Get Results sorted rankwise"
choice = int(input())
for x in range(int(start), int(end) + 1) :
	r = requests.post("http://136.232.2.202:8084/student19e.aspx", data={'roll': x, 'sem': sem})
	string = r.text
	if string == "No such student exists in this database" :
		continue
	name = get_data(string, "<span id=\"lblname\">Name  ")
	roll = get_data(string, "<span id=\"lblroll\">Roll No.  ")
	if sem == 1:
		SGPA = get_data(string, "<span id=\"lblbottom1\">SGPA       ODD(1st.) SEMESTER: ")
	elif sem == 2:
		SGPA = get_data(string, "<span id=\"lblbottom2\">SGPA       EVEN(2nd.) SEMESTER: ")
	elif sem == 3:
		SGPA = get_data(string, "<span id=\"lblbottom1\">SGPA       ODD(3rd.) SEMESTER: ")
	elif sem == 4:
		SGPA = get_data(string, "<span id=\"lblbottom2\">SGPA       EVEN(4th.) SEMESTER: ")
	elif sem == 5 :
		SGPA = get_data(string, "<span id=\"lblbottom1\">SGPA       ODD(5th.) SEMESTER: ")
	elif sem == 6 :
		SGPA = get_data(string, "<span id=\"lblbottom2\">SGPA       EVEN(6th.) SEMESTER: ")
	elif sem == 7 :
		SGPA = get_data(string, "<span id=\"lblbottom1\">SGPA       ODD(7th.) SEMESTER: ")
	else :
		SGPA = get_data(string, "<span id=\"lblbottom2\">SGPA       EVEN(8th.) SEMESTER: ")
	name = name.encode('ascii', 'ignore').decode('ascii')
	if choice == 1 :
		f1.write(" ".join([roll, name, SGPA, '\n']))
	else :
		tup = (SGPA, name, roll)
		final.append(tup)
	print x
final.sort(reverse = True)
rank = 1
for s, name, r in final:
	f1.write(" ".join([str(rank), s, r, name, '\n']))
	rank += 1
f1.close()
