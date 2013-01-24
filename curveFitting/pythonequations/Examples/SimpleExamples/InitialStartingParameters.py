#! /usr/bin/python
#    Version info: $Id: InitialStartingParameters.py 309 2011-05-19 20:00:31Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations, numpy


# This equation is very sensitive to starting parameters - see http://www.nbb.cornell.edu/neurobio/land/PROJECTS/MKG23curvefit/index.html
equation = pythonequations.Equations2D.BioScience.CellularConductance2D('Offset') # Non-linear function with offset


equation.fittingTarget = 'SSQABS' # see the Equation base class for a list of fitting targets
equation.ConvertTextToData(equation.exampleData) # Equations have ASCII text data for testing and examples

equation.Initialize() # now that the equation has data, set up the cache



# if you use a linear equation and a fitting target of 'SSQABS' the fit will be linear and these starting parameters will be ignored
equation.SetEstimatedCoefficientArray([-10, -7, -0.2, 0.2, 8, -.01]) # Initial Starting Parameters

# You can still use the genetic algorithm parameter search in case your starting parameters might be near a local error minimum
# Both the genetic algorithm parameter estimates and the above parameter estimates will be tested and the best result returned
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
