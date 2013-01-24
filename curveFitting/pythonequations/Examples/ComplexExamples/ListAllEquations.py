#! /usr/bin/python
#    Version info: $Id: ListAllEquations.py 230 2010-06-30 20:20:14Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os, inspect;
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


for submodule in inspect.getmembers(pythonequations.Equations2D) + inspect.getmembers(pythonequations.Equations3D):
    if inspect.ismodule(submodule[1]):
        print submodule[0]
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                extendedNameList = pythonequations.EquationBaseClasses.Equation.ExtendedFormsDict.keys()
                extendedNameList.sort()
                for extendedName in extendedNameList:
                    try:
                        equation = equationClass[1](extendedName)
                    except:
                        continue
                    
                    print "      " + equation.name, str(equation.dimensionality) + "D"
        print
