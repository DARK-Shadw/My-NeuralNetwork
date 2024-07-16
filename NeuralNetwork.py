from matrix import Matrix

from math import exp

def sigmoid(n):
    return 1 / (1 + exp(-n))

def dsigmoid(y):
    return y * (1 - y)

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

        self.learning_rate = 0.1




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
        input = Matrix.fromArray(inputs)

        # Generating the Hidden layer data
        hidden = Matrix.multiply(self.weigths_ih, input)    # Weigthed sum from input to hidden
        hidden.add(self.bias_h)         # adding bias
        hidden.map(sigmoid)             # activation function

        # Generating Output layer data
        outputs = Matrix.multiply(self.weigths_ho, hidden)    # Weigthed sum from hidden to output
        outputs.add(self.bias_o)         # adding bias
        outputs.map(sigmoid)             # activation function

        targets = Matrix.fromArray(targets)

        # calculate the output layers error
        output_errors = Matrix.substract(targets, outputs)

        # Calculate Gradient
        gradients = Matrix.static_map(outputs, dsigmoid)
        gradients = Matrix.multiply(gradients, output_errors)
        gradients.multiply_scalar(self.learning_rate)


        # Calculate Output -> Hidden deltas
        # eq: <>W_ho = lr * E * (O*(1-0)*H))
        hidden_T = Matrix.transpose(hidden)
        weights_ho_delta = Matrix.multiply(gradients, hidden_T)

        # Adjust weights by delats
        self.weigths_ho.add(weights_ho_delta)
        # Adjust the deltas by its bias (which is just gradients)
        self.bias_o.add(gradients)


        # Calculate the hidden layers error
        who_t = Matrix.transpose(self.weigths_ho)
        hidden_errors = Matrix.multiply(who_t, output_errors)

        # Calculate hidden Gradient
        hidden_gradient = Matrix.static_map(hidden, dsigmoid)
        hidden_gradient = Matrix.multiply(hidden_gradient, hidden_errors)
        hidden_gradient.multiply_scalar(self.learning_rate)


        # Calculate Hidden -> Input deltas
        input_T = Matrix.transpose(input)
        weights_hi_delta = Matrix.multiply(hidden_gradient, input_T)


        self.weigths_ih.add(weights_hi_delta)
        self.bias_h.add(hidden_gradient)


    def set_learning_rate(self, n: float):
        self.learning_rate = n