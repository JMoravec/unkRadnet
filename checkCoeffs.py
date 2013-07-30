import sqlite3,datetime

conn = sqlite3.connect("sql/test.db")
cur = conn.cursor()

with open("alphaCoefficients", 'r') as f:
	for line in f:
		a = False
		b = False
		c = False
		d = False
		startDate,bla,alpha1,alpha1lambda,alpha2,alpha2lambda,bla2 = line.rstrip().split(',')
		cur.execute("""SELECT AlphaCurve.alpha1, AlphaCurve.Alpha1Lambda, AlphaCurve.Alpha2,AlphaCurve.alpha2Lambda FROM Filter join AlphaCurve on (Filter.FilterID = alphaCurve.FilterID) where filter.startDate = ?""",(startDate,))
		stuff = cur.fetchone()
		if float(stuff[0]) == alpha1 or float(stuff[0]) == alpha2:
			a = True
		if float(stuff[1]) == alpha1lambda or float(stuff[1]) == alpha2lambda:
			b = True
		if float(stuff[2]) == alpha1 or float(stuff[2]) == alpha2:
			c = True
		if float(stuff[3]) == alpha1lambda or float(stuff[3]) == alpha2lambda:
			d = True

		if a == True and b == True and c == True and d == True:
			print 'Good'
		else:
			print startDate

conn.close()
