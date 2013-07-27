""" 
This python program takes data from the full *Activity files generated by the calculate.c program and calculates the coefficients for a double exponential function using that data. It will print the numbers to screen as well as appending the data to two files: alphaCoefficients and betaCoefficients.
"""

import os, sys, inspect,sqlite3,datetime

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2

def fitToCurve(filterID):
	equation = pyeq2.Models_2D.Exponential.DoubleExponential()

	#establish connection to database file
	conn = sqlite3.connect("../sql/radnet.db")
	cur = conn.cursor()

	#get filterid if filterNum was entered
	"""
	if filterID == None:
		cur.execute(SELECT FilterID FROM Filter WHERE FilterNum = ?, (filterNum,))
		filterID = cur.fetchone()
		filterID = int(filterID[0])
	else:
	"""
	filterID = int(filterID)

	# What this section does is reads the data from the file given from the initial argument and formats it so the zunzun.com code can read it. We need two separate Strings so we can have two equations found.
	alpha = 'X\tY\n'
	beta = 'X\tY\n'
	""" reference old code
	alpha = alpha + data1 + "\t" + data2 + "\n"
	beta = beta + data3 + "\t" + data4 + "\n"
	"""
	#get all the data from sql
	cur.execute("""SELECT DeltaT, AlphaAct, BetaAct FROM Activity WHERE FilterID = ?""",(filterID,))
	wholeDate =  cur.fetchall()
	for dataPoint in wholeDate:
		alpha = alpha + str(dataPoint[0]) + "\t" + str(dataPoint[1]) + "\n"
		beta = beta + str(dataPoint[0]) + "\t" + str(dataPoint[2]) + "\n"

	#fit plot to alpha data 

	#get coefficients from zunzun
	data = alpha
	pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
	equation.Solve()
    
	#print coeff to screen
	print("This is for alpha data:\n")
	print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
	print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
	print "Fitted Parameters:"

	for i in range(len(equation.solvedCoefficients)):
		print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])

	#change the coefficients to float type
	alphaInitial1 = float(equation.solvedCoefficients[0])
	alphaLam1 = float(equation.solvedCoefficients[1])
	alphaInitial2 = float(equation.solvedCoefficients[2])
	alphaLam2 = float(equation.solvedCoefficients[3])

	# put data into database
	for i in [(filterID,alphaInitial1,alphaLam1, alphaInitial2, alphaLam2)]:
		cur.execute("""INSERT INTO AlphaCurve (FilterID, Alpha1, Alpha1Lambda, Alpha2, Alpha2Lambda) VALUES (?,?,?,?,?)""", i)
	conn.commit()


	#fit plot to beta data
	data = beta
	pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
	equation.Solve()
    
	print("\nThis is for beta data:\n")
	print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
	print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
	print "Fitted Parameters:"

	for i in range(len(equation.solvedCoefficients)):
		print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])

	betaInitial1 = float(equation.solvedCoefficients[0])
	betaLam1 = float(equation.solvedCoefficients[1])
	betaInitial2 = float(equation.solvedCoefficients[2])
	betaLam2 = float(equation.solvedCoefficients[3])

	for i in [(filterID, betaInitial1, betaLam1, betaInitial2, betaLam2)]:
		cur.execute("""INSERT INTO BetaCurve (FilterID, Beta1, Beta1Lambda, Beta2, Beta2Lambda) VALUES (?,?,?,?,?)""", i)
	conn.commit()
	conn.close()

if __name__ == "__main__":
	fitToCurve(sys.argv[1])
