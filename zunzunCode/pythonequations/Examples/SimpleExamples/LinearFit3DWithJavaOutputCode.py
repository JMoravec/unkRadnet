#! /usr/bin/python
#    Version info: $Id: LinearFit3DWithJavaOutputCode.py 297 2011-02-15 20:36:09Z zunzun.com $

# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os;
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


equation = pythonequations.Equations3D.Polynomial.Linear3D() # Simple surface

equation.fittingTarget = 'SSQABS' # see the Equation base class for a list of fitting targets
equation.ConvertTextToData(equation.exampleData) # Equations have ASCII text data for testing and examples

equation.Initialize() # now that the equation has data, set up the cache

# If performing a nonlinear fit and you have parameter estimates, set them
# instead of calling this method.  This call is harmless for linear fits
equation.SetGAParametersAndGuessInitialCoefficientsIfNeeded() # estimate initial parameters if needed

equation.FitToCacheData() # perform the fit


print equation.name, str(equation.dimensionality) + "D"

# Choose your language...
#print equation.CodeCPP()     # C++
#print equation.CodeCS()      # C#
print equation.CodeJAVA()     # Java
#print equation.CodeMATLAB()  # MATLAB
#print equation.CodePYTHON()  # Python
#print equation.CodeSCILAB()  # SCILAB
#print equation.CodeVBA()     # VB for Applications
