import numpy as np
class NeuralNet:
    def __init__(self, num_hidden_layers, layer_sizes ,activations ):
        ### first element in layer_sizes is input dimension and last element is output dimension##

        self.L = num_hidden_layers + 1 # doesn't include input layer
        self.input_dim = layer_sizes[0]
        assert(len(layer_sizes) == self.L + 1) ### Input_size, hidden layer sizes and output layer size
        self.output_dim = layer_sizes[self.L]
        assert(len(activations) == self.L)
        self.layer_sizes = layer_sizes
        self.activations = activations
        ### Initializing Weights and Biases ####
        self.b = []
        for i in range(self.L):
            self.b.append( np.zeros( (self.layer_sizes[i+1],1) ) ) ## i+1 because 0 index is the Input layer
        self.W = []
        ### Xavier Initialization Ref: deeplearning.ai/ai-notes/initializing...###
        for i in range(self.L):
            a = self.layer_sizes[i]
            b = self.layer_sizes[i+1]
            self.W.append(  np.random.randn(b,a)*( np.sqrt(2/(a+b)) ) )
    #### Activation Functions ######
    def relu(self, x):
        ## works for vector
        return np.maximum(0, x, x)
    def tanh(self, x):
        ## works for vector
        return np.tanh(x)
    def sigmoid(self, x):
        ### check if this works for a vector
        return 1/(1 + np.exp(-x))
    ### Output Activations ###
    def softmax(self, a):
        pass 
    def activate(self, activation, x):
        if activation == 'relu':
            return self.relu(x)
        elif activation == 'tanh':
            return self.tanh(x)
        elif activation == 'sigmoid':
            return self.sigmoid(x)
        elif activation == 'softmax':
            return self.softmax(x)
    def forward(self, inputs):
        a = []
        for l in range(1,self.L+1):
            ### Layer l ###
            ### Aggregation ###
            z = None
            if l == 1:
                input_transpose = inputs.T 
                assert(self.W[l-1].shape[1] == input_transpose.shape[0])
                z = np.matmul(self.W[l-1],inputs.T) + self.b[l-1]
            else:
                assert(self.W[l-1].shape[1] == a[l-2].shape[0])
                z = np.matmul(self.W[l-1],a[l-2]) + self.b[l-1]
            
            ### Activation ###
            a.append(self.activate(self.activations[l-1]),z)
        output = a[-1]
        return output
    def softmax_grad(x):
        pass
    def activation_grads(self, activation, x):
        if activation == 'relu':
            return np.greater(x,0).astype(int)
        elif activation == 'tanh':
            return 1 - np.square(self.tanh(x))
        elif activation == 'sigmoid':
            f = self.sigmoid(x)
            return f*(1-f)
        elif activation == 'softmax':
            return self.softmax_grad(x)
    def backward_prop(self, inputs, outputs):
        ## returns gradient of weights, biases
        dW = []
        db = []
        for i in range(self.L):
            a = self.layer_sizes[i]
            b = self.layer_sizes[i+1]
            dW.append(np.zeros((b,a)))
            db.append(np.zeros((b,1)))
    def update_params(self, grads, eta, optimizer):
        dW = None 
        db = None
        ### Assuming dW and db has the grads
        if optimizer == 'gd':
            self.W += np.multiply(dW,eta)
            self.b += np.multiply(db,eta)
        else:
            pass
        ### Other optimzers are to be implemented



    def fit(self, train_inputs, valid_inputs, train_outputs, valid_outputs, batch_size):
        ## All inputs and outputs are numpy arrays
        ### Gradient Descent ####
        train_size = train_inputs.shape[0]
        valid_size = valid_inputs.shape[0] 
        t = 0
        max_epochs = 100
        while(t<max_epochs):
            t+=1
            loss = 0
            #### Minibatch ####
            st = 0
            end = batch_size
            while(end <= train_size):
                mini_input = train_inputs[st:end]
                mini_output = train_outputs[st:end]
                st = end 
                end = st+batch_size 
                ### Network predicted outputs ###
                y_hat = self.forward(mini_input)
                assert(y_hat.shape  == mini_output.shape[0])
                grads = self.backward_prop(mini_input,mini_output)
                ## grads should have dW and db
                self.update_params(grads)

                ##update loss ##
            ## Print Loss and change in accuracy for each epoch for Training####

            ## Do the same with validation data ##

        ### log training ............... ##    


















    

