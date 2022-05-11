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

    all_perms = list(itertools.permutations(list(models.keys())))
    store = []

    for perm in all_perms:
        perm_values = {}
        local_models = {}
        for client_id in perm:
            # model is deepcopied inorder to not affect the actual model
            model = copy.deepcopy(models[client_id])
            local_models[client_id] = model

            current_value = model_evaluation_func(averaging_func(local_models))

            new_value = current_value - sum(perm_values.values())

            if new_value < 0:
                new_value = 0

            perm_values[client_id] = new_value

        store.append(perm_values)

    sv = {client_id:0 for client_id in models.keys()}

    for item in store:
        for key, value in item.items():
            sv[key] += value

    for key, value in sv.items():
        sv[key] = sv[key] / len(store)

    return sv