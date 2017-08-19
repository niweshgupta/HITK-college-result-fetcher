import os,requests

def bekar(haystack, needle):
	a = haystack.split(needle)
	b = a[1].split("</span>")
	return b[0]

f1 = open("result.txt", 'w+')
final = []
for x in range(12616001001, 12616001189) :
	r = requests.post("http://61.12.70.61:8084/heresult17.aspx", data={'roll': x, 'sem': 2})
	string = r.text
	if string == "No such student exists in this database" :
		continue
	name = bekar(string, "<span id=\"lblname\">Name  ")
	roll = bekar(string, "<span id=\"lblroll\">Roll No.  ")
	SGPA = bekar(string, "<span id=\"lblbottom2\">SGPA       EVEN(2nd.) SEMESTER: ")
	name = name.encode('ascii', 'ignore').decode('ascii')
	tup = (SGPA, name, roll)
	final.append(tup)
	print x
	# f1.write(" ".join([roll, name, SGPA, '\n']))
final.sort(reverse = True)
rank = 1
for s, name, r in final:
	f1.write(" ".join([str(rank), s, r, name, '\n']))
	rank += 1
f1.close()