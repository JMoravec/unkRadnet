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
#    Version info: $Id: ExtendedVersionHandler_LinearDecay.py 5 2012-01-22 10:17:35Z zunzun.com@gmail.com $

import pyeq2
import IExtendedVersionHandler


class ExtendedVersionHandler_LinearDecay(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        x_or_xy = 'xy'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / ' + x_or_xy
        else:
            try:
                cd = inModel.GetCoefficientDesignators()
                return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / (' + inModel.listOfAdditionalCoefficientDesignators[len(cd)] + ' * ' + x_or_xy + ')'
            except:
                return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / (' + x_or_xy + ')'


    def AssembleDisplayName(self, inModel):
        return inModel._baseName + ' With Linear Decay'


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__ + "_LinearDecay"


    def AssembleCoefficientDesignators(self, inModel):
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._coefficientDesignators
        else:
            return inModel._coefficientDesignators + [inModel.listOfAdditionalCoefficientDesignators[len(inModel._coefficientDesignators)]]


    def AssembleOutputSourceCodeCPP(self, inModel):
        x_or_xy = 'x_in * y_in'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x_in'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel.SpecificCodeCPP() + "temp = temp / (" + x_or_xy + ");\n"
        else:
            cd = inModel.GetCoefficientDesignators()
            return inModel.SpecificCodeCPP() + "temp = temp / ("  + cd[len(cd)-1] + ' * ' + x_or_xy + ");\n"
        

    # overridden from abstract parent class
    def ShouldDataBeRejected(self, inModel):
        
        if inModel.dataCache.independentData1ContainsZeroFlag == True: # cannot divide by zero
            return True
        if inModel.dataCache.independentData2ContainsZeroFlag == True: # cannot divide by zero
            return True
        
        if (inModel.independentData1CannotContainPositiveFlag == True) and (inModel.dataCache.independentData1ContainsPositiveFlag == True):
            return True
        if (inModel.independentData2CannotContainPositiveFlag == True) and (inModel.dataCache.independentData2ContainsPositiveFlag == True):
            return True
        if (inModel.independentData1CannotContainNegativeFlag == True) and (inModel.dataCache.independentData1ContainsNegativeFlag == True):
            return True
        if (inModel.independentData2CannotContainNegativeFlag == True) and (inModel.dataCache.independentData2ContainsNegativeFlag == True):
            return True
        return False


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        if inModel.GetDimensionality() == 2:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return inBaseModelCalculation / inDataCacheDictionary['X']
            else:
                return inBaseModelCalculation / (inCoeffs[len(inCoeffs)-1] * inDataCacheDictionary['X'])
        else:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return inBaseModelCalculation / inDataCacheDictionary['XY']
            else:
                return inBaseModelCalculation / (inCoeffs[len(inCoeffs)-1] * inDataCacheDictionary['XY'])
