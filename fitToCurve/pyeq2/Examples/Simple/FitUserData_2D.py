#    Version info: $Id: FitUserData_2D.py 1 2012-01-07 22:20:43Z zunzun.com@gmail.com $

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



if __name__ == "__main__":

    # see IModel.fittingTargetDictionary
    equation = pyeq2.Models_2D.Exponential.DoubleExponential('SSQABS')
    
    data = '''
      X        Y
	.116	1056.24
	.4		854.12
	.9		655.26
	1.583	508.56
	2.683	339.04
	3.816	311.33
	4.883	270.58
	6.2		242.87
    '''
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
    equation.Solve()
    
    
    ##########################################################
    
    
    print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print "Fitted Parameters:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
