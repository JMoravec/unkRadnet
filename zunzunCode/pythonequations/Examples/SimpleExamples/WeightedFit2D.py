#! /usr/bin/python
#    Version info: $Id: LinearFit2D.py 10 2008-06-28 01:32:52Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os;
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


equation = pythonequations.Equations2D.Polynomial.Linear2D() # Straight line

equation.fittingTarget = 'SSQABS' # see the Equation base class for a list of fitting targets




# Note the extra parameter here, this turns on weighted fitting.
# In other, unweighted, fitting examples this method only requires string data
# All data points will require a weight here, unweighted data points are ignored
equation.ConvertTextToData('''

X   Y     Weight

1   1     1
2   2.001 1
3   3     1
4   6     0.15
9   9     This data point has no weight and is completey ignored

''', 1) # note the extra parameter of "1" that turns on weighted fitting




equation.Initialize() # now that the equation has data, set up the cache

# If performing a nonlinear fit and you have parameter estimates, set them
# instead of calling this method.  This call is harmless for linear fits
equation.SetGAParametersAndGuessInitialCoefficientsIfNeeded() # estimate initial parameters if needed

equation.FitToCacheData() # perform the fit

equation.CalculateErrors() # so we can print the errors

print equation.name, str(equation.dimensionality) + "D"
print equation.fittingTarget + ":", equation.CalculateFittingTarget(equation.coefficientArray)
for i in range(len(equation.coefficientArray)):
    print "Coefficient " + equation.coefficientDesignatorTuple[i] + ": " + str(equation.coefficientArray[i])
print
for i in range(len(equation.DependentDataArray)):
    print 'X:', equation.IndependentDataArray[0][i],
    print 'Y', equation.DependentDataArray[i],
    print 'Model:', equation.PredictedArray[i],
    print 'Abs. Error:', equation.AbsoluteErrorArray[i],
    print 'Rel. Error:', equation.RelativeErrorArray[i],
    print 'Percent Error:', equation.PercentErrorArray[i]
