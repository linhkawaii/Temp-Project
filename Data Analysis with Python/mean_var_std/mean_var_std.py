import numpy as np
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)

    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).item()]
    variance = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).item()]
    std_deviation = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).item()]
    max_value = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).item()]
    min_value = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).item()]
    sum_value = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).item()]

    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return result
    
