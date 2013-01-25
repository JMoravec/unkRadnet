#! /usr/bin/python
#    Version info: $Id: FitAllEquations2D.py 128 2009-12-03 17:58:01Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
from __future__ import generators
import sys, os, inspect, copy
import multiprocessing
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


# Standard lowest sum-of-squared errors
fittingTarget = 'SSQABS'


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
        t8 = equation.extendedName

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


def IterativelyFitData(modulus, modulusOffset):

    equationsProcessed = 0

    # this example yields a sorted output list to inspect after completion
    resultList = []

    # we are using the same data set repeatedly, so create a cache external to the equations
    externalCacheDict = {}

    for submodule in inspect.getmembers(pythonequations.Equations2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    extendedNameList = pythonequations.EquationBaseClasses.Equation.ExtendedFormsDict.keys()
                    extendedNameList.sort()
                    for extendedName in extendedNameList:
                
                        try:
                            equation = equationClass[1](extendedName)
                        except:
                            continue
                                            
                        if equation.splineFlag or equation.userDefinedFunctionFlag:
                            continue
                        
                        if 0 == ((equationsProcessed + modulusOffset) % modulus):
                            print 'Fitting', equation.name, str(equation.dimensionality) + "D"

                        equation.cacheDict = externalCacheDict # reuse the cache
                        equation.fittingTarget = fittingTarget # see the Equation base class for a list of fitting targets

                        # we only need to convert text to data once and before the first
                        # equation is fitted, the cache is empty - use this as a flag
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
                            equation.IndependentData1ContainsNegativeFlag = IndependentData1ContainsNegativeFlag
                            equation.IndependentData1ContainsPositiveFlag = IndependentData1ContainsPositiveFlag
                            equation.IndependentData2ContainsZeroFlag = IndependentData2ContainsZeroFlag
                            equation.IndependentData2ContainsNegativeFlag = IndependentData2ContainsNegativeFlag
                            equation.IndependentData2ContainsPositiveFlag = IndependentData2ContainsPositiveFlag
                            equation.IndependentDataArray = IndependentDataArray
                            equation.DependentDataArray = DependentDataArray

                        # non-polynomial, non-polyfunctional equations here
                        if equation.polynomialFlag == 0 and equation.polyfunctionalFlag == 0 and equation.polyrationalFlag == 0:
                            if 0 == ((equationsProcessed + modulusOffset) % modulus):
                                SetParametersAndFit(equation, resultList)
                            equationsProcessed += 1

                        # polynomials are iterated from zero to some maximum order
                        if equation.polynomialFlag == 1:
                            equationCount = 0
                            for xPolynomialOrder in range(7): # arbitrary choice of maximum 6th order for this example
                                equation.xPolynomialOrder = xPolynomialOrder
                                if 0 == ((equationsProcessed + modulusOffset) % modulus):
                                    SetParametersAndFit(equation, resultList)
                                    equationCount += 1
                                    if (equationCount % 5) == 0:
                                        print '    ', equationCount
                                equationsProcessed += 1
                            print '    ', equationCount, 'equations fitted'

                        # polyfunctionals are combinations of individual functions with some maximum number of combinations
                        if equation.polyfunctionalFlag == 1:
                            equationCount = 0
                            maxCoeffs = 5 # arbitrary choice of maximum functions in a polyfunctional for this example
                            functionList = [] # make a list of function indices
                            for i in range(len(equation.EquationListForPolyfunctional)):
                                functionList.append(i)

                            for coeffCount in range(1, maxCoeffs+1):
                                xComboList = UniqueCombinations(functionList, coeffCount)
                                for k in xComboList:
                                    equation.Polyfun2DFlags = k
                                    if 0 == ((equationsProcessed + modulusOffset) % modulus):
                                        SetParametersAndFit(equation, resultList)
                                        equationCount += 1
                                        if (equationCount % 1000) == 0 and equationCount > 0:
                                            print '    ', equationCount, '...'
                                    equationsProcessed += 1
                            print '    ', equationCount, 'equations fitted'


                        # polyrationals are combinations of individual functions with some maximum number of combinations
                        if equation.polyrationalFlag == 1:
                            equationCount = 0
                            maxCoeffs = 2 # arbitrary choice of maximum number of numerator or denominator functions in a polyrational for this example
                            functionList = [] # make a list of function indices
                            for i in range(len(equation.EquationListForPolyrational)):
                                functionList.append(i)

                            for numeratorCoeffCount in range(1, maxCoeffs+1):
                                numeratorComboList = UniqueCombinations(functionList, numeratorCoeffCount)
                                for numeratorCombo in numeratorComboList:
                                    equation.Polyrat2DNumeratorFlags = numeratorCombo
                                    for denominatorCoeffCount in range(1, maxCoeffs+1):
                                        denominatorComboList = UniqueCombinations2(functionList, denominatorCoeffCount)
                                        for denominatorCombo in denominatorComboList:
                                            equation.Polyrat2DDenominatorFlags = denominatorCombo
                                            if 0 == ((equationsProcessed + modulusOffset) % modulus):
                                                SetParametersAndFit(equation, resultList)
                                                equationCount += 1
                                                if (equationCount % 50) == 0 and equationCount > 0:
                                                    print '    ', equationCount, ',', equation.Polyrat2DNumeratorFlags, equation.Polyrat2DDenominatorFlags
                                            equationsProcessed += 1
                                                
                            print '    ', equationCount, 'equations fitted'
    return resultList


if __name__ == "__main__":

    allResults = []


    ##############################################
    # Parallel region begins
    ##############################################
    number_of_cpu_cores = multiprocessing.cpu_count() # hit the server hard using all CPU cores at the same time
    pool = multiprocessing.Pool(processes=number_of_cpu_cores)
    poolItems = []
    for i in range(number_of_cpu_cores):
        poolItems.append(pool.apply_async(IterativelyFitData, (number_of_cpu_cores, i,))) # divides the equations among the processes
    pool.close()
    pool.join()
    for i in range(number_of_cpu_cores):
        allResults += poolItems[i].get()
    poolItems = None # done with the items in the parallel process pool
    pool = None # done with the parallel process pool
    ##############################################
    # Parallel region ends
    ##############################################


    # the individual elements in resultList were assigned in SetParametersAndFit()
    print
    print 'done - fitted', len(allResults), 'equations, sorting result set...'

    # Sort the result list by fitting target value, see SetParametersAndFit() for assignment
    allResults.sort(ResultListSortFunction) # currently requires the 3rd element in each result to be fitting target

    # now find and instantiate the "best fit" equation based on the name stored in the result list
    found = 0 # flag to stop looking for the equation we are after here
    for submodule in inspect.getmembers(pythonequations.Equations2D):
        if inspect.ismodule(submodule[1]) and found == 0:
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]) and found == 0:
                        if equationClass[0] == allResults[0][0]:
                            equation = equationClass[1](allResults[0][8]) # use extended form name here
                            found = 1

    # assign the allResults values, then initialize the equation
    equation.fittingTarget = fittingTarget
    equation.ConvertTextToData(equation.exampleData)
    equation.xPolynomialOrder = allResults[0][3]
    equation.Polyfun2DFlags = allResults[0][4]
    equation.coefficientArray = allResults[0][5]
    equation.Polyrat2DNumeratorFlags = allResults[0][6]
    equation.Polyrat2DDenominatorFlags = allResults[0][7]

    equation.Initialize() # coefficients and flags are set, initialize to these known values

    equation.CalculateErrors()

    # while allResults[0] may be the lowest fitting target value,
    # it requires further evaluation to determine if it is the best
    # for your needs.  For example, it may interpolate badly.
    print '\"Best fit\" was', equation.name, str(equation.dimensionality) + "D"

    if allResults[0][3] != 0:
        print 'Polynomial order', allResults[0][3]
    if allResults[0][4] != []:
        print 'Polyfunctional flags', allResults[0][4]
    if equation.Polyrat2DNumeratorFlags != []: # is this a polyrational?
        print 'Polyrational flags, numerator:', allResults[0][6], '  denominator:', allResults[0][7],
        if len(equation.coefficientArray) == 1 + len(equation.Polyrat2DNumeratorFlags) + len(equation.Polyrat2DDenominatorFlags):
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
