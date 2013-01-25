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
#    Version info: $Id: IExtendedVersionHandler.py 4 2012-01-22 09:34:22Z zunzun.com@gmail.com $

import pyeq2
import abc, inspect


class IExtendedVersionHandler(object):

    @abc.abstractmethod
    def AssembleDisplayHTML(self):
        raise NotImplementedError, 'The IExtendedVersionHandler abstract base class does not implement ' + inspect.stack()[0][3]

    @abc.abstractmethod
    def AssembleDisplayName(self, inModel):
        raise NotImplementedError, 'The IExtendedVersionHandler abstract base class does not implement ' + inspect.stack()[0][3]

    @abc.abstractmethod
    def AssembleCoefficientDesignators(self):
        raise NotImplementedError, 'The IExtendedVersionHandler abstract base class does not implement ' + inspect.stack()[0][3]

    @abc.abstractmethod
    def AssembleOutputSourceCodeCPP(self, IModel):
        raise NotImplementedError, 'The IExtendedVersionHandler abstract base class does not implement ' + inspect.stack()[0][3]


    def ShouldDataBeRejected(self, inModel):
        if (inModel.independentData1CannotContainZeroFlag == True) and (inModel.dataCache.independentData1ContainsZeroFlag == True):
            return True
        if (inModel.independentData2CannotContainZeroFlag == True) and (inModel.dataCache.independentData2ContainsZeroFlag == True):
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


    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        foundX = False
        foundXY = False
        for i in inDataCacheFunctions: # if these are already in the cache, we don't need to add them again
            if i[0] == 'X' and inModel.GetDimensionality() == 2:
                foundX = True
            if i[0] == 'XY' and inModel.GetDimensionality() == 3:
                foundXY = True
                
        if inModel.GetDimensionality() == 2:
            if not foundX:
                return inDataCacheFunctions + \
                       [[pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []]]
        else:
            if not foundXY:
                return inDataCacheFunctions + \
                       [[pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []]]
        return inDataCacheFunctions


    @abc.abstractmethod
    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        raise NotImplementedError, 'The IExtendedVersionHandler abstract base class does not implement ' + inspect.stack()[0][3]


    def CanLinearSolverBeUsedForSSQABS(self, inModelFlag):
        return False
