# ShapleyValueFL
A pip library for computing the marginal contribution (Shapley Value) for each client in a Federated Learning environment.

## Usage

```python 
from svfl.svfl import calculate_sv

models = {
    "client-id-1" : ModelUpdate(),
    "client-id-2" : ModelUpdate().
    "client-id-3" : ModelUpdate().
}

def evaluate_model(model):
    # function to compute evaluation metric, ex: accuracy, precision
    return metric

def fed_avg(models):
    # function to average the model updates, FedAvg for example
    return model

# returns a key value pair with the client identifier and it's respective Shapley Value
contribution_measure = calculate_sv(models, evaluate_model, fed_avg)
```

## Future Work

- Built-in support for standard averaging methods like FedAvg, & FedProx.



## Feedback
Any feedback/corrections/additions are welcome:

If this was helpful, please leave a star on the [github](https://github.com/akassharjun/ShapleyValueFL) page.