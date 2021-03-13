import wandb
wandb.init(name = 'test_run',
project='testing',
)
import dataset
import NeuralNet as nn

data = dataset.dataset()
X_train = data['x_train']
Y_train = data['y_train']
X_val = data['x_val']
Y_val = data['y_val']
input_dim = X_train.shape[1]
num_classes = Y_train.shape[1]
sweep_config = {
    'method': 'random', #grid, random
    'metric': {
      'name': 'val_accuracy',
      'goal': 'maximize'   
    },
    'parameters': {
        'epochs': {
            'values': [5, 10]
        },
        'num_hidden_layers': {
            'values': [3,4,5]
        },
        'hidden_layer_size': {
            'values': [32,64,128]
        },
        'weight_decay': {
            'values': [0, 0.0005, 0.5]
        },
        'learning_rate': {
            'values': [1e-3, 1e-4]
        },
        'optimizer': {
            'values': ['sgd', 'momentum','nesterov', 'rmsprop','adam','nadam']
        },
        'batch_size':{
            'values': [16,32,64]
        },
        'weight_init':{
            'values':['random','Xavier']
        },
        'activation': {
            'values': ['relu', 'elu', 'selu', 'softmax']
        }
    }
}
# swwep_id = wandb.sweep(sweep_config, entity="sweep",project="testing")
network = nn.NeuralNet(3,[input_dim,4,4,4,output_dim],['relu','relu','relu','soft_max'])
network.fit(X_train, X_val, Y_train, Y_val, 1000,'cross_entropy', 0.001, 'gd')
# Configure the sweep – specify the parameters to search through, the search strategy, the optimization metric et all.
