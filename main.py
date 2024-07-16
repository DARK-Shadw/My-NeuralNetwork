import random
from NeuralNetwork import NeuralNetwork

nn = NeuralNetwork(2, 2, 1)

input = [1,0]
targets = [1, 0]

trainign_data =[
    {
        "input": [1,0],
        "targets": [1]
    },
    {
        "input": [0,1],
        "targets": [1]
    },
    {
        "input": [1,1],
        "targets": [0]
    },
    {
        "input": [0,0],
        "targets": [0]
    }
]
# output = nn.feedforward(input)

# nn.train(input, targets)
usr_data = []
while True:
    for i in range(10000):
        data = random.choice(trainign_data)
        nn.train(data["input"], data["targets"])

    
    print(nn.feedforward([0,0]))
    print(nn.feedforward([1,1]))
    print(nn.feedforward([0,1]))
    print(nn.feedforward([1,0]))

