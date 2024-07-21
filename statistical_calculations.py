import statistics

def calculate_mean(values):
    return statistics.mean(values)

def calculate_median(values):
    return statistics.median(values)

def calculate_standard_deviation(values):
    return statistics.stdev(values)

def calculate_variance(values):
    return statistics.variance(values)

def calculate_coefficient_of_variation(values):
    mean = calculate_mean(values)
    std_dev = calculate_standard_deviation(values)
    return (std_dev / mean) * 100

def calculate_quartiles(values):
    return statistics.quantiles(values, n=4)
