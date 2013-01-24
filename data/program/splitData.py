import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2

if __name__ == "__main__":

	equation = pyeq2.Models_2D.Exponential.DoubleExponential()

	alpha = 'X\tY\n'
	beta = 'X\tY\n'
	f = open(sys.argv[1],'r')
	while f:
		line = f.readline()
		if len(line) != 0:
			if line[0] != '#':
				data1,data2,data3,data4 = line.split(',')
				alpha = alpha + data1 + "\t" + data2 + "\n"
				beta = beta + data3 + "\t" + data4 
		else:
			break

	fileName = sys.argv[1]

#fit plot to alpha data
	data = alpha
	pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
	equation.Solve()
    
	print("This is for alpha data:\n")
	print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
	print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
	print "Fitted Parameters:"
	for i in range(len(equation.solvedCoefficients)):
		print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])

	alphaFile = open("alphaCoefficients","a")
	alphaFile.write(fileName[0:8] + "," +  str(equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))+",")
	for i in range(len(equation.solvedCoefficients)):
		alphaFile.write(str(equation.solvedCoefficients[i])+",")
	alphaFile.write('\n')

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

	betaFile = open("betaCoefficients","a")
	betaFile.write(fileName[0:8] + "," + str(equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))+",")
	for i in range(len(equation.solvedCoefficients)):
		betaFile.write(str(equation.solvedCoefficients[i])+",")
	betaFile.write('\n')

	alphaFile.close()
	betaFile.close()
	f.close()
