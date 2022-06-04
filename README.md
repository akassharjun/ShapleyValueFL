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

The marginal contribution of the $i-th$ participant is defined as $
(v(S\cup \{i\}) - v(S))$ when they join this coalition.

Let's see this equation in action, consider a Federated Learning environment with three clients, so $N = \{0, 1, 2\}$. We list the contribution of each subset within this coalition. Let's consider the contribution to be measured in terms of model accuracy.


<div align="center">

$v(\emptyset) = 0$ &emsp;&emsp; $v(\{0\}) = 40$ &emsp;&emsp; $v(\{1\}) = 60$ &emsp;&emsp; $v(\{2\}) = 80$

$v(\{0,1\}) = 70$ &emsp;&emsp; $v(\{0,2\}) = 75$ &emsp;&emsp; $v(\{1,2\}) = 85$

$v(\{0,1,2\}) = 90$
</div>

| Subset  | Client #0 | Client #1 | Client #2 |
| ------------- | ------------- | ------------- | ------------- |
| $0 \leftarrow 1 \leftarrow 2$ | 40  | 30 | 20 |
| $0 \leftarrow 2 \leftarrow 1$ | 40  | 15 | 35 |
| $1 \leftarrow 0 \leftarrow 2$ | 10  | 60 | 20 |
| $1 \leftarrow 2 \leftarrow 0$ | 5  | 60 | 25 |
| $2 \leftarrow 0 \leftarrow 1$ | 0  | 10 | 80 |
| $2 \leftarrow 1 \leftarrow 0$ | 5  | 5 | 80 |
| $Sum$ | 100  | 180 | 260 |
| $\phi(i)$ | 16.67  | 30 | 20 |

The arrow signifies the order in which each client joins the coalition. Consider the
first iteration $0 \leftarrow 1 \leftarrow 2$, we calculate the marginal contribution of each client using the
above equation. Client 0's is $v(\{0\}) = 40$. Client 1's is $v(\{0, 1\}) - v(\{0\}) = 30$. Finally Client 2's marginal contribution is given as $v(\{0, 1, 2\}) - v(\{0, 1\}) - v(\{0\}) = 20$. The marginal contribution is calculated for each permutation
likewise, and the Shapley Value is derived by averaging all of these marginal contributions.

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
    # function to merge the model updates into one model for evaluation, ex: FedAvg, FedProx
    return model

# returns a key value pair with the client identifier and it's respective Shapley Value
contribution_measure = calculate_sv(models, evaluate_model, fed_avg)
```

## Future Work

- Built-in support for standard averaging methods like FedAvg, & FedProx.



## Feedback
Any feedback/corrections/additions are welcome:

If this was helpful, please leave a star on the [github](https://github.com/akassharjun/ShapleyValueFL) page.