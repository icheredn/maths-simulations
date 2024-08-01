import matplotlib.pyplot as plt
import numpy as np

def plot_power_of_unity(z, m, M):
    """
        Plot all values 1^z in the complex exponential sense 
        i.e. 1^z = exp(z*ln(1)) = exp(z*[ln(1)+i*arg(1)]) = exp(z*2pi*k*i)
  
    """
    X = [np.cos(2*z*np.pi*k) for k in range(m, M)]
    Y = [np.sin(2*z*np.pi*k) for k in range(m, M)]

    fig, axes = plt.subplots(figsize=(7.5,7.5))

    axes.add_patch(plt.Circle((0, 0), 1, color='g', fill=False))

    axes.scatter(X, Y)
    for i in range(m, M):
        axes.annotate(f'{str(i)}', (X[i-m], Y[i-m]))

    #axes.spines[['right', 'top']].set_visible(False)
    plt.grid()
    fig.tight_layout()
    plt.show()

#plot_power_of_unity(np.sqrt(3), 0, 50)
#plot_power_of_unity(np.pi, 0, 50)

#plot_power_of_unity(np.e, 0, 72) # very close to 71-st root of unity but permutated
#plot_power_of_unity(1/71, 0, 100)
#plot_power_of_unity(np.e, 71, 143)
#plot_power_of_unity(np.e, 142, 214)

#plot_power_of_unity(1/np.e, 0, 200) # almost root 193
# plot_power_of_unity(1/193, 0, 200)

plot_power_of_unity((np.sqrt(5)-1)/2, 0, 988)
