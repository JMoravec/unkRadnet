#    Version info: $Id: ListAllStandardEquations_2D.py 1 2012-01-07 22:20:43Z zunzun.com@gmail.com $

import os, sys, inspect

if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2, pyeq2.ExtendedVersionHandlers


if __name__ == "__main__":

    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in ['Default', 'Offset']:
                        
                        if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                            continue
    
                        equation = equationClass[1]('SSQABS', extendedVersionName)
                        print '2D ' + submodule[0] + ' --- ' + equation.GetDisplayName()
                        
    print 'Done.'