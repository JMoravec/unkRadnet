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
#    Version info: $Id: ExtendedVersionHandler_Reciprocal.py 1 2012-01-07 22:20:43Z zunzun.com@gmail.com $

import pyeq2
import IExtendedVersionHandler


class ExtendedVersionHandler_Reciprocal(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = 1.0 / ' + inModel._leftSideHTML


    def AssembleDisplayName(self, inModel):
        return 'Reciprocal ' + inModel._baseName


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__ + "_Reciprocal"


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators


    def AssembleOutputSourceCodeCPP(self, inModel):
        return inModel.SpecificCodeCPP() + "temp = 1.0 / temp;\n"


    # overridden from abstract parent class
    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        return 1.0 / inBaseModelCalculation
