from math import cos, sin, pi, floor, sqrt
import cmath
import matplotlib.pyplot as plt
import time
import numpy as np


def sum_cosines(t): # 1, 5, sqrt(2) Hz
    return cos(2*pi*t - pi/4) + cos(2*pi*5*t) + cos(2*pi*sqrt(2)*t) + cos(2*pi*100*t)

def make_cosine(freq, phase):
    return lambda t: cos(2*pi*freq*t + phase)

def const_signal(t):
    return 1

def rect(t):
    if -1/2 < t and t < 1/2:
        return 1
    elif t == -1/2 or t == 1/2:
        return 1/2
    else:
        return 0

def sinc(t):
    return sin(pi*t)/(pi*t)


def make_partition(t0, t1, sample_freq):
    L = t1 - t0
    T = 1 / sample_freq # sampling period
    N = floor(sample_freq * L) # num samples
    return [t0 + i*T for i in range(N)]


def sample_signal(signal, t_values):
    return [signal(t) for t in t_values]


def DFT(X):
    """
        Samples DTFT with period 1/N
    """
    N = len(X)
    ksi = cmath.exp(-2j*pi/N)
    S = [0]*N

    for f in range(N):
        compared_signal_f = ksi**f
        power = 1
        for n in range(N):
            S[f] += X[n] * power
            power *= compared_signal_f

    return S


def DTFT(X):
    """
        Return DTFT
    """
    
    N_input = len(X)

    def dtft(f):
        S = 0
        compared_signal_f = cmath.exp(-2j*pi*f)
        #print(f'{compared_signal_f=}')
        power = 1
        for n in range(N_input):
            S += X[n] * power
            power *= compared_signal_f
        #print(f'{S=}')
        return S
    
    return dtft


def abs_list(S):
    return [sqrt(z.real**2 + z.imag**2) for z in S]


def calc_and_plot_all(tasks: list[tuple[list[float], str, int]]): 

    N_tasks = len(tasks)
    print(N_tasks)
    fig, axes = plt.subplots(N_tasks, 1, figsize=(13,7.5))

    if N_tasks == 1:
        axes = [axes]

    i = 0
    for task in tasks:
        samples = task[0]
        transform_type = task[1]
        sampling_freq = task[2]
        sampling_int_length = len(samples)/sampling_freq
        if transform_type == 'DFT':
            df_transform = DFT(samples)
            axes[i].scatter([x/sampling_int_length for x in range(len(samples))], abs_list(df_transform), s=2)
            axes[i].grid()
        elif transform_type == 'DTFT':
            dtf_transform = DTFT(samples)
            partition = make_partition(0, 1, sample_freq=5000) # sample DFTF of rect at a very high frequency
            dtft_sampling = sample_signal(dtf_transform, partition)
            axes[i].plot(partition, abs_list(dtft_sampling), color='red')
            axes[i].grid()

        i += 1

    fig.tight_layout()
    plt.show()


def main():
    f_samp = 800
    input_1 = sample_signal(sum_cosines, make_partition(5, 50, f_samp))
    #calc_and_plot_all([(input_1, 'DTFT', f_samp),(input_1, 'DFT', f_samp)])

    # input_2 = sample_signal(lambda t: make_cosine(2, 0)(t) + make_cosine(20, 0)(t), make_partition(0, 50, f_samp))
    # calc_and_plot_all([(input_2, 'DTFT', f_samp)])
    
    input_3 = sample_signal(make_cosine(sqrt(2), 0), make_partition(0, 0.5, f_samp))
    calc_and_plot_all([(input_3, 'DTFT', f_samp), (input_3, 'DFT', f_samp)])

    # time_start = time.perf_counter()
    # fft_transform_1 = np.fft.fft(input_1)
    # time_end = time.perf_counter()
    # print(f'FFT exec time: {time_end - time_start}s')

    # input_const = sample_signal(const_signal, make_partition(0, 2, 50))
    # calc_and_plot_all([(input_const, 'DFT', 50)])
    
    
    # sampling_freq = 20
    # partition1 = make_partition(0, 100, sampling_freq)
    # calc_and_plot_all([
    #                     (sample_signal(rect, partition1), 'DFT', sampling_freq), 
    #                    (sample_signal(rect, partition1), 'DTFT', sampling_freq),
    #                    ])


if __name__ == '__main__':
    main()