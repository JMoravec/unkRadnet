#! /usr/bin/python
#    Version info: $Id: NonLinearFit2D.py 10 2008-06-28 01:32:52Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


equation = pythonequations.Equations2D.Exponential.Exponential2D() # Simple non-linear function

equation.fittingTarget = 'SSQABS' # see the Equation base class for a list of fitting targets
equation.ConvertTextToData(equation.exampleData) # Equations have ASCII text data for testing and examples

equation.Initialize() # now that the equation has data, set up the cache

# Give the equation a sequence of fixed parameters, use the value -1.0E300 for coefficients that are NOT fixed
equation.fixedCoefficientArray = [0.092, -1.0E300]

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
