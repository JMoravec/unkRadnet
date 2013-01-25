#! /usr/bin/python
#    Version info: $Id: FitAllEquations2D.py 75 2009-08-04 19:32:09Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
from __future__ import generators
import sys, os, inspect;
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


weightedTextData = '''

X   Y     Weight

1   1     1
2   2.001 1
3   3     1
4   6     0.15
5   5.5   1
6   7     1
7   8.5   1
9   9     This data point has no weight and is completey ignored

'''

# helper function
def SetParametersAndFit(equation, resultList):
    try:
        equation.Initialize()

        # check for number of coefficients > number of data points to be fitted
        if len(equation.coefficientDesignatorTuple) > len(equation.IndependentDataArray[0]):
            return

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if equation.ShouldDataBeRejectedByThisEquation():
            return

        equation.SetGAParametersAndGuessInitialCoefficientsIfNeeded()
        equation.FitToCacheData()

        t0 = equation.__class__.__name__
        t1 = equation.name
        t2 = equation.CalculateFittingTarget(equation.coefficientArray)

        if t2 > 1.0E290: #skip equations yielding very large errors
            return

        t3 = equation.xPolynomialOrder
        t4 = equation.Polyfun2DFlags
        t5 = equation.coefficientArray
        t6 = equation.extendedName

        resultList += ([t0,t1,t2,t3,t4,t5,t6]),

    except:
        print "Exception in " + equation.name + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n'


# helper function
def ResultListSortFunction(a, b):
    if a[2] < b[2]:
        return -1
    if a[2] > b[2]:
        return 1
    return 0


# helper function
def UniqueCombinations(items, n):
    if n==0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in UniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc




# this example yields a sorted output list to inspect after completion
resultList = []

# Standard lowest sum-of-squared errors
fittingTarget = 'SSQABS'

# we are using the same data set repeatedly, so create a cache external to the equations
externalCacheDict = {}

for submodule in inspect.getmembers(pythonequations.Equations2D):
    if inspect.ismodule(submodule[1]):
        if submodule[0] != 'BioScience':
            continue
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                for extendedName in ['', 'Offset']: # do use offset versions
                
                    try:
                        # passing no parameter here means no extended form, however in this example we do want offset forms
                        equation = equationClass[1](extendedName)
                    except:
                        continue
                                    
                    print 'Fitting', equation.name, str(equation.dimensionality) + "D"

                    equation.cacheDict = externalCacheDict # reuse the cache
                    equation.fittingTarget = fittingTarget # see the Equation base class for a list of fitting targets

                    # we only need to convert text to data once and before the first
                    # equation is fitted, the cache is empty - use this as a flag
                    if externalCacheDict == {}:
                        # Note the extra parameter here, this turns on weighted fitting.
                        # All data points will require a weight here, unweighted data points are ignored
                        equation.ConvertTextToData(weightedTextData, 1)
                        DependentDataContainsZeroFlag = equation.DependentDataContainsZeroFlag
                        IndependentData1ContainsZeroFlag = equation.IndependentData1ContainsZeroFlag
                        IndependentData1ContainsPositiveFlag = equation.IndependentData1ContainsPositiveFlag
                        IndependentData1ContainsNegativeFlag = equation.IndependentData1ContainsNegativeFlag
                        IndependentData2ContainsZeroFlag = equation.IndependentData2ContainsZeroFlag
                        IndependentData2ContainsPositiveFlag = equation.IndependentData2ContainsPositiveFlag
                        IndependentData2ContainsNegativeFlag = equation.IndependentData2ContainsNegativeFlag
                        IndependentDataArray = equation.IndependentDataArray
                        DependentDataArray = equation.DependentDataArray
                    else:
                        equation.DependentDataContainsZeroFlag = DependentDataContainsZeroFlag
                        equation.IndependentData1ContainsZeroFlag = IndependentData1ContainsZeroFlag
                        equation.IndependentData1ContainsPositiveFlag = IndependentData1ContainsPositiveFlag
                        equation.IndependentData1ContainsNegativeFlag = IndependentData1ContainsNegativeFlag
                        equation.IndependentData2ContainsZeroFlag = IndependentData2ContainsZeroFlag
                        equation.IndependentData2ContainsPositiveFlag = IndependentData2ContainsPositiveFlag
                        equation.IndependentData2ContainsNegativeFlag = IndependentData2ContainsNegativeFlag
                        equation.IndependentDataArray = IndependentDataArray
                        equation.DependentDataArray = DependentDataArray

                    SetParametersAndFit(equation, resultList)


# the individual elements in resultList were assigned in SetParametersAndFit()
print 'done - fitted', len(resultList), 'equations, sorting result set...'

# Sort the result list by fitting target value, see SetParametersAndFit() for assignment
resultList.sort(ResultListSortFunction) # currently requires the 3rd element in each result to be fitting target

# now find and instantiate the "best fit" equation based on the name stored in the result list
found = 0 # flag to stop looking for the equation we are after here
for submodule in inspect.getmembers(pythonequations.Equations2D):
    if inspect.ismodule(submodule[1]) and found == 0:
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]) and found == 0:
                    if equationClass[0] == resultList[0][0]:
                        equation = equationClass[1](resultList[0][6]) # use extended form name here
                        found = 1

# assign the resultList values, then initialize the equation
equation.fittingTarget = fittingTarget

# Note the extra parameter here, this turns on weighted fitting.
# All data points will require a weight here, unweighted data points are ignored
equation.ConvertTextToData(weightedTextData, 1)

equation.xPolynomialOrder = resultList[0][3]
equation.Polyfun2DFlags = resultList[0][4]
equation.coefficientArray = resultList[0][5]

equation.Initialize() # coefficients and flags are set, initialize to these known values

equation.CalculateErrors()

# while resultList[0] may be the lowest fitting target value,
# it requires further evaluation to determine if it is the best
# for your needs.  For example, it may interpolate badly.
print '\"Best fit\" was', equation.name, str(equation.dimensionality) + "D"

if resultList[0][3] != 0:
    print 'Polynomial order', resultList[0][3]
if resultList[0][4] != []:
    print 'Polyfunctional flags', resultList[0][4]

print 'Fitting target value', equation.fittingTarget + ":", equation.CalculateFittingTarget(equation.coefficientArray)
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
