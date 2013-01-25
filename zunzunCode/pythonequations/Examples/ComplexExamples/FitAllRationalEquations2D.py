#! /usr/bin/python
#    Version info: $Id: FitAllEquations2D.py 118 2009-11-20 11:49:58Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
from __future__ import generators
import sys, os, inspect, copy;
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations



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

        t0 = copy.deepcopy(equation.__class__.__name__)
        t1 = copy.deepcopy(equation.name)
        t2 = copy.deepcopy(equation.CalculateFittingTarget(equation.coefficientArray))

        if t2 > 1.0E290: #skip equations yielding very large errors
            return

        t3 = copy.deepcopy(equation.xPolynomialOrder)
        t4 = copy.deepcopy(equation.Polyfun2DFlags)
        t5 = copy.deepcopy(equation.coefficientArray)
        t6 = copy.deepcopy(equation.Polyrat2DNumeratorFlags)
        t7 = copy.deepcopy(equation.Polyrat2DDenominatorFlags)
        t8 = copy.deepcopy(equation.extendedName)

        resultList += ([t0,t1,t2,t3,t4,t5,t6,t7,t8]),

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

# helper function
def UniqueCombinations2(items2, n2):
    if n2==0:
        yield []
    else:
        for i2 in xrange(len(items2)):
            for cc2 in UniqueCombinations2(items2[i2+1:],n2-1):
                yield [items2[i2]]+cc2



# this example yields a sorted output list to inspect after completion
resultList = []

# Standard lowest sum-of-squared errors
fittingTarget = 'SSQABS'

# we are using the same data set repeatedly, so create a cache external to the equations
externalCacheDict = {}

print 'Fitting User-Selectable Rational 2D'

# polyfunctionals are combinations of individual functions with some maximum number of combinations
maxCoeffs = 2 # arbitrary choice of maximum number of numerator or denominator functions in a polyrational for this example
functionList = [] # make a list of function indices
for i in range(len(pythonequations.Equations2D.Rational.Polyrational2D.EquationListForPolyrational)):
    functionList.append(i)

equationCount = 0
for numeratorCoeffCount in range(1, maxCoeffs+1):
    numeratorComboList = UniqueCombinations(functionList, numeratorCoeffCount)
    for numeratorCombo in numeratorComboList:
        for denominatorCoeffCount in range(1, maxCoeffs+1):
            denominatorComboList = UniqueCombinations2(functionList, denominatorCoeffCount)
            for denominatorCombo in denominatorComboList:
                for extendedName in ['', 'Offset']:
               
                    equation = pythonequations.Equations2D.Rational.Polyrational2D(extendedName)
                    equation.cacheDict = externalCacheDict # reuse the cache
                    equation.fittingTarget = fittingTarget # see the Equation base class for a list of fitting targets
                    if externalCacheDict == {}:
                        equation.ConvertTextToData(equation.exampleData) # Equations have ASCII text data for testing and examples
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
                    equation.Polyrat2DNumeratorFlags = numeratorCombo
                    equation.Polyrat2DDenominatorFlags = denominatorCombo
                    SetParametersAndFit(equation, resultList)
                                
                equationCount += 1
                if (equationCount % 50) == 0:
                    # the "time 2" is for offset versions
                    print '    ', equationCount * 2, ',', equation.Polyrat2DNumeratorFlags, equation.Polyrat2DDenominatorFlags


# the individual elements in resultList were assigned in SetParametersAndFit()
print
print 'done - fitted', len(resultList), 'equations, sorting result set...'

# Sort the result list by fitting target value, see SetParametersAndFit() for assignment
resultList.sort(ResultListSortFunction) # currently requires the 3rd element in each result to be fitting target

equation = pythonequations.Equations2D.Rational.Polyrational2D(resultList[0][8])

# assign the resultList values, then initialize the equation
equation.fittingTarget = fittingTarget
equation.ConvertTextToData(equation.exampleData)
equation.xPolynomialOrder = resultList[0][3]
equation.Polyfun2DFlags = resultList[0][4]
equation.coefficientArray = resultList[0][5]
equation.Polyrat2DNumeratorFlags = resultList[0][6]
equation.Polyrat2DDenominatorFlags = resultList[0][7]

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
if equation.Polyrat2DNumeratorFlags != []: # is this a polyrational?
    print 'Polyrational flags, numerator:', resultList[0][6], '  denominator:', resultList[0][7],
    if resultList[0][8] == "Offset":
        print '  plus offset'
    print


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
