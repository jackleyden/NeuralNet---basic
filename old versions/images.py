from numpy import exp, array, random, dot
from PIL import Image
import numpy as np

#https://medium.com/technology-invention-and-more/how-to-build-a-multi-layered-neural-network-in-python-53ec3d1d326a

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1
        self.bias = 1

class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)
            
            #print(training_set_outputs, output_from_layer_2,layer2_error)
            
            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

            ## Adjust the bias
            self.layer1.bias += 0.1 * np.sum(layer1_delta)
            self.layer2.bias += 0.1 * np.sum(layer2_delta)

    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights)+self.layer1.bias)
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights)+self.layer2.bias)
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self):
        print("    Layer 1 (4 neurons, each with 3 inputs): ")
        print(self.layer1.synaptic_weights)
        print("L1 bias", self.layer1.bias)
        print("    Layer 2 (1 neuron, with 4 inputs):")
        print(self.layer2.synaptic_weights)
        print("L2 bias", self.layer2.bias)


def imageOutResult(s,x,y):#test outputs for the akkad demo images
    if s == x:
        outNode1.append(y[0])
        outNode2.append(y[1])
        outNode3.append(y[2])
        outNode4.append(y[3])
                
if __name__ == "__main__":
    #   o
    #o<   \
    #   o
    #o<   >  o - data 1
    #   o
    #o<   >  o - data 2
    #   o
    #o<   >  o - data 3
    #   o
    #o<   >  o - data 4
    #   o
    #o    /
    #   o
    
    
    imgArray = [] #final 
    outNode1 = []
    outNode2 = []
    outNode3 = []
    outNode4 = []
    outNode5 = []
    outNode6 = []
    outNode7 = []
    outNode8 = []
    outNode9 = []
    outNode10 = []
    outNode11 = []
    outNode12 = []
    outNode13 = []
    outNode14 = []


    #append pixles for inputs
    for s in range(0,13+1): #0-13 results
        for t in range(0,1): #3 test images for every expected result
            im = Image.open("images/images/Akkad/"+str(s)+"."+str(t)+".png")
            im1 = np.asarray(im)
            img1 = []
            
            for i in range(len(im1)): #extract image pixel data
                for j in range(len(im1[i])):
                    img1.append(im1[i][j][0]);
            imgArray.append(img1) #append image to array of images

            for checkx in range(4): #test expected outputs append
                y = [0,0,0,0]
                y[checkx] = 1 #change the zero that is to be the expected outcome
                imageOutResult(s,checkx,y) #if s == checkx then append y to array

    
    imgArray = array(imgArray)
    
    #Seed the random number generator
    random.seed(1)    

    # Create layer 1 (7 neurons, each with 6 inputs)
    layer1 = NeuronLayer(20, len(img1)) #all images must be the same pixel size

    # Create layer 2 (4 single neuron with 7 inputs)
    layer2 = NeuronLayer(8, 20)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork(layer1, layer2)


    print("Stage 1) Random starting synaptic weights: ")
    neural_network.print_weights()

    # The training set. We have 7 examples, each consisting of 3 input values
    # and 1 output value.

    training_set_inputs = array([[1, 0, 1, 0, 1, 0],
                                 [0, 1, 1, 0, 1, 1],
                                 [0, 0, 1, 0, 0, 1],
                                 [0, 1, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 1],
                                 [1, 1, 1, 1, 1, 1],
                                 [0, 0, 0, 0, 0, 0],
                                 [254, 254, 254, 254, 254, 254]])
    
    # each line down is a node      v  v  v  v  v  v  v
    training_set_outputs2 = array([[1 ,0, 0, 0, 1, 0, 0, 1],
                                   [0 ,1, 0, 0, 0, 1, 0, 1],
                                   [0 ,0, 1, 0, 0, 0, 1, 1],
                                   [0 ,0, 0, 1, 1, 1, 1, 1]]).T ####

    #image rec outputs
    img_training_set_outputs = array([outNode1,
                                      outNode2,
                                      outNode3,
                                      outNode4]).T
                                    #  0 1 2 3 4 5 6 7 8 9 10111213
    img_training_set_outputs = array([[1,0,0,0,0,0,0,0,1,0,0,1,1,0],
                                      [0,1,0,0,0,0,0,0,1,1,0,1,1,0],
                                      [0,0,1,0,0,0,0,0,1,0,0,0,1,0],
                                      [0,0,0,1,0,0,0,0,1,1,0,0,1,0],
                                      
                                      [0,0,0,0,1,0,0,0,0,0,1,1,1,0],
                                      [0,0,0,0,0,1,0,0,0,1,1,1,1,0],
                                      [0,0,0,0,0,0,1,0,0,0,1,0,1,0],
                                      [0,0,0,0,0,0,0,1,0,1,1,0,1,0],
                                      ]).T
    print("Test Inputs: ", len(img1))
    print(imgArray)

    print("Test Outputs: ")
    print(img_training_set_outputs)
    


    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    neural_network.train(imgArray, img_training_set_outputs, 100000)
    
    print("Stage 2) New synaptic weights after training for single stage output: ")
    neural_network.print_weights()

    check = "check"
    while True:
        inputt = str(input())
        if inputt != "":
            check = "images/images/Akkad/"+inputt
        im = Image.open(check+".png")
        imcheck = np.asarray(im)
        
        checkimg = []
        for i in range(len(imcheck)):
            for j in range(len(imcheck[i])):
                checkimg.append(imcheck[i][j][0]);
                
        # Test the neural network with a new situation.

        #data for check
        #data = array([inputdata, inputdata1, inputdata2, inputdata3, inputdata4, inputdata5])
        
        print("Stage 3) Considering a new situation", array(checkimg), "-> ?: ")
        hidden_state, output = neural_network.think(array(checkimg))
        print("original: ", output)
        print("Rounded Result: ",[round(output.tolist()[0]),round(output.tolist()[1]),
              round(output.tolist()[2]), round(output.tolist()[3]),
              round(output.tolist()[4]),round(output.tolist()[5]),
              round(output.tolist()[6]), round(output.tolist()[7])])

        print("what it should be: ", img_training_set_outputs[int(float(inputt))])
