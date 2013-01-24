#! /usr/bin/python
#    Version info: $Id: NonLinearFit2D.py 10 2008-06-28 01:32:52Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


spline = pythonequations.Equations3D.Spline.Spline3D()

spline.ConvertTextToData(spline.exampleData) # Equations have ASCII text data for testing and examples

spline.Initialize() # now that the equation has data, set up the cache

spline.smoothingFactor = 0.1
spline.xOrder = 3
spline.yOrder = 3

spline.FitToCacheData() # perform the spline fit

spline.CalculateErrors() # so we can print the errors
spline.CalculateParameterStatistics() # testing to make sure this code works

print spline.name, str(spline.dimensionality) + "D"
for i in range(len(spline.coefficientArray)):
    print "Spline Coefficient " + str(i+1) + ': ' + str(spline.coefficientArray[i])
print
print "Spline Knot 1: " + str(spline.scipySpline.get_knots()[0])
print "Spline Knot 2: " + str(spline.scipySpline.get_knots()[1])
print
for i in range(len(spline.DependentDataArray)):
    print 'X:', spline.IndependentDataArray[0][i],
    print 'Y:', spline.IndependentDataArray[1][i],
    print 'Z', spline.DependentDataArray[i],
    print 'Model:', spline.PredictedArray[i],
    print 'Abs. Error:', spline.AbsoluteErrorArray[i],
    print 'Rel. Error:', spline.RelativeErrorArray[i],
    print 'Percent Error:', spline.PercentErrorArray[i]
