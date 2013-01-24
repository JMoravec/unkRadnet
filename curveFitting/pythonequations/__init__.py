#    pythonequations is a collection of equations expressed as Python classes
#    Copyright (C) 2008 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id: __init__.py 333 2011-11-26 19:18:28Z zunzun.com $


import EquationBaseClasses, EquationsForPolyfunctionals, Equations2D, Equations3D
import os, sys, inspect, StringIO, scipy, scipy.weave, shutil

svnRevisionNumber = '$Id: __init__.py 333 2011-11-26 19:18:28Z zunzun.com $'.split()[2] # subversion keyword subtitution on checkin

speedupFileNamePrefix = 'speedup_importing'
speedupImportFileName = speedupFileNamePrefix + '_' + svnRevisionNumber + '.py'

# remove old "speedup importing" files before attempting to make new file
allFilesInDir = os.listdir(os.path.dirname(__file__))
for fileName in allFilesInDir:
    if fileName.startswith(speedupFileNamePrefix) and not fileName.startswith(speedupImportFileName):
        # user may not have rights to delete file
        try:
            os.remove(os.path.join(os.path.dirname(__file__), fileName))

            # clean up weave's leftover mess on non-Unix operating systems
            # thanks to Stephen Kemp in London for pointing out the problem
            if (os.path.exists(scipy.weave.catalog.default_dir())):
                shutil.rmtree(scipy.weave.catalog.default_dir(), True)
        except:
            pass

speedupFileNameAndPath = os.path.join(os.path.dirname(__file__), speedupImportFileName)
if (os.path.exists(speedupFileNameAndPath)):
    exec('import ' + speedupImportFileName[:-3])
    equationCount = 0
    for submodule in inspect.getmembers(Equations2D) + inspect.getmembers(Equations3D):
        if True == inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if True == inspect.isclass(equationClass[1]):
                    equationClass[1].equationIndex = equationCount # give each equation class a unique identifying index matching the below function code
                    equationCount += 1
    exec('ExtraCodeForEquationBaseClasses.cppCodeForEvaluate = ' + speedupImportFileName[:-3] + '.cppCodeForEvaluate')
    exec('ExtraCodeForEquationBaseClasses.cppCodeForGA = ' + speedupImportFileName[:-3] + '.cppCodeForGA')
else:
    # to allocate C++ function array, first count the total number of equations
    equationCount = 0
    for submodule in inspect.getmembers(Equations2D) + inspect.getmembers(Equations3D):
        if True == inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if True == inspect.isclass(equationClass[1]):
                    equationCount += 1
                    
    # clean up weave's leftover mess on non-Unix operating systems
    # thanks to Stephen Kemp in London for pointing out the problem
    if (os.path.exists(scipy.weave.catalog.default_dir())):
        shutil.rmtree(scipy.weave.catalog.default_dir(), True)



    # two code fragments will be generated, one for evaluating and one for Genetic Algorithm (GA) use

    ExtraCodeForEquationBaseClasses.cppCodeForEvaluate = '''
double temp, temp_x_sq, temp_y_sq, s_sq, s_over_r, s_sq_b, s_over_r_b;
int i, k;
int functionArrayInitializedFlag = 0;

void (*functionArray[''' + str(equationCount) + '''])(int, int, int, int, int*, double*, double*, double*, int*) = {NULL};
'''

    ExtraCodeForEquationBaseClasses.cppCodeForGA = '''
double temp, temp_x_sq, temp_y_sq, s_sq, s_over_r, s_sq_b, s_over_r_b, summation;
int i, k;
int functionArrayInitializedFlag = 0;

double (*functionArray[''' + str(equationCount) + '''])(int, int, int, int, int*, double*, double*, double*, int*) = {NULL};
'''

    cppCodeForFunctionPointerArrayInitialization = '''
void initializeFunctionPointerArray()
{
    if (0 != functionArrayInitializedFlag)
    {
        return;
    }
    functionArrayInitializedFlag = 1;
        
'''

    # shrink this code for better "weave"  compilation characteristics immediately below
    extendedFormSwitchCaseCode = '''
switch(extFormFlag) // does nothing for "case 0", the non-extended form of the base equation
{
    case 0: // non-extended version
        break;

    case 1: // Offset
        temp = temp + coeff[_nc];
        break;
        
    case 2: // Reciprocal
        temp = 1.0 / temp;
        break;

    case 3: // ReciprocalWithOffset
        temp = 1.0 / temp + coeff[_nc];
        break;

    case 4: // InverseX
    case 14: // InverseXY
        temp = _id[_cwo[len_cgl-1] + i] / temp;
        break;

    case 5: // InverseXWithOffset
    case 15: // InverseXYWithOffset
        temp = _id[_cwo[len_cgl-2] + i] / temp + coeff[_nc];
        break;

    case 6: // X_LinearDecay
    case 8: // X_ExponentialDecay
        temp = temp / (coeff[_nc] * _id[_cwo[len_cgl-1] + i]);
        break;

    case 7: // X_LinearDecayAndOffset
    case 9: // X_ExponentialDecayAndOffset
        temp = temp / (coeff[_nc] * _id[_cwo[len_cgl-2] + i]) + coeff[_nc+1];
        break;

    case 10: // X_LinearGrowth
    case 12: // X_ExponentialGrowth
        temp = temp * (coeff[_nc] * _id[_cwo[len_cgl-1] + i]);
        break;

    case 11: // X_LinearGrowthAndOffset
    case 13: // X_ExponentialGrowthAndOffset
        temp = temp * (coeff[_nc] * _id[_cwo[len_cgl-2] + i]) + coeff[_nc+1];
        break;
        
    case 16: // XY_LinearDecay
    case 18: // XY_ExponentialDecay
        temp = temp / (coeff[_nc] * _id[_cwo[len_cgl-1] + i]);
        break;

    case 17: // XY_LinearDecayAndOffset
    case 19: // XY_ExponentialDecayAndOffset
        temp = temp / (coeff[_nc] * _id[_cwo[len_cgl-2] + i]) + coeff[_nc+1];
        break;

    case 20: // XY_LinearGrowth
    case 22: // XY_ExponentialGrowth
        temp = temp * coeff[_nc] * _id[_cwo[len_cgl-1] + i];
        break;

    case 21: // XY_LinearGrowthAndOffset
    case 23: // XY_ExponentialGrowthAndOffset
        temp = temp * (coeff[_nc] * _id[_cwo[len_cgl-2] + i]) + coeff[_nc+1];
        break;
}
'''

    reducedString = ''
    linesOfText = StringIO.StringIO(extendedFormSwitchCaseCode).readlines()
    for line in linesOfText:
        line = line.strip()
        if len(line) < 1:
            continue
        index = line.find(' //')
        if index != -1:
            line = line[:index]
        reducedString += line
    extendedFormSwitchCaseCode = reducedString

    # make functions and place addresses into function pointer array
    equationCount = 0
    for submodule in inspect.getmembers(Equations2D) + inspect.getmembers(Equations3D):
        if True == inspect.ismodule(submodule[1]):
            ExtraCodeForEquationBaseClasses.cppCodeForEvaluate += '// MODULE ' + submodule[0] + '\n'
            ExtraCodeForEquationBaseClasses.cppCodeForGA += '// MODULE ' + submodule[0] + '\n'
            for equationClass in inspect.getmembers(submodule[1]):
                if True == inspect.isclass(equationClass[1]):
                    
                    equationClass[1].equationIndex = equationCount # give each equation class a unique identifying index matching the below function code
                    
                    equation = equationClass[1]() # need to make an instance so the extended forms can auto-generate themselves properly
                    
                    # len_cgl is length of cache generation list after extending
                    # _nc is number of coefficients before extending
                    ExtraCodeForEquationBaseClasses.cppCodeForEvaluate += '''
void function_''' + str(equationCount) + '''(int len_cgl, int extFormFlag, int _ndp, int _nc, int* _cwo, double* coeff, double* _id, double* resultArray, int* _pndia)
{for (i=0; i < _ndp; i++){try{''' + equation.function_cpp_code + extendedFormSwitchCaseCode + '''
#ifdef __GNUC__
if (!(__fpclassify (temp) & (FP_ZERO | FP_NORMAL))){temp = 1.0E300;}
#endif
}catch(...){temp = 1.0E300;}resultArray[i] = temp;}}
'''

                    # len_cgl is length of cache generation list after extending
                    # _nc is number of coefficients before extending
                    ExtraCodeForEquationBaseClasses.cppCodeForGA += '''
double function_''' + str(equationCount) + '''(int len_cgl, int extFormFlag, int _ndp, int _nc, int* _cwo, double* coeff, double* _id, double* dep_data, int* _pndia)
{summation = 0.0;for(i=0; i<_ndp; i++){try{''' + equation.function_cpp_code + extendedFormSwitchCaseCode + '''
#ifdef __GNUC__
if (!(__fpclassify (temp) & (FP_ZERO | FP_NORMAL))){summation = 1.0E300;break;}
#endif
temp = temp - dep_data[i];summation += temp * temp;}catch(...){summation = 1.0E300;break;}}return summation;}
'''

                    cppCodeForFunctionPointerArrayInitialization += '''
functionArray[''' + str(equationCount) + '''] = &function_''' + str(equationCount) + ''';
'''

                    equationCount += 1

    ExtraCodeForEquationBaseClasses.cppCodeForEvaluate += cppCodeForFunctionPointerArrayInitialization + '''
}
'''
    ExtraCodeForEquationBaseClasses.cppCodeForGA += cppCodeForFunctionPointerArrayInitialization + '''
}
'''
    
    # user may not have write priviliges to this directory, wrap in try/except block
    try:
        f = open(speedupFileNameAndPath, 'w')
        f.write('cppCodeForEvaluate = \'\'\'' + ExtraCodeForEquationBaseClasses.cppCodeForEvaluate + '\'\'\'\n\ncppCodeForGA = \'\'\'' + ExtraCodeForEquationBaseClasses.cppCodeForGA + '\'\'\'\n')
        f.close()
    except:
        pass
