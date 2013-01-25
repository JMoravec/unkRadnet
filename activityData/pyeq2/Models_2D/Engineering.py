#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2012 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: Engineering.py 1 2012-01-07 22:20:43Z zunzun.com@gmail.com $

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them


import pyeq2.Model_2D_BaseClass


class DispersionOptical(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Dispersion Optical"
    _HTML = 'n<sup>2</sup>(x) = A1 + A2*x<sup>2</sup> + A3/x<sup>2</sup> + A4/x<sup>4</sup>'
    _leftSideHTML = 'n<sup>2</sup>(x)'
    _coefficientDesignators = ['A1', 'A2', 'A3', 'A4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A1 = inCoeffs[0]
        A2 = inCoeffs[1]
        A3 = inCoeffs[2]
        A4 = inCoeffs[3]

        try:
            temp = A1 + (A2 * x_PowX2) + (A3 / x_PowX2) + (A4 / x_PowX4)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A1 + (A2 * x_in * x_in) + (A3 / (x_in * x_in)) + (A4 / (x_in * x_in * x_in * x_in));\n"
        return s



class DispersionOpticalSqrt(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Dispersion Optical Square Root"
    _HTML = 'n = (A1 + A2*x<sup>2</sup> + A3/x<sup>2</sup> + A4/x<sup>4</sup>)<sup>0.5</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A1', 'A2', 'A3', 'A4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A1 = inCoeffs[0]
        A2 = inCoeffs[1]
        A3 = inCoeffs[2]
        A4 = inCoeffs[3]

        try:
            temp = numpy.power(A1 + (A2 * x_PowX2) + (A3 / x_PowX2) + (A4 / x_PowX4), 0.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = pow(A1 + (A2 * x_in * x_in) + (A3 / (x_in * x_in)) + (A4 / (x_in * x_in * x_in * x_in)), 0.5);\n"
        return s



class Extended_Steinhart_Hart(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extended Steinhart-Hart"
    _HTML = '1/T = A + Bln(R) + C(ln(R))<sup>2</sup> + D(ln(R))<sup>3</sup>'
    _leftSideHTML = '1/T'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B*x_LogX + C*numpy.power(x_LogX, 2.0) + D*numpy.power(x_LogX, 3.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*log(x_in) + C*pow(log(x_in), 2.0) + D*pow(log(x_in), 3.0);\n"
        return s



class Ramberg_Osgood(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Ramberg-Osgood"
    _HTML = 'y = (Stress / Youngs_Modulus) + (Stress/K)<sup>(1.0/n)</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['Youngs_Modulus', 'K', 'n']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        Youngs_Modulus = inCoeffs[0]
        K = inCoeffs[1]
        n = inCoeffs[2]

        try:
            temp = (x_in / Youngs_Modulus) +  numpy.power(x_in / K, 1.0 / n)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (x_in / Youngs_Modulus) +  pow(x_in / K, 1.0 / n);\n"
        return s



class Reciprocal_Extended_Steinhart_Hart(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Reciprocal Extended Steinhart-Hart"
    _HTML = 'T = 1.0 / (A + Bln(R) + C(ln(R))<sup>2</sup> + D(ln(R))<sup>3</sup>)'
    _leftSideHTML = 'T'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = 1.0 / (A + B*x_LogX + C*numpy.power(x_LogX, 2.0) + D*numpy.power(x_LogX, 3.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (A + B*log(x_in) + C*pow(log(x_in), 2.0) + D*pow(log(x_in), 3.0));\n"
        return s



class Reciprocal_Steinhart_Hart(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Reciprocal Steinhart-Hart"
    _HTML = 'T = 1.0 / (A + Bln(R) + C(ln(R))<sup>3</sup>)'
    _leftSideHTML = 'T'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        PowLogX_3 = inDataCacheDictionary['PowLogX_3.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = 1.0 / (A + B*LogX + C*PowLogX_3)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (A + B*log(x_in) + C*pow(log(x_in), 3.0));\n"
        return s



class SellmeierOptical(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sellmeier Optical"
    _HTML = 'n<sup>2</sup>(x) = 1 + (B1 x<sup>2</sup>)/(x<sup>2</sup>-C1) + (B2 x<sup>2</sup>)/(x<sup>2</sup>-C2) + (B3 x<sup>2</sup>)/(x<sup>2</sup>-C3)'
    _leftSideHTML = 'n<sup>2</sup>(x)'
    _coefficientDesignators = ['B1', 'C1', 'B2', 'C2', 'B3', 'C3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        B1 = inCoeffs[0]
        C1 = inCoeffs[1]
        B2 = inCoeffs[2]
        C2 = inCoeffs[3]
        B3 = inCoeffs[4]
        C3 = inCoeffs[5]

        try:
            temp = 1.0 + ((B1 * x_PowX2)/(x_PowX2 - C1)) + ((B2 * x_PowX2)/(x_PowX2 - C2)) + ((B3 * x_PowX2)/(x_PowX2 - C3))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + ((B1 * x_in * x_in)/(x_in * x_in - C1)) + ((B2 * x_in * x_in)/(x_in * x_in - C2)) + ((B3 * x_in * x_in)/(x_in * x_in - C3));\n"
        return s



class SellmeierOpticalSqrt(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sellmeier Optical Square Root"
    _HTML = 'n = (1 + (B1 x<sup>2</sup>)/(x<sup>2</sup>-C1) + (B2 x<sup>2</sup>)/(x<sup>2</sup>-C2) + (B3 x<sup>2</sup>)/(x<sup>2</sup>-C3))<sup>0.5</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['B1', 'C1', 'B2', 'C2', 'B3', 'C3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        B1 = inCoeffs[0]
        C1 = inCoeffs[1]
        B2 = inCoeffs[2]
        C2 = inCoeffs[3]
        B3 = inCoeffs[4]
        C3 = inCoeffs[5]

        try:
            temp = numpy.power(1.0 + ((B1 * x_PowX2)/(x_PowX2 - C1)) + ((B2 * x_PowX2)/(x_PowX2 - C2)) + ((B3 * x_PowX2)/(x_PowX2 - C3)), 0.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = pow(1.0 + ((B1 * x_in * x_in)/(x_in * x_in - C1)) + ((B2 * x_in * x_in)/(x_in * x_in - C2)) + ((B3 * x_in * x_in)/(x_in * x_in - C3)), 0.5);\n"
        return s



class Steinhart_Hart(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Steinhart-Hart"
    _HTML = '1/T = A + Bln(R) + C(ln(R))<sup>3</sup>'
    _leftSideHTML = '1/T'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B*x_LogX + C*numpy.power(x_LogX, 3.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*log(x_in) + C*pow(log(x_in), 3.0);\n"
        return s



class VanDeemterChromatography(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "VanDeemter Chromatography"
    _HTML = 'y = a + b/x + cx'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[-1.0]), [-1.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX_Neg1 = inDataCacheDictionary['PowX_-1.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * x_PowX_Neg1 + c * x_in
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b / x_in + c * x_in;\n"
        return s



