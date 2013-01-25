#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: Sigmoidal.py 274 2010-09-29 13:16:14Z zunzun.com $

import pythonequations, pythonequations.EquationBaseClasses, pythonequations.ExtraCodeForEquationBaseClasses
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


class AndreaPrunottoSigmoidA3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = False
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name ="Andrea Prunotto Sigmoid A"
    _HTML = "z = a0 + (a1 / (1.0 + exp(a2 * (x + a3 + a4 * y + a5 * x * y))))"
    coefficientDesignatorTuple = ("a0", "a1", "a2", "a3", "a4", "a5")
    function_cpp_code = 'temp = coeff[0] + (coeff[1] / (1.0 + exp(coeff[2] * (_id[_cwo[0]+i] + coeff[3] + coeff[4] * _id[_cwo[1]+i] + coeff[5] * _id[_cwo[2]+i]))));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_XY(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a0 + (a1 / (1.0 + exp(a2 * (x_in + a3 + a4 * y_in + a5 * x_in * y_in))));\n"
        return s



class AndreaPrunottoSigmoidB3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = False
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name ="Andrea Prunotto Sigmoid B"
    _HTML = "z = a0 + (a1 / (1.0 + exp(a2 * (x * a3 + a4 * y + a5 * x * y))))"
    coefficientDesignatorTuple = ("a0", "a1", "a2", "a3", "a4", "a5")
    function_cpp_code = 'temp = coeff[0] + (coeff[1] / (1.0 + exp(coeff[2] * (_id[_cwo[0]+i] * coeff[3] + coeff[4] * _id[_cwo[1]+i] + coeff[5] * _id[_cwo[2]+i]))));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_XY(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a0 + (a1 / (1.0 + exp(a2 * (x_in * a3 + a4 * y_in + a5 * x_in * y_in))));\n"
        return s



class Sigmoid3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name ="Sigmoid"
    _HTML = "z = a / ((1.0 + exp(b - cx)) * (1.0 + exp(d - fy)))"
    coefficientDesignatorTuple = ("a", "b", "c", "d", 'f')
    function_cpp_code = 'temp = coeff[0] / ((1.0 + exp(coeff[1] - coeff[2] * _id[_cwo[2]+i])) * (1.0 + exp(coeff[3] - coeff[4] * _id[_cwo[4]+i])));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a / ((1.0 + exp(b - c * x_in)) * (1.0 + exp(d - f * y_in)));\n"
        return s



class FraserSmithSigmoid3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name ="Fraser Smith Sigmoid"
    _HTML = "z = 1.0 / ((1.0 + exp(a - bx)) * (1.0 + e(c - dy)))"
    coefficientDesignatorTuple = ("a", "b", "c", "d")
    function_cpp_code = 'temp = 1.0 / ((1.0 + exp(coeff[0] - coeff[1] * _id[_cwo[1]+i])) * (1.0 + exp(coeff[2] - coeff[3] * _id[_cwo[3]+i])));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / ((1.0 + exp(a - b * x_in)) * (1.0 + exp(c - d * y_in)));\n"
        return s
