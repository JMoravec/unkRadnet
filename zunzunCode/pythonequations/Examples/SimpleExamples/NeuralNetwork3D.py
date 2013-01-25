#! /usr/bin/python
#    Version info: $Id: NeuralNetwork3D.py 314 2011-07-11 08:50:50Z zunzun.com $
'''
# the pythonequations base is located up one directory from the top-level examples
# directory, go up one directory in the path from there for the import to work properly
import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pythonequations


neuralNetwork = pythonequations.Equations3D.NeuralNetwork.NeuralNetwork3D()
neuralNetwork.printExampleOutput = True # show extra information when running examples
neuralNetwork.hiddenNodeCountLayer_1 = 2 # how many hidden nodes in the first hidden layer?
neuralNetwork.hiddenNodeCountLayer_2 = 2 # how many hidden nodes in the second hidden layer?


neuralNetwork.ConvertTextToData(neuralNetwork.exampleData) # Neural networks have ASCII text data for testing and examples

neuralNetwork.Initialize() # now that the neural network has data, set up the cache


# search for best neuron activation functions rather than use default sigmoids
# this is time consuming but might be useful on difficult problems
#neuralNetwork.FindBestNeuralNetworkActivationFunctions()


neuralNetwork.TrainNeuralNetwork( 10 ) # train the neural network 10 times, yielding best-of-10 result

neuralNetwork.CalculateErrors() # so we can print the errors


if neuralNetwork.hiddenNodeCountLayer_2:
    print neuralNetwork.name, str(neuralNetwork.dimensionality) + "D", 'using', neuralNetwork.hiddenNodeCountLayer_1, 'node(s) in the first hidden layer and', neuralNetwork.hiddenNodeCountLayer_2, 'node(s) in the second hidden layer'
else:
    print neuralNetwork.name, str(neuralNetwork.dimensionality) + "D", 'using', neuralNetwork.hiddenNodeCountLayer_1, 'node(s) in a single hidden layer'

print
if neuralNetwork.testingForActivationFunctionsFlag:
    print "Search for activation functions was on:"
    print 'Hidden layer activation function:', neuralNetwork.bestHiddenActivationFunction.__name__
    print 'Ouput layer activation function:', neuralNetwork.bestOutputActivationFunction.__name__
else:
    print "Search for activation functions was off, using default sigmoid activation functions"

print
print neuralNetwork.fittingTarget + ":", neuralNetwork.CalculateFittingTarget(None)

print
for i in range(len(neuralNetwork.DependentDataArray)):
    print 'X:', neuralNetwork.IndependentDataArray[0][i],
    print 'Y:', neuralNetwork.IndependentDataArray[1][i],
    print 'Z', neuralNetwork.DependentDataArray[i],
    print 'Model:', neuralNetwork.PredictedArray[i],
    print 'Abs. Error:', neuralNetwork.AbsoluteErrorArray[i],
    print 'Rel. Error:', neuralNetwork.RelativeErrorArray[i],
    print 'Percent Error:', neuralNetwork.PercentErrorArray[i]
'''
