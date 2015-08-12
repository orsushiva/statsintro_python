''' Different discrete distribution functions.
- Binomial distribution
- Poisson distribution (PMF, CDF, and PPF)

'''

# author: Thomas Haslwanter, date: Feb-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# additional packages
import C2_8_mystyle

#----------------------------------------------------------------------
def show_binomial():
    """Show an example of binomial distributions"""
    
    # Arbitrarily select 3 total numbers, and 3 probabilities
    ns = [20,20,40]
    ps = [0.5, 0.7, 0.5]
    
    # For each (p,n)-pair, plot the corresponding binomial PMFs
    for (p,n) in zip(ps, ns):
        bd = stats.binom(n,p)       # generate the "frozen function"
        x = np.arange(n+1)          # generate the x-values
        plt.plot(x, bd.pmf(x), 'o--', label='p={0:3.1f}, n={1}'.format(p,n))
    
    # Format the plot
    plt.legend()
    plt.title('Binomial distribuition')
    plt.xlabel('X')
    plt.ylabel('P(X)')
    plt.annotate('Upper Limit', xy=(20,0), xytext=(27,0.04), 
                 arrowprops=dict(shrink=0.05))
    
    # Show and save the plot
    C2_8_mystyle.printout_plain('Binomial_distribution_pmf.png')
    
#----------------------------------------------------------------------
def show_poisson():
    """Show an example of Poisson distributions"""
    
    # Arbitrarily select 3 lambda values
    lambdas = [1,4,10]
    
    k = np.arange(20)       # generate x-values
    markersize = 8
    for par in lambdas:
        plt.plot(k, stats.poisson.pmf(k, par), 'o--', label='$\lambda={0}$'.format(par))
    
    # Format the plot
    plt.legend()
    plt.title('Poisson distribuition')
    plt.xlabel('X')
    plt.ylabel('P(X)')
    
    # Show and save the plot
    C2_8_mystyle.printout_plain('Poisson_distribution_pmf.png')
    
#----------------------------------------------------------------------
def show_poisson_views():
    """Show different views of a Poisson distribution"""
    
    fig, ax = plt.subplots(3,1)
    
    k = np.arange(25)
    pd = stats.poisson(10)
    C2_8_mystyle.set(12)
    
    ax[0].plot(k, pd.pmf(k),'x-')
    ax[0].set_title('Poisson distribition')
    ax[0].set_xticklabels([])
    ax[0].set_ylabel('PMF (X)')
    
    ax[1].plot(k, pd.cdf(k))
    ax[1].set_xlabel('X')
    ax[1].set_ylabel('CDF (X)')
    
    y = np.linspace(0,1,100)
    ax[2].plot(y, pd.ppf(y))
    ax[2].set_xlabel('X')
    ax[2].set_ylabel('PPF (X)')
    
    plt.tight_layout()
    plt.show()
    
# -----------------------------------------------------------------------------------
if __name__ == '__main__':
    show_binomial()
    show_poisson()
    show_poisson_views()
