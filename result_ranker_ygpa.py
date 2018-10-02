import os,requests

def get_data(haystack, needle):
	a = haystack.split(needle)
	b = a[1].split("</span>")
	return b[0]

f1 = open("result.txt", 'w+')
final = []
print "Enter the roll number range (eg : 12616001001 12616001189) : "
start, end = raw_input().split()
print "Enter the sem number (eg : 2) : "
sem = int(input())
print "Enter your choice : "
print "1. Get Results sorted alphabetically"
print "2. Get Results sorted rankwise"
f1.write("https://github.com/niweshgupta\n")
choice = int(input())
for x in range(int(start), int(end) + 1) :
	r = requests.post("http://61.12.70.61:8084/heresult18e.aspx", data={'roll': x, 'sem': sem})
	string = r.text
	if string == "No such student exists in this database" :
		continue
	name = get_data(string, "<span id=\"lblname\">Name  ")
	roll = get_data(string, "<span id=\"lblroll\">Roll No.  ")
	if sem == 2:
		YGPA = get_data(string, "<span id=\"lblbottom3\">YGPA       1st. YEAR: ")
	elif sem == 4:
		YGPA = get_data(string, "<span id=\"lblbottom3\">YGPA       2nd. YEAR: ")
	elif sem == 6 :
		YGPA = get_data(string, "<span id=\"lblbottom3\">YGPA       3rd. YEAR: ")
	else :
		YGPA = get_data(string, "<span id=\"lblbottom3\">YGPA       4th. YEAR: ")
	name = name.encode('ascii', 'ignore').decode('ascii')
	if choice == 1 :
		f1.write(" ".join([roll, name, YGPA, '\n']))
	else :
		tup = (float(YGPA), name, roll)
		final.append(tup)
	print roll, name, YGPA
final.sort(reverse = True)
rank = 1
for s, name, r in final:
	f1.write(" ".join([str(rank), str(s), r, name, '\n']))
	rank += 1
f1.close()
