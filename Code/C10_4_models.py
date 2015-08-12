''' Three different ways to fit a linear model:
- analytically
- using the statsmodels tools
- using the formula-based approach

'''

# author: Thomas Haslwanter, date: Jun-2015

import numpy as np
import matplotlib.pyplot as plt

def createData():
    ''' Generate a noisy, slightly quadratic dataset '''
    x = np.arange(100)
    y = 150 + 3*x + 0.03*x**2 + 5*np.random.randn(len(x))
    return(x,y)

def analyticalSolution(x,y):
    '''Analytical solution, using "lstsq" '''
    
    # Create the Design Matrices
    M1 = np.vstack( (np.ones_like(x), x) ).T
    M2 = np.vstack( (np.ones_like(x), x, x**2) ).T
    M3 = np.vstack( (np.ones_like(x), x, x**2, x**3) ).T
    
    # an equivalent alternative solution with statsmodels would be e.g.
    # M1 = sm.add_constant(x)
    
    # Solve the equations
    p1 = np.linalg.lstsq(M1, y)
    p2 = np.linalg.lstsq(M2, y)
    p3 = np.linalg.lstsq(M3, y)
    
    # Print the results
    np.set_printoptions(precision=2)
    print('The coefficients from the linear fit: {0}'.format(p1[0]))
    print('The coefficients from the quadratic fit: {0}'.format(p2[0]))
    print('The coefficients from the cubic fit: {0}'.format(p3[0]))
    
    return (M1, M2, M3)

def smSolution(M1, M2, M3):
    '''Solution with the tools from statsmodels'''
    
    import statsmodels.api as sm
    import C2_8_mystyle
    
    Res1 = sm.OLS(y, M1).fit()
    Res2 = sm.OLS(y, M2).fit()
    Res3 = sm.OLS(y, M3).fit()
    
    print(Res1.summary2())
    print(Res2.summary2())
    print(Res3.summary2())
    
    # Plot the data
    plt.plot(x,y, '.', label='Data')
    plt.plot(x, Res1.fittedvalues, 'r--', label='Linear Fit')
    plt.plot(x, Res2.fittedvalues, 'g', label='Quadratic Fit')
    plt.plot(x, Res3.fittedvalues, 'y', label='Cubic Fit')
    plt.legend(loc='upper left', shadow=True)
    
    C2_8_mystyle.printout('linearModel.png', xlabel='x', ylabel='y')

def smfSolution(x,y):
    '''Formula-based modeling '''
    
    import pandas as pd
    import statsmodels.formula.api as smf
    
    # Turn the data into a pandas DataFrame,
    # so that we can address them in the formulas with their name
    df = pd.DataFrame({'x':x, 'y':y})
    
    # Fit the models, and show the results
    Res1F = smf.ols('y~x', df).fit()
    Res2F = smf.ols('y ~ x+I(x**2)', df).fit()
    Res3F = smf.ols('y ~ x+I(x**2)+I(x**3)', df).fit()
    
    print(Res1F.summary())
    print(Res2F.summary())
    print(Res3F.summary())
    
    #Res1.conf_int()
    #Res1F.conf_int()

if __name__=='__main__':
    x,y = createData()    
    M1, M2, M3 = analyticalSolution(x, y)        
    smSolution(M1, M2, M3)    
    smfSolution(x, y)