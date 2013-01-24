#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: ExtraCodeForEquationBaseClasses.py 327 2011-09-23 17:38:44Z zunzun.com $

import numpy, scipy
numpy.seterr(all = 'raise') # numpy raises warnings, convert to exceptions to trap them


def GetCppCodeForActivationFunction(activationFunctionString, variableNameString):
    if activationFunctionString == 'LinearLayer':
        return '\t' + variableNameString + ' = '+ variableNameString + ';\n'
    if activationFunctionString == 'SigmoidLayer': # 1. / (1. + safeExp(-x))
        return '\t' + variableNameString + ' = 1.0 / (1.0 + exp(-1.0 * ' + variableNameString + '));\n'
    if activationFunctionString == 'TanhLayer': # outbuf[:] = tanh(inbuf)
        return '\t' + variableNameString + ' = tanh(' + variableNameString + ');\n'
    raise Exception('Unknown or unused activation function ' + activationFunctionString)


class custom_prng_for_diffev(numpy.random.mtrand.RandomState):
    def __init__(self):
        numpy.random.mtrand.RandomState.__init__(self)
        self.max_index = 5000
        self.array = numpy.random.rand(self.max_index)
        self.index = 0

    
    def rand(self, size):
        if self.index + size > self.max_index:
            self.index = 0
        return_val = self.array[self.index:self.index + size]
        self.index += size
        return return_val
    
    
    
def CG_Ones(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Ones'
    return numpy.ones_like(data[0])
    

def CG_X(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'X'
    return data[0]


def CG_NegX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'NegX'
    return -1.0 * data[0]


def CG_Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Y'
    return data[1]

    
def CG_NegY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'NegY'
    return -1.0 * data[1]


def CG_SinX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'SinX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.sin(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_TanX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'TanX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.tan(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_CoshX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'CoshX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.cosh(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_Log10X(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Log10X'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log10(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowX_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(data[0], args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowLogX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowLogX_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.log(data[0]), args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowExpX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowExpX_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue =  numpy.power(numpy.exp(data[0]), args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_Polyfunctional2D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Polyfunctional2D_' + str(args)
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = eqInstance.Polyfun2DEqList[args].value(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_Polyrational2D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Polyrational2D_' + str(args)
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = eqInstance.Polyrat2DEqList[args].value(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_TwoPiX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'TwoPiX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = 2.0 * numpy.pi * data[0]
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_NistEnsoCosX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'NistEnsoCosX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue =  numpy.cos(2.0 * numpy.pi * data[0] / 12.0)
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_NistEnsoSinX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'NistEnsoSinX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.sin(2.0 * numpy.pi * data[0] / 12.0)
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_ExpX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'ExpX'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.exp(data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_ExpXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'ExpXY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.exp(data[0] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_XSQMINUSYSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'XSQMINUSYSQ'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = (data[0] * data[0]) - (data[1] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_YSQMINUSXSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'YSQMINUSXSQ'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = (data[1] * data[1]) - (data[0] * data[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_XSQPLUSYSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'XSQPLUSYSQ'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = (data[0] * data[0]) + (data[1] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'ExpY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.exp(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_Polyfunctional3D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Polyfunctional3D_' + str(args)
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = eqInstance.Polyfun3DEqList[args[0]].value(data[0]) * eqInstance.Polyfun3DEqList[args[1]].value(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowLogY_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.log(data[1]), args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowExpY_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.exp(data[1]), args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowX_PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowX_PowY_' + str(args[0]) + str(args[1])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(data[0], args[0]) * numpy.power(data[1], args[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowLogX_PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowLogX_PowLogY_' + str(args[0]) + str(args[1])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.log(data[0]), args[0]) * numpy.power(numpy.log(data[1]), args[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowExpX_PowExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowExpX_PowExpY_' + str(args[0]) + str(args[1])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.exp(data[0]), args[0]) * numpy.power(numpy.exp(data[1]), args[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowX_PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowX_PowLogY_' + str(args[0]) + str(args[1])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(data[0], args[0]) * numpy.power(numpy.log(data[1]), args[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowLogX_PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowLogX_PowY_' + str(args[0]) + str(args[1])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(numpy.log(data[0]), args[0]) * numpy.power(data[1], args[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'PowY_' + str(args[0])
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.power(data[1], args[0])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_Log10Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'Log10Y'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log10(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogXY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[0] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_SinXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'SinXY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.sin(data[0] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_TanXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'TanXY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.tan(data[0] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_CoshXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'CoshXY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.cosh(data[0] * data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_CoshY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'CoshY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.cosh(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_TanY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'TanY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.tan(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_SinY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'SinY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.sin(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_XY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'XY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = data[0] * data[1]
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogX_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogX_LogY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[0]) * numpy.log(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_ExpX_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'ExpX_LogY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.exp(data[0]) * numpy.log(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogX_ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogX_ExpY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[0]) * numpy.exp(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_ExpX_ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'ExpX_ExpY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.exp(data[0]) * numpy.exp(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_X_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'X_LogY'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = data[0] * numpy.log(data[1])
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LogX_Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LogX_Y'
    try: # numpy.seterr(all = 'raise') and numpy.seterr(all = 'ignore') control behavior here
        returnValue = numpy.log(data[0]) * data[1]
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


# see http://en.wikipedia.org/wiki/Legendre_polynomials
def CG_LegendreX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
    cosineFlag = args[1]
    
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LegendreX_' + str(n)
            
    try:
        if cosineFlag == 1: # convert degrees to radians
            data = numpy.cos(numpy.radians(data[0]))
        elif cosineFlag == 2: # already in radians
            data = numpy.cos(data[0])
        else: # no cosine
            data = data[0]

        if n == 0:
            returnValue = numpy.ones_like(data)
        elif n == 1:
            returnValue = data
        elif n == 2:
            returnValue = (1.0 / 2.0) * (3.0*numpy.power(data, 2.0) - 1.0)
        elif n == 3:
            returnValue = (1.0 / 2.0) * (5.0*numpy.power(data, 3.0) - 3.0*data)
        elif n == 4:
            returnValue = (1.0 / 8.0) * (35.0*numpy.power(data, 4.0) - 30.0*numpy.power(data, 2.0) + 3.0)
        elif n == 5:
            returnValue = (1.0 / 8.0) * (63.0*numpy.power(data, 5.0) - 70.0*numpy.power(data, 3.0) + 15.0*data)
        elif n == 6:
            returnValue = (1.0 / 16.0) * (231.0*numpy.power(data, 6.0) - 315.0*numpy.power(data, 4.0) + 105.0*numpy.power(data, 2.0) - 5.0)
        elif n == 7:
            returnValue = (1.0 / 16.0) * (429.0*numpy.power(data, 7.0) - 693.0*numpy.power(data, 5.0) + 315.0*numpy.power(data, 3.0) - 35.0*data)
        elif n == 8:
            returnValue = (1.0 / 128.0) * (6435.0*numpy.power(data, 8.0) - 12012.0*numpy.power(data, 6.0) + 6930.0*numpy.power(data, 4.0) - 1260.0*numpy.power(data, 2.0) + 35.0)
        elif n == 9:
            returnValue = (1.0 / 128.0) * (12155.0*numpy.power(data, 9.0) - 25740.0*numpy.power(data, 7.0) + 18018.0*numpy.power(data, 5.0) - 4620.0*numpy.power(data, 3.0) + 315.0*data)
        elif n == 10:
            returnValue = (1.0 / 256.0) * (46189.0*numpy.power(data, 10.0) - 109395.0*numpy.power(data, 8.0) + 90090.0*numpy.power(data, 6.0) - 30030.0*numpy.power(data, 4.0) + 3465.0*numpy.power(data, 2.0) - 63.0)
        else:
            raise Exception("Legendre Polynomial Degree of " + str(n) + " is too high, please use a degree of 10 or less.") # will be trapped
            
        returnValue[numpy.invert(numpy.isfinite(returnValue))] = 1.0E300
        return returnValue
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CG_LegendreCosineDegreesX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
    
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LegendreCosineDegreesX_' + str(n)
    else:
        return CG_LegendreX(data=data, args = [n, 1], eqInstance=eqInstance, NameOrValueFlag=NameOrValueFlag)


def CG_LegendreCosineRadiansX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
    
    if NameOrValueFlag == 1: # name used by cache, must be distinct
        return 'LegendreCosineRadiansX_' + str(n)
    else:
        return CG_LegendreX(data=data, args = [n, 2], eqInstance=eqInstance, NameOrValueFlag=NameOrValueFlag)


