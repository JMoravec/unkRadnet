#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: Peak.py 334 2011-11-27 21:22:21Z zunzun.com $

import pythonequations, pythonequations.EquationBaseClasses, pythonequations.ExtraCodeForEquationBaseClasses
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


class Hamilton2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = False
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Hamilton"
    _HTML = "Vb = Gb * (I/mu)<sup>ln(mu/I)/(B*B)</sup> + (Vb<sub>max</sub> * I)/(I + sigma_b)"
    coefficientDesignatorTuple = ('Gb', 'mu', 'B', 'Vbmax', 'sigma_b')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = coeff[0] * pow(_id[_cwo[0]+i] / coeff[1], log(coeff[1] / _id[_cwo[0]+i]) / (coeff[2] * coeff[2])) + (coeff[3] * _id[_cwo[0]+i]) / (_id[_cwo[0]+i] + coeff[4]);'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def VerifyCoefficientsAreWithinBounds(self, in_coeffArray):
        # see Equation base class definition of this method
        return (self.lowerCoefficientBoundsArray[0] < in_coeffArray[0] < self.upperCoefficientBoundsArray[0]) and \
            (self.lowerCoefficientBoundsArray[1] < in_coeffArray[1] < self.upperCoefficientBoundsArray[1]) and \
            (self.lowerCoefficientBoundsArray[2] < in_coeffArray[2] < self.upperCoefficientBoundsArray[2]) and \
            (self.lowerCoefficientBoundsArray[3] < in_coeffArray[3] < self.upperCoefficientBoundsArray[3]) and \
            (self.lowerCoefficientBoundsArray[4] < in_coeffArray[4] < self.upperCoefficientBoundsArray[4])

    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[0] = 0.0
            self.lowerCoefficientBoundsArray[1] = 0.0
            self.lowerCoefficientBoundsArray[2] = 0.0
            self.lowerCoefficientBoundsArray[3] = 0.0
            self.lowerCoefficientBoundsArray[4] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = Gb * pow(x_in / mu, log(mu/x_in)/(B*B)) + (Vbmax * x_in) / (x_in + sigma_b);\n"
        return s



class LorentzianPeakA2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak A"
    _HTML = "y = 1.0 / (1.0 + (x-a)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a")
    function_cpp_code = 'temp = 1.0 / (1.0 + pow(_id[_cwo[0]+i] - coeff[0], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow(x_in-a, 2.0));\n"
        return s



class LorentzianModifiedPeakA2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak A"
    _HTML = "y = 1.0 / (1.0 + (x-a)<SUP>b</SUP>)"
    coefficientDesignatorTuple = ("a", 'b')
    function_cpp_code = 'temp = 1.0 / (1.0 + pow(_id[_cwo[0]+i] - coeff[0], coeff[1]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow(x_in-a, 2.0));\n"
        return s



class LorentzianPeakB2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak B"
    _HTML = "y = 1.0 / (a + (x-b)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = 1.0 / (coeff[0] + pow(_id[_cwo[0]+i] - coeff[1], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow(x_in-b, 2.0));\n"
        return s



class LorentzianModifiedPeakB2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak B"
    _HTML = "y = 1.0 / (a + (x-b)<SUP>c</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = 1.0 / (coeff[0] + pow(_id[_cwo[0]+i] - coeff[1], coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow(x_in-b, c));\n"
        return s



class LorentzianPeakC2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak C"
    _HTML = "y = a / (b + (x-c)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] / (coeff[1] + pow(_id[_cwo[0]+i] - coeff[2], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow(x_in-c, 2.0));\n"
        return s



class LorentzianModifiedPeakC2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak C"
    _HTML = "y = a / (b + (x-c)<SUP>d</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = coeff[0] / (coeff[1] + pow(_id[_cwo[0]+i] - coeff[2], coeff[3]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow(x_in-c, d));\n"
        return s



class LorentzianPeakD2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak D"
    _HTML = "y = 1.0 / (1.0 + ((x-a)/b)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a", 'b')
    function_cpp_code = 'temp = 1.0 / (1.0 + pow((_id[_cwo[0]+i] - coeff[0]) / coeff[1], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow((x_in-a) / b, 2.0));\n"
        return s



class LorentzianModifiedPeakD2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak D"
    _HTML = "y = 1.0 / (1.0 + ((x-a)/b)<SUP>c</SUP>)"
    coefficientDesignatorTuple = ("a", 'b', 'c')
    function_cpp_code = 'temp = 1.0 / (1.0 + pow((_id[_cwo[0]+i] - coeff[0]) / coeff[1], coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow((x_in-a) / b, c));\n"
        return s



class LorentzianPeakE2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak E"
    _HTML = "y = 1.0 / (a + ((x-b)/c)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = 1.0 / (coeff[0] + pow((_id[_cwo[0]+i] - coeff[1])/coeff[2], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow((x_in-b)/c, 2.0));\n"
        return s



class LorentzianModifiedPeakE2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak E"
    _HTML = "y = 1.0 / (a + ((x-b)/c)<SUP>d</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = 1.0 / (coeff[0] + pow((_id[_cwo[0]+i] - coeff[1])/coeff[2], coeff[3]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow((x_in-b)/c, d));\n"
        return s



class LorentzianPeakF2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Peak F"
    _HTML = "y = a / (b + ((x-c)/d)<SUP>2</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = coeff[0] / (coeff[1] + pow((_id[_cwo[0]+i] - coeff[2]) / coeff[3], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow((x_in-c)/d, 2.0));\n"
        return s



class LorentzianModifiedPeakF2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Lorentzian Modified Peak F"
    _HTML = "y = a / (b + ((x-c)/d)<SUP>f</SUP>)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd', 'f')
    function_cpp_code = 'temp = coeff[0] / (coeff[1] + pow((_id[_cwo[0]+i] - coeff[2]) / coeff[3], coeff[4]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow((x_in-c)/d, f));\n"
        return s



class BoxLucasA2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas A"
    _HTML = "y = a * (1.0 - b<SUP>x</sup>)"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = coeff[0] * (1.0 - pow(coeff[1],  _id[_cwo[0]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - pow(b, x_in));\n"
        return s



class BoxLucasB2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas B"
    _HTML = "y = a * (1.0 - exp(-bx))"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = coeff[0] * (1.0 - exp(-1.0 * coeff[1] * _id[_cwo[0]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - exp(-1.0 * b * x_in));\n"
        return s



class BoxLucasC2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas C"
    _HTML = "y = (a / (a-b)) * (exp(-bx) - exp(-ax))"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = (coeff[0] / (coeff[0] - coeff[1])) * (exp(-1.0 * coeff[1] * _id[_cwo[0]+i]) - exp(-1.0 * coeff[0] * _id[_cwo[0]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (a-b)) * (exp(-1.0 * b *x_in) - exp(-1.0 * a * x_in));\n"
        return s



class BoxLucasAShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas A Shifted"
    _HTML = "y = a * (1.0 - b<SUP>x-c</sup>)"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * (1.0 - pow(coeff[1], _id[_cwo[0]+i] - coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - pow(b, x_in - c));\n"
        return s



class BoxLucasBShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas B Shifted"
    _HTML = "y = a * (1.0 - exp(-b(x-c)))"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = coeff[0] * (1.0 - exp(-1.0 * coeff[1] * (_id[_cwo[0]+i] - coeff[2])));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - exp(-1.0 * b * (x_in - c)));\n"
        return s



class BoxLucasCShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Box Lucas C shifted"
    _HTML = "y = (a / (a-b)) * (exp(-b(x-c)) - exp(-a(x-c)))"
    coefficientDesignatorTuple = ("a", "b", 'c')
    function_cpp_code = 'temp = (coeff[0] / (coeff[0] - coeff[1])) * (exp(-1.0 * coeff[1] * (_id[_cwo[0]+i]-coeff[2])) - exp(-1.0 * coeff[0] * (_id[_cwo[0]+i]-coeff[2])));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (a-b)) * (exp(-1.0 * b * (x_in-c)) - exp(-1.0 * a * (x_in-c)));\n"
        return s



class Gaussian2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Gaussian Peak"
    _HTML = "y = a * exp(-0.5 * ((x-b)/c)<sup>2</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c")
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((x_in-b) / c, 2.0));\n"
        return s



class Gaussian_Modified2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Gaussian Peak Modified"
    _HTML = "y = a * exp(-0.5 * ((x-b)/c)<sup>d</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], coeff[3]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((x_in-b) / c, d));\n"
        return s



class LogNormal2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Log-Normal Peak"
    _HTML = "y = a * exp(-0.5 * ((ln(x)-b)/c)<sup>2</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c")
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], 2.0));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[2] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_LogX(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in)-b) / c, 2.0));\n"
        return s



class LogNormal_Modified2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Log-Normal Peak Modified"
    _HTML = "y = a * exp(-0.5 * ((ln(x)-b)/c)<sup>d</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], coeff[3]));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[2] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_LogX(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in)-b) / c, d));\n"
        return s



class ArnoldCohenLogNormalShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = False
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Arnold Cohen Log-Normal Peak Shifted"
    _HTML = "y = (a * exp(-0.5 * ((ln(x-e)-b)/c)<sup>2</sup>)) / (d * (x-e))"
    coefficientDesignatorTuple = ("a", "b", "c", 'd', 'e')
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = (coeff[0] * exp(-0.5 * pow((log(_id[_cwo[0]+i] - coeff[4]) - coeff[1]) / coeff[2], 2.0))) / (coeff[3] * (_id[_cwo[0]+i] - coeff[4]));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[2] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * exp(-0.5 * pow((log(x_in-e)-b) / c, 2.0))) / (d * (x_in-e));\n"
        return s



class ArnoldCohenTwoParameterLogNormalShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = False
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name = "Arnold Cohen Two-Parameter Log-Normal Peak Shifted"
    _HTML = "y = exp(-0.5 * ((ln(x-e)-b)/c)<sup>2</sup>) / (sqrt(2*pi) * c * (x-e))"
    coefficientDesignatorTuple = ("b", "c", 'e')
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = exp(-0.5 * pow((log(_id[_cwo[0]+i] - coeff[2]) - coeff[0]) / coeff[1], 2.0)) / (2.506628274631000502415765284811 * coeff[1] * (_id[_cwo[0]+i] - coeff[2]));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[1] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-0.5 * pow((log(x_in-e)-b) / c, 2.0)) / (2.506628274631000502415765284811  * c * (x_in-e));\n"
        return s



class LogNormalShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Log-Normal Peak Shifted"
    _HTML = "y = a * exp(-0.5 * ((ln(x-d)-b)/c)<sup>2</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((log(_id[_cwo[0]+i] - coeff[3]) - coeff[1]) / coeff[2], 2.0));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[2] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in-d)-b) / c, 2.0));\n"
        return s



class LogNormal_ModifiedShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Log-Normal Peak Modified Shifted"
    _HTML = "y = a * exp(-0.5 * ((ln(x-e)-b)/c)<sup>d</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd', 'e')
    CannotAcceptDataWithZeroX = True
    CannotAcceptDataWithNegativeX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow((log(_id[_cwo[0]+i] - coeff[4]) - coeff[1]) / coeff[2], coeff[3]));'
    requiresCoefficientBoundsCheckWhenFitting = 1


    def Initialize(self):
        pythonequations.EquationBaseClasses.Equation2D.Initialize(self)

        try:
            self.lowerCoefficientBoundsArray[2] = 0.0
        except:
            pass

    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in-e)-b) / c, d));\n"
        return s



class ExtremeValue2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Extreme Value Peak"
    _HTML = "y = a * exp(-exp(-((x-b)/c))-((x-b)/c)+1.0)"
    coefficientDesignatorTuple = ("a", "b", "c")
    function_cpp_code = 'temp = coeff[0] * exp(-1.0 * exp(-1.0 * ((_id[_cwo[0]+i]-coeff[1])/coeff[2])) - ((_id[_cwo[0]+i]-coeff[1])/coeff[2]) + 1.0);'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * exp(-1.0 * ((x_in-b)/c))-((x_in-b)/c) + 1.0);\n"
        return s



class Logistic2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Logistic Peak"
    _HTML = "y = 4a * exp(-1.0 * (x-b) / c) / (1.0 + exp(-1.0 * (x-b) / c))"
    coefficientDesignatorTuple = ("a", "b", "c")
    function_cpp_code = 'temp = 4.0 * coeff[0] * exp(-1.0 * ((_id[_cwo[0]+i] - coeff[1])) / coeff[2]) / (1.0 + exp(-1.0 * ((_id[_cwo[0]+i] - coeff[1])) / coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 4.0 * a * exp(-1.0 * (x_in - b) / c) / (1.0 + exp(-1.0 * (x_in - b) / c));\n"
        return s



class Pulse2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Pulse Peak"
    _HTML = "y = 4a * exp(-(x-b)/c) * (1.0 - exp(-(x-b)/c))"
    coefficientDesignatorTuple = ("a", "b", "c")
    function_cpp_code = 'temp = 4.0 * coeff[0] * exp(-1.0 * (_id[_cwo[1]+i] - coeff[1]) / coeff[2]) * (1.0 - exp(-1.0 * (_id[_cwo[1]+i] - coeff[1]) / coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Ones(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 4.0 * a * exp(-1.0 * (x_in-b) / c) * (1.0 - exp(-1.0 * (x_in-b) / c));\n"
        return s



class WeibullPeak2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Weibull Peak"
    _HTML = "y = a * exp(-0.5 * (ln(x/b)/c)<sup>2</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c")
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow(log(_id[_cwo[0]+i] / coeff[1]) / coeff[2], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, 2.0));\n"
        return s



class WeibullPeak_Modified2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Weibull Peak Modified"
    _HTML = "y = a * exp(-0.5 * (ln(x/b)/c)<sup>d</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow(log(_id[_cwo[0]+i] / coeff[1]) / coeff[2], coeff[3]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, d));\n"
        return s



class WeibullPeakShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Weibull Peak Shifted"
    _HTML = "y = a * exp(-0.5 * (ln((x-d)/b)/c)<sup>2</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow(log((_id[_cwo[0]+i]-coeff[3]) / coeff[1]) / coeff[2], 2.0));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-d)/b) / c, 2.0));\n"
        return s



class WeibullPeak_ModifiedShifted2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Weibull Peak Modified Shifted"
    _HTML = "y = a * exp(-0.5 * (ln((x-e)/b)/c)<sup>d</sup>)"
    coefficientDesignatorTuple = ("a", "b", "c", 'd', 'e')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = coeff[0] * exp(-0.5 * pow(log((_id[_cwo[0]+i]-coeff[4]) / coeff[1]) / coeff[2], coeff[3]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-e)/b) / c, d));\n"
        return s



class PseudoVoight2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Pseudo-Voight Peak"
    _HTML = "y = a * (d * (1/(1+((x-b)/c)<sup>2</sup>)) + (1-d) * exp(-0.5 * ((x-b)/c)<sup>2</sup>))"
    coefficientDesignatorTuple = ("a", "b", "c", 'd')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], 2.0);\n'
    function_cpp_code += 'temp = coeff[0] * (coeff[3] * (1.0 / (1.0 + temp)) + (1.0-coeff[3]) * exp(-0.5 * temp));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = pow((x_in-b) / c, 2.0);\n"
        s = "\ttemp = a * (d * (1.0 / (1.0 + temp)) + (1.0-d) * exp(-0.5 * temp));\n"
        return s



class PseudoVoight_Modified2D(pythonequations.EquationBaseClasses.Equation2D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name = "Pseudo-Voight Peak Modified"
    _HTML = "y = a * (d * (1/(1+((x-b)/c)<sup>e</sup>)) + (1-d) * exp(-0.5 * ((x-b)/c)<sup>f</sup>))"
    coefficientDesignatorTuple = ("a", "b", "c", 'd', 'f')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = pow((_id[_cwo[0]+i] - coeff[1]) / coeff[2], coeff[4]);\n'
    function_cpp_code += 'temp = coeff[0] * (coeff[3] * (1.0 / (1.0 + temp)) + (1.0-coeff[3]) * exp(-0.5 * temp));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = pow((x_in-b) / c, f);\n"
        s = "\ttemp = a * (d * (1.0 / (1.0 + temp)) + (1.0-d) * exp(-0.5 * temp));\n"
        return s

