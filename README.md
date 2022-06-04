# ShapleyValueFL
A pip library for computing the marginal contribution (Shapley Value) for each client in a Federated Learning environment.

## Table of Content
- [ShapleyValueFL](#shapleyvaluefl)
  - [Table of Content](#table-of-content)
  - [Brief](#brief)
  - [Usage](#usage)
  - [Future Work](#future-work)
  - [Feedback](#feedback)

## Brief
The Shapley Value is a game theory concept that explores how to equitably distribute rewards and costs among members of a coalition. It is extensively used in incentive mechanisms for Federated Learning to fairly distribute rewards to clients based on their contribution to the system.

Let $v(S)$ where $S\subset N$ is defined as the contribution of the model collaboratively trained by the subset $S$. $N$ is a set of all the participants in the system.
The $i-th$ participant’s Shapley Value $\phi(i)$ is defined as

$$\phi(i) = \sum_{S\subset N \backslash \{i\}} \frac{|S|!(N-|S|-1)!}{|N|!}(v(S\cup \{i\}) - v(S))$$

The marginal contribution of the $i-th$ participant is defined as $(v(S\cup \{i\}) - v(S))$ when they join this coalition.


## Usage

```python 
from svfl.svfl import calculate_sv

models = {
    "client-id-1" : ModelUpdate(),
    "client-id-2" : ModelUpdate(),
    "client-id-3" : ModelUpdate(),
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