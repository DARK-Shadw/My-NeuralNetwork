from NeuralNetwork import NeuralNetwork

nn = NeuralNetwork(2, 2, 2)

input = [1,0]
targets = [1, 0]
# output = nn.feedforward(input)

nn.train(input, targets)

# print(output)