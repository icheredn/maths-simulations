import logging
import numpy as np
import time
import matplotlib.pyplot as plt


def plot_cdf(X):
    num_points = 30
    min_val = np.min(X)
    max_val = np.max(X)
    d = (max_val - min_val)/(num_points-1)

    interval_partition = np.array([min_val+i*d for i in range(num_points)])

    X_len = len(X)
    cdf_values = np.array([np.sum(X <= x)/X_len for x in interval_partition])

    plt.plot(interval_partition, cdf_values)

    return interval_partition, cdf_values


def plot_density(int_div, cdf_values):
    num_points = len(int_div)
    pdf_values = (cdf_values[2:]-cdf_values[:num_points-2]) / (int_div[2:] - int_div[:num_points-2])

    plt.plot(int_div[1:num_points-1], pdf_values)


def main():
    logging.basicConfig(level=logging.INFO, format='\x1b[35m%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    start = time.perf_counter()

    X = np.random.random(500_000)

    X_sqrt = np.sqrt(X)

    lam = 10
    X_exp_dist = -1/lam * np.log(1-X) # F(x) = 1 - exp(-lambda*x)

    X_log_dist = np.exp(2*X - 1) # F(x) = 1/2 * (1 + log(x)) : 1/e < x < e
    end = time.perf_counter()

    logging.info(f'Sample mean: {X.mean()} Sample std: {X.std()}')
    logging.info(f'Exec time: {end - start}')

    # plt.hist(x=X, bins=50)
    # int_div, cdf_vals = plot_cdf(X)
    # plot_density(int_div, cdf_vals)

    # plt.hist(x=X_sqrt, bins=50, histtype='step')
    int_div, cdf_vals = plot_cdf(X_sqrt)
    plot_density(int_div, cdf_vals)

    # plt.hist(x=X_exp_dist, bins=50)
    # int_div, cdf_vals = plot_cdf(X_exp_dist)
    # plot_density(int_div, cdf_vals)

    # plt.hist(x=X_log_dist, bins=50)
    # int_div, cdf_vals = plot_cdf(X_log_dist)
    # plot_density(int_div, cdf_vals)


    # num_poi = 20
    # d = (3 - 0.3) / (num_poi - 1)
    # int_division = np.array([0.3 + i * d for i in range(num_poi)])
    # plt.scatter(int_division, 1/2*(1+np.log(int_division)))

    plt.show()


if __name__ == '__main__':
    main()

