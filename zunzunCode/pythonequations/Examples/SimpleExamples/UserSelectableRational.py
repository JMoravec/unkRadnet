#! /usr/bin/python
#    Version info: $Id: NonLinearFit2D.py 10 2008-06-28 01:32:52Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


equation = pythonequations.Equations2D.Rational.Polyrational2D('Offset') # this example uses an offset

equation.fittingTarget = 'SSQABS' # see the Equation base class for a list of fitting targets
equation.ConvertTextToData(equation.exampleData) # Equations have ASCII text data for testing and examples

# IMPORTANT NOTE - set these flags BEFORE calling equation.Initialize() immediately below
# These flags are list indices that determine the functions to be used in the rational equation's numerator and denominator
# See the bottom of the file EquationsForPolyfunctionals.py where the function GenerateListForPolyrationals() is used to generate the list
equation.Polyrat2DNumeratorFlags = [0, 1, 4]
equation.Polyrat2DDenominatorFlags = [1, 3]

equation.Initialize() # now that the equation has data and the rational flags are set, we can set up the cache.

checkData = equation.ShouldDataBeRejectedByThisEquation() # test whether the rational can accept the data, the default exampleData above should be OK
if checkData:
    raise Exception(checkData)

# If performing a nonlinear fit and you have parameter estimates, set them
# instead of calling this method.  This call is harmless for linear fits
equation.SetGAParametersAndGuessInitialCoefficientsIfNeeded() # estimate initial parameters if needed

equation.FitToCacheData() # perform the fit

equation.CalculateErrors() # so we can print the errors

print equation.name, str(equation.dimensionality) + "D"
print equation.fittingTarget + ":", equation.CalculateFittingTarget(equation.coefficientArray)
print 'Polyrational flags, numerator:', equation.Polyrat2DNumeratorFlags, '  denominator:', equation.Polyrat2DDenominatorFlags
if equation.extendedName == 'Offset':
    print "Offset extended version was selected"
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
