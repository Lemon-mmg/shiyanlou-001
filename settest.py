import sys
SetTest=set()
InputString=sys.argv[1:]
for i in InputString :
	if i not in SetTest :
	    SetTest.add(i)
print(SetTest)