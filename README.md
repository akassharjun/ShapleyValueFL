# ShapleyValueFL
A pip library for computing the marginal contribution (Shapley Value) for each client in a Federated Learning environment.

## Usage

```python 
from svfl.svfl import calculate_sv

models = {
    "CLIENT ID 1" : Model(),
    "CLIENT ID 2" : Model()
}

def evaluate_model(model):
    # compute accuracy
    return accuracy

def fed_avg(models):
    # average the model updates, FedAvg is an example
    return model

calculate_sv(models, evaluate_model, fed_avg)
```

Send the model updates and client identifies as a key value pair