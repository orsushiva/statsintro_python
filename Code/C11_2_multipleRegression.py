'''Multiple Regression
Shows how to calculate just the best fit, or - using "statsmodels" - all the corresponding statistical parameters.
Also shows how to make 3d plots.

'''

# author: Thomas Haslwanter, date: July-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import C2_8_mystyle

# additional packages ...
# ... for the 3d plot ...
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# ... and for the statistic
from statsmodels.formula.api import ols

def generatedata():
    ''' Generate and show the data '''
    x = np.linspace(-5,5,101)
    (X,Y) = np.meshgrid(x,x)
    
    # To get reproducable values, I provide a seed value
    np.random.seed(987654321)   
    
    Z = -5 + 3*X-0.5*Y+np.random.randn(np.shape(X)[0], np.shape(X)[1])
    
    # Plot the figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X,Y,Z, cmap=cm.afmhot, rstride=2, cstride=2, 
        linewidth=0, antialiased=False)
    ax.view_init(20,-120)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.colorbar(surf, shrink=0.6)
    
    outFile = '3dSurface.png'
    C2_8_mystyle.printout_plain(outFile)
    
    
    return (X.flatten(),Y.flatten(),Z.flatten())

def regressionmodel(X,Y,Z):
    '''Multilinear regression model, calculating fit, P-values, confidence intervals etc.'''
    
    # Convert the data into a Pandas DataFrame
    df = pd.DataFrame({'x':X, 'y':Y, 'z':Z})
    
    # --- >>> START stats <<< ---
    # Fit the model
    model = ols("z ~ x + y", df).fit()
    
    # Print the summary
    print((model.summary()))
    # --- >>> STOP stats <<< ---
    
    return model._results.params  # should be array([-4.99754526,  3.00250049, -0.50514907])

def linearmodel(X,Y,Z):
    '''Just fit the plane'''
    
    # --- >>> START stats <<< ---
    M = np.vstack((np.ones(len(X)), X, Y)).T
    bestfit = np.linalg.lstsq(M,Z)
    # --- >>> STOP stats <<< ---

    print(('Best fit plane:', bestfit))
    
    return bestfit
                  
if __name__ == '__main__':
    (X,Y,Z) = generatedata()    
    regressionmodel(X,Y,Z)    
    linearmodel(X,Y,Z)
