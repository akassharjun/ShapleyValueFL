import copy
import itertools


def calculate_sv(models, model_evaluation_func, averaging_func):
    """
    Computes the Shapley Value for clients

    Parameters:
    models (dict): Key value pair of client identifiers and model updates.
    model_evaluation_func (func) : Function to evaluate model update.
    averaging_func (func) : Function to used to average the model updates.

    Returns:
    sv: Key value pair of client identifiers and the computed shapley values.

    """

    # find out all the possible permutations.
    all_perms = list(itertools.permutations(list(models.keys())))
    perm_data = []

    for perm in all_perms:
        perm_values = {}
        local_models = {}
        for client_id in perm:
            # model is deep copied in order to not affect the actual model.
            model = copy.deepcopy(models[client_id])
            local_models[client_id] = model

            current_value = model_evaluation_func(averaging_func(local_models))

            new_value = current_value - sum(perm_values.values())

            # if it's greater than 0, there is no improvement over it.
            if new_value < 0:
                new_value = 0

            perm_values[client_id] = new_value

        perm_data.append(perm_values)

    sv = {client_id:0 for client_id in models.keys()}

    for item in perm_data:
        # sum all the values in each permutation for the respective client.
        for key, value in item.items():
            sv[key] += value

    # average to compute the shapley value
    for key, value in sv.items():
        sv[key] = sv[key] / len(perm_data)

    return sv