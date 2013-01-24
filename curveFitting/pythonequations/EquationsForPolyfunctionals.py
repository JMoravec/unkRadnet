#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: EquationsForPolyfunctionals.py 331 2011-11-25 12:21:22Z zunzun.com $

import sys
import numpy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them

class ExtendedFormBaseClass():
    CannotAcceptDataWithZeroX = False
    CannotAcceptDataWithZeroY = False
    CannotAcceptDataWithPositiveX = False
    CannotAcceptDataWithPositiveY = False
    CannotAcceptDataWithNegativeX = False
    CannotAcceptDataWithNegativeY = False

class Offset_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = ''
        self.JAVA = ''
        self.CPP = ''
        self.CSHARP = ''
        self.PYTHON = ''
        self.SCILAB = ''

    def value(self, x):
        return numpy.ones_like(x)


class ArcTangent_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'atan(' + variableName + ')'
        self.JAVA = 'Math.atan(' + codeName + ')'
        self.CPP = 'atan(' + codeName + ')'
        self.CSHARP = 'Math.Atan(' + codeName + ')'
        self.PYTHON = 'math.atan(' + codeName + ')'
        self.SCILAB = 'atan(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.arctan(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            print 'atan exception:', sys.exc_info()[0], sys.exc_info()[1]
            return 1.0E300 * numpy.ones_like(x)


class Power_NegativeOne_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithZeroY = True
        self._HTML = variableName + "<SUP>-1</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', -1.0)'
        self.CPP = 'pow(' + codeName + ', -1.0)'
        self.CSHARP = 'Math.Pow(' + codeName + ', -1.0)'
        self.PYTHON = 'math.pow(' + codeName + ', -1.0)'
        self.SCILAB = '(' + codeName + ' ^ -1.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, -1.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class HyperbolicCosine_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'cosh(' + variableName + ')'
        self.JAVA = 'Math.cosh(' + codeName + ')'
        self.CPP = 'cosh(' + codeName + ')'
        self.CSHARP = 'Math.Cosh(' + codeName + ')'
        self.PYTHON = 'math.cosh(' + codeName + ')'
        self.SCILAB = 'cosh(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.cosh(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_OnePointFive_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = variableName + "<SUP>1.5</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', 1.5)'
        self.CPP = 'pow(' + codeName + ', 1.5)'
        self.CSHARP = 'Math.Pow(' + codeName + ', 1.5)'
        self.PYTHON = 'math.pow(' + codeName + ', 1.5)'
        self.SCILAB = '(' + codeName + ' ^ 1.5)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, 1.5)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_ZeroPointFive_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = variableName + "<SUP>0.5</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', 0.5)'
        self.CPP = 'pow(' + codeName + ', 0.5)'
        self.CSHARP = 'Math.Pow(' + codeName + ', 0.5)'
        self.PYTHON = 'math.pow(' + codeName + ', 0.5)'
        self.SCILAB = '(' + codeName + ' ^ 0.5)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, 0.5)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class VariableUnchanged_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = variableName
        self.JAVA = codeName
        self.CPP = codeName
        self.CSHARP = codeName
        self.PYTHON = codeName
        self.SCILAB = codeName

    def value(self, x):
        return x


class Power_Two_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = variableName + "<SUP>2</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', 2.0)'
        self.CPP = 'pow(' + codeName + ', 2.0)'
        self.CSHARP = 'Math.Pow(' + codeName + ', 2.0)'
        self.PYTHON = 'math.pow(' + codeName + ', 2.0)'
        self.SCILAB = '(' + codeName + ' ^ 2.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, 2.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class HyperbolicSine_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'sinh(' + variableName + ')'
        self.JAVA = 'Math.sinh(' + codeName + ')'
        self.CPP = 'sinh(' + codeName + ')'
        self.CSHARP = 'Math.Sinh(' + codeName + ')'
        self.PYTHON = 'math.sinh(' + codeName + ')'
        self.SCILAB = 'sinh(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.sinh(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Exponential_VariableUnchanged_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'exp(' + variableName + ')'
        self.JAVA = 'Math.exp(' + codeName + ')'
        self.CPP = 'exp(' + codeName + ')'
        self.CSHARP = 'Math.Exp(' + codeName + ')'
        self.PYTHON = 'math.exp(' + codeName + ')'
        self.SCILAB = 'exp(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.exp(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Exponential_VariableTimesNegativeOne_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'exp(-' + variableName + ')'
        self.JAVA = 'Math.exp(-1.0 * ' + codeName + ')'
        self.CPP = 'exp(-1.0 * ' + codeName + ')'
        self.CSHARP = 'Math.Exp(-1.0 * ' + codeName + ')'
        self.PYTHON = 'math.exp(-1.0 * ' + codeName + ')'
        self.SCILAB = 'exp(-1.0 * ' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.exp(-x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Sine_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'sin(' + variableName + ')'
        self.JAVA = 'Math.sin(' + codeName + ')'
        self.CPP = 'sin(' + codeName + ')'
        self.CSHARP = 'Math.Sin(' + codeName + ')'
        self.PYTHON = 'math.sin(' + codeName + ')'
        self.SCILAB = 'sin(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.sin(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Cosine_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'cos(' + variableName + ')'
        self.JAVA = 'Math.cos(' + codeName + ')'
        self.CPP = 'cos(' + codeName + ')'
        self.CSHARP = 'Math.Cos(' + codeName + ')'
        self.PYTHON = 'math.cos(' + codeName + ')'
        self.SCILAB = 'cos(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.cos(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Tangent_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'tan(' + variableName + ')'
        self._HTML = 'tan(' + variableName + ')'
        self.JAVA = 'Math.tan(' + codeName + ')'
        self.CPP = 'tan(' + codeName + ')'
        self.CSHARP = 'Math.Tan(' + codeName + ')'
        self.PYTHON = 'math.tan(' + codeName + ')'
        self.SCILAB = 'tan(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.tan(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class HyperbolicTangent_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self._HTML = 'tanh(' + variableName + ')'
        self._HTML = 'tanh(' + variableName + ')'
        self.JAVA = 'Math.tanh(' + codeName + ')'
        self.CPP = 'tanh(' + codeName + ')'
        self.CSHARP = 'Math.Tanh(' + codeName + ')'
        self.PYTHON = 'math.tanh(' + codeName + ')'
        self.SCILAB = 'tanh(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.tanh(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_NegativeZeroPointFive_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithZeroY = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = variableName + "<SUP>-0.5</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', -0.5)'
        self.CPP = 'pow(' + codeName + ', -0.5)'
        self.CSHARP = 'Math.Pow(' + codeName + ', -0.5)'
        self.PYTHON = 'math.pow(' + codeName + ', -0.5)'
        self.SCILAB = '(' + codeName + ' ^ -0.5)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, -0.5)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_NegativeTwo_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithZeroY = True
        self._HTML = variableName + "<SUP>-2.0</SUP>"
        self.JAVA = 'Math.pow(' + codeName + ', -2.0)'
        self.CPP = 'pow(' + codeName + ', -2.0)'
        self.CSHARP = 'Math.Pow(' + codeName + ', -2.0)'
        self.PYTHON = 'math.pow(' + codeName + ', -2.0)'
        self.SCILAB = '(' + codeName + ' ^ -2.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(x, -2.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Log_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithZeroY = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = 'ln(' + variableName + ')'
        self.JAVA = 'Math.log(' + codeName + ')'
        self.CPP = 'log(' + codeName + ')'
        self.CSHARP = 'Math.Log(' + codeName + ')'
        self.PYTHON = 'math.log(' + codeName + ')'
        self.SCILAB = 'log(' + codeName + ')'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.log(x)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_NegativeOne_OfLog_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithZeroY = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = 'ln(' + variableName + ")<SUP>-1</SUP>"
        self.JAVA = 'Math.pow(Math.log(' + codeName + '), -1.0)'
        self.CPP = 'pow(log(' + codeName + '), -1.0)'
        self.CSHARP = 'Math.Pow(Math.Log(' + codeName + '), -1.0)'
        self.PYTHON = 'math.pow(math.log(' + codeName + '), -1.0)'
        self.SCILAB = '(log(' + codeName + ') ^ -1.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(numpy.log(x), -1.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_Two_OfLog_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithZeroY = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = 'ln(' + variableName + ")<SUP>2</SUP>"
        self.JAVA = 'Math.pow(Math.log(' + codeName + '), 2.0)'
        self.CPP = 'pow(log(' + codeName + '), 2.0)'
        self.CSHARP = 'Math.Pow(Math.Log(' + codeName + '), 2.0)'
        self.PYTHON = 'math.pow(math.log(' + codeName + '), 2.0)'
        self.SCILAB = '(log(' + codeName + ') ^ 2.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(numpy.log(x), 2.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)


class Power_NegativeTwo_OfLog_Term(ExtendedFormBaseClass):

    def __init__(self, variableName, codeName):
        self.CannotAcceptDataWithZeroX = True
        self.CannotAcceptDataWithNegativeX = True
        self.CannotAcceptDataWithZeroY = True
        self.CannotAcceptDataWithNegativeY = True
        self._HTML = 'ln(' + variableName + ")<SUP>-2</SUP>"
        self.JAVA = 'Math.pow(Math.log(' + codeName + '), -2.0)'
        self.CPP = 'pow(log(' + codeName + '), -2.0)'
        self.CSHARP = 'Math.Pow(Math.Log(' + codeName + '), -2.0)'
        self.PYTHON = 'math.pow(math.log(' + codeName + '), -2.0)'
        self.SCILAB = '(log(' + codeName + ') ^ -2.0)'

    def value(self, x):
        try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
            returnValue = numpy.power(numpy.log(x), -2.0)
            returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
            return returnValue
        except:
            return 1.0E300 * numpy.ones_like(x)



# variableName here could be x or y
# the order of occurrence in this list is the order of display on the web pages
def GenerateListForPolyfunctionals(variableName, codeName):
    EquationList = []
    
    EquationList.append(Offset_Term(variableName, codeName))
    
    EquationList.append(Power_ZeroPointFive_Term(variableName, codeName))
    EquationList.append(VariableUnchanged_Term(variableName, codeName))
    EquationList.append(Power_OnePointFive_Term(variableName, codeName))
    EquationList.append(Power_Two_Term(variableName, codeName))
    EquationList.append(Power_NegativeZeroPointFive_Term(variableName, codeName))
    EquationList.append(Power_NegativeOne_Term(variableName, codeName))
    EquationList.append(Power_NegativeTwo_Term(variableName, codeName))
    
    EquationList.append(Log_Term(variableName, codeName))
    EquationList.append(Power_Two_OfLog_Term(variableName, codeName))
    EquationList.append(Power_NegativeOne_OfLog_Term(variableName, codeName))
    EquationList.append(Power_NegativeTwo_OfLog_Term(variableName, codeName))
    
    EquationList.append(Exponential_VariableUnchanged_Term(variableName, codeName))
    EquationList.append(Exponential_VariableTimesNegativeOne_Term(variableName, codeName))
    
    EquationList.append(Sine_Term(variableName, codeName))
    EquationList.append(HyperbolicSine_Term(variableName, codeName))
    EquationList.append(Cosine_Term(variableName, codeName))
    EquationList.append(HyperbolicCosine_Term(variableName, codeName))
    EquationList.append(Tangent_Term(variableName, codeName))
    EquationList.append(ArcTangent_Term(variableName, codeName))
    EquationList.append(HyperbolicTangent_Term(variableName, codeName))

    return EquationList


# variableName here could be x or y
# this list is small due to my available CPU, you can add more to be thorough
def GenerateListForPolyrationals(variableName, codeName):
    EquationList = []
    
    EquationList.append(Offset_Term(variableName, codeName))
    
    EquationList.append(VariableUnchanged_Term(variableName, codeName))
    EquationList.append(Power_NegativeOne_Term(variableName, codeName))
    
    EquationList.append(Power_Two_Term(variableName, codeName))
    EquationList.append(Power_NegativeTwo_Term(variableName, codeName))
    
    EquationList.append(Log_Term(variableName, codeName))
    EquationList.append(Power_NegativeOne_OfLog_Term(variableName, codeName))

    EquationList.append(Exponential_VariableUnchanged_Term(variableName, codeName))
    EquationList.append(Exponential_VariableTimesNegativeOne_Term(variableName, codeName))

    return EquationList
