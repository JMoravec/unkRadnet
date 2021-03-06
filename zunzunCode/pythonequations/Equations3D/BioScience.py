#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: BioScience.py 274 2010-09-29 13:16:14Z zunzun.com $

import pythonequations, pythonequations.EquationBaseClasses, pythonequations.ExtraCodeForEquationBaseClasses
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


class ChenClayton3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Chen-Clayton"
    _HTML = "r.h.(T<sub>k</sub>,M) = exp(-(C1/T<sup>C2</sup>) * exp(-C3*T<sup>C4</sup>*M))"
    webCitationLink = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'
    coefficientDesignatorTuple = ('C1', 'C2', 'C3', 'C4')
    CannotAcceptDataWithZeroX = True
    function_cpp_code = 'temp = exp(-1.0 * (coeff[0]/pow(_id[_cwo[0]+i],coeff[1])) * exp(-1.0*coeff[2]*pow(_id[_cwo[0]+i],coeff[3])*_id[_cwo[1]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * (C1/pow(x_in,C2)) * exp(-1.0 * C3 * pow(x_in, C4) * y_in));\n"
        return s



class ModifiedChungPfost3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Modified Chung-Pfost"
    _HTML = "r.h.(T,M) = exp(-(C1/(T+C2)) * exp(-C3*M))"
    webCitationLink = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'
    coefficientDesignatorTuple = ('C1', 'C2', 'C3')
    function_cpp_code = 'temp = exp(-1.0 * (coeff[0]/(_id[_cwo[0]+i]+coeff[1])) * exp(-1.0*coeff[2]*_id[_cwo[1]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * (C1/(x_in+C2)) * exp(-1.0 * C3 * y_in));\n"
        return s



class ModifiedHalsey3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Modified Halsey"
    _HTML = "r.h.(T,M) = exp(-exp(C1 + C2*T) * M<sup>-C3</sup>)"
    webCitationLink = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'
    coefficientDesignatorTuple = ('C1', 'C2', 'C3')
    function_cpp_code = 'temp = exp(-1.0 * exp(coeff[0] + coeff[1] * _id[_cwo[0]+i]) * pow(_id[_cwo[1]+i], -1.0 * coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * exp(C1 + C2*x_in) * pow(y_in, -1.0 * C3));\n"
        return s



class ModifiedHenderson3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Modified Henderson"
    _HTML = "r.h.(T,M) = 1 - exp(-C1 * (T + C2) * M<sup>C3</sup>)"
    webCitationLink = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'
    coefficientDesignatorTuple = ('C1', 'C2', 'C3')
    function_cpp_code = 'temp = 1.0 - exp(-1.0 * coeff[0] * (_id[_cwo[0]+i]+coeff[1]) * pow(_id[_cwo[1]+i], coeff[2]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 - exp(-1.0 * C1 * (x_in + C2) * pow(y_in, C3));\n"
        return s



class StrohmanYoerger3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Strohman-Yoerger"
    _HTML = "r.h.(P<sub>s</sub>,M) = exp(C1*exp(-C2*M)*ln(P<sub>s</sub>) - C3*exp(-C4*M))"
    webCitationLink = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'
    coefficientDesignatorTuple = ('C1', 'C2', 'C3', 'C4')
    function_cpp_code = 'temp = exp(coeff[0]*exp(-1.0*coeff[1]*_id[_cwo[1]+i])*log(_id[_cwo[0]+i]) - coeff[2]*exp(-1.0*coeff[3]*_id[_cwo[1]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = exp(C1*exp(-C2*y_in)*log(x_in) - C3*exp(-C4*y_in));\n"
        return s



class LogisticGrowth3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = False
    RequiresAutoGeneratedReciprocalForm = False
    RequiresAutoGeneratedInverseForms = False
    _name ="Logistic Growth"
    _HTML = "z = a / (1 + exp(-(b + cx + dy + fxy))) + g"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd', 'f', 'g')
    function_cpp_code = 'temp = coeff[0] / (1.0 + exp(-1.0 * (coeff[1] + coeff[2] * _id[_cwo[0]+i] + coeff[3] * _id[_cwo[1]+i] + coeff[4] * _id[_cwo[0]+i] * _id[_cwo[1]+i]))) + coeff[5];'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + exp(-1.0 * (b + c * x_in + d * y_in + f * x_in * y_in))) + g;\n"
        return s



class HighLowAffinityIsotopeDisplacement3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="High-Low Affinity Isotope Displacement (y = [Hot])"
    _HTML = "z = aby / (1+b(x+y))"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = (coeff[0] * coeff[1] * _id[_cwo[1]+i]) / (1.0 + coeff[1] * (_id[_cwo[0]+i] + _id[_cwo[1]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * b * y_in) / (1.0 + b * (x_in + y_in));\n"
        return s



class HighLowAffinityDoubleIsotopeDisplacement3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="High-Low Affinity Double Isotope Displacement (y = [Hot])"
    _HTML = "z = aby / (1+b(x+y)) +  cdy / (1+d(x+y))"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = (coeff[0] * coeff[1] * _id[_cwo[1]+i]) / (1.0 + coeff[1] * (_id[_cwo[0]+i] + _id[_cwo[1]+i])) + (coeff[2] * coeff[3] * _id[_cwo[1]+i]) / (1.0 + coeff[3] * (_id[_cwo[0]+i] + _id[_cwo[1]+i]));'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * b * y_in) / (1.0 + b * (x_in + y_in)) + (c * d * y_in) / (1.0 + d * (x_in + y_in));\n"
        return s



class MichaelisMentenIsotopeDisplacement3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Michaelis-Menten Isotope Displacement (y = [Hot])"
    _HTML = "z = ay / (b + x + y)"
    coefficientDesignatorTuple = ("a", "b")
    function_cpp_code = 'temp = (coeff[0] * _id[_cwo[1]+i]) / (coeff[1] + _id[_cwo[0]+i] + _id[_cwo[1]+i]);'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * y_in) / (b + x_in + y_in);\n"
        return s



class MichaelisMentenDoubleIsotopeDisplacement3D(pythonequations.EquationBaseClasses.Equation3D):
    RequiresAutoGeneratedGrowthAndDecayForms = True
    RequiresAutoGeneratedOffsetForm = True
    RequiresAutoGeneratedReciprocalForm = True
    RequiresAutoGeneratedInverseForms = True
    _name ="Michaelis-Menten Double Isotope Displacement (y = [Hot])"
    _HTML = "z = ay / (b + x + y) +  cy / (d + x + y)"
    coefficientDesignatorTuple = ("a", "b", 'c', 'd')
    function_cpp_code = 'temp = (coeff[0] * _id[_cwo[1]+i]) / (coeff[1] + _id[_cwo[0]+i] + _id[_cwo[1]+i]) + (coeff[2] * _id[_cwo[1]+i]) / (coeff[3] + _id[_cwo[0]+i] + _id[_cwo[1]+i]);'


    def CreateCacheGenerationList(self):
        self.CacheGenerationList = []
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_X(NameOrValueFlag=1), []])
        self.CacheGenerationList.append([pythonequations.ExtraCodeForEquationBaseClasses.CG_Y(NameOrValueFlag=1), []])

    def SpecificCodeCPP(self):
        s = "\ttemp = (a * y_in) / (b + x_in + y_in) + (c * y_in) / (d + x_in + y_in);\n"
        return s
