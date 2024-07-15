from matrix import Matrix

from math import exp

def sigmoid(n):
    return 1 / (1 + exp(-n))

class NeuralNetwork:
    def __init__(self, n_input, n_hidden, n_output) -> None:
        self.num_input = n_input
        self.num_hidden = n_hidden
        self.num_output = n_output
        self.weigths_ih = Matrix(self.num_hidden, self.num_input)
        self.weigths_ho = Matrix(self.num_output, self.num_hidden)
        self.weigths_ih.randomize()
        self.weigths_ho.randomize()

        self.bias_h = Matrix(self.num_hidden, 1)
        self.bias_o = Matrix(self.num_output, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()




    def feedforward(self, input_arr):

        input = Matrix.fromArray(input_arr)

        # Generating the Hidden layer data
        hidden = Matrix.multiply(self.weigths_ih, input)    # Weigthed sum from input to hidden
        hidden.add(self.bias_h)         # adding bias
        hidden.map(sigmoid)             # activation function

        # Generating Output layer data
        output = Matrix.multiply(self.weigths_ho, hidden)    # Weigthed sum from hidden to output
        output.add(self.bias_o)         # adding bias
        output.map(sigmoid)             # activation function

        return output.toArray()
    
    def train(self, inputs, targets):
        outputs = self.feedforward(inputs)

        outputs = Matrix.fromArray(outputs)
        targets = Matrix.fromArray(targets)

        # calculate the output layers error
        output_errors = Matrix.substract(targets, outputs)

        # Calculate the hidden layers error
        who_t = Matrix.transpose(self.weigths_ho)
        hidden_errors = Matrix.multiply(who_t, output_errors)

        # TODO: Implement or use Gradient Descent to tweak the weights based on the errors