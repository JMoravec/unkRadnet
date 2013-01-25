#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: Polyfunctional.py 274 2010-09-29 13:16:14Z zunzun.com $y)

import pythonequations, pythonequations.EquationBaseClasses, pythonequations.ExtraCodeForEquationBaseClasses, pythonequations.EquationsForPolyfunctionals
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


class Polyfunctional2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = False
    RequiresAutoGeneratedOffsetForm = False
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "User-Selectable Polyfunctional"
    _HTML = "y = user-selectable function"
    coefficientDesignatorTuple = ()
    polyfunctionalFlag = 1
    LinearSSQSolverFlag = 1
    EquationListForPolyfunctional = pythonequations.EquationsForPolyfunctionals.GenerateListForPolyfunctionals('x', 'x_in')
    Polyfun2DEqList = pythonequations.EquationsForPolyfunctionals.GenerateListForPolyfunctionals('unused', 'unused')
    function_cpp_code = 'temp = 0.0;\nfor (int k=0; k<_nc; k++)\n\ttemp += coeff[k] * _id[_cwo[k]+i];'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        for i in range(1, len(self.EquationListForPolyfunctional)):
            if i in self.Polyfun2DFlags:
                self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Polyfunctional2D(NameOrValueFlag=1, args=i), i])
        if 0 in self.Polyfun2DFlags:
            self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Polyfunctional2D(NameOrValueFlag=1, args=0), 0])


    def SpecificCodeCPP(self):
        s = ""
        count = 0
        for xindex in range(1, len(self.EquationListForPolyfunctional)):
            if xindex in self.Polyfun2DFlags:
                s += "\ttemp += " + self.coefficientDesignatorTuple[count] + " * " + self.EquationListForPolyfunctional[xindex].CPP + ";\n"
                count += 1
        if 0 in self.Polyfun2DFlags:
            s += "\ttemp += " + self.coefficientDesignatorTuple[count] + ";\n"
        return s


    def Initialize(self):
        self.coefficientDesignatorTuple = ()
        self.additionalDesignatorList = []

        if len(self.Polyfun2DFlags) == 0:
            self._HTML = "y = user-selectable function"
            return

        for i in range(len(self.Polyfun2DFlags)-1):
            self.coefficientDesignatorTuple += (pythonequations.EquationBaseClasses.Equation.ascii[i]),
        if 0 in self.Polyfun2DFlags:
            self.coefficientDesignatorTuple += ('Offset'),
        else:
            self.coefficientDesignatorTuple += (pythonequations.EquationBaseClasses.Equation.ascii[len(self.Polyfun2DFlags)-1]),

        self._HTML = "</B><B>y = " # turn off any preceding bolding
        count = 0
        for xindex in range(1, len(self.EquationListForPolyfunctional)):
            if xindex in self.Polyfun2DFlags:
                self._HTML += pythonequations.EquationBaseClasses.Equation.ascii[count] + "(</B>&nbsp;" + self.EquationListForPolyfunctional[xindex]._HTML + "&nbsp;<B>) "
                count += 1
                if len(self.Polyfun2DFlags) > count:
                    self._HTML += "+ "
        if 0 in self.Polyfun2DFlags:
                self._HTML += "Offset"

        self._HTML += '</B>'

        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        self.CannotAcceptDataWithZeroX = False
        self.CannotAcceptDataWithPositiveX = False
        self.CannotAcceptDataWithNegativeX = False
        for i in range(len(self.coefficientDesignatorTuple)):
            self.CannotAcceptDataWithZeroX |= self.EquationListForPolyfunctional[self.Polyfun2DFlags[i]].CannotAcceptDataWithZeroX
            self.CannotAcceptDataWithPositiveX |= self.EquationListForPolyfunctional[self.Polyfun2DFlags[i]].CannotAcceptDataWithPositiveX
            self.CannotAcceptDataWithNegativeX |= self.EquationListForPolyfunctional[self.Polyfun2DFlags[i]].CannotAcceptDataWithNegativeX