import sys, os
sys.path.append('./rawData')
import calculate
from calculate import *

sys.path.append('./fitToCurve')
import splitData
from splitData import *

def checkInput():
	bla = raw_input('Do these numbers match up with data book? [y,n]: ')
	if bla == 'y' or bla == 'Yes' or bla == 'yes':
		os.system('mv ' + sys.argv[1] + ' ./rawData')
		return True
	elif bla == 'n' or bla == 'No' or bla == 'no':
		print('Check your typed and printed data! Removing generated file, run this program again when fixed')
		os.system('rm ' + sys.argv[1] + 'Activity')
		return False
	else:
		print("You didn't type 'y' or 'n', try again")
		if checkInput() == True:
			return True
		else:
			return False
	
calculate(sys.argv[1])

if checkInput() == True:
	#run the fit curve program
	fitToCurve(sys.argv[1] + 'Activity')
	os.system('mv ' + sys.argv[1] + 'Activity ' + './fitToCurve')
