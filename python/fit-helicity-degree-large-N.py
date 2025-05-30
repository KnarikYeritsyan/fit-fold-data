import numpy as np
from sympy.abc import s,sigma,h,Q,o,p,T	#t_0 = o, h_ps = p
from sympy.utilities.lambdify import lambdify
from sympy import sqrt,exp
from pandas import read_csv
from scipy.optimize import curve_fit
import pandas as pd
import sys
import json
import os

R = 8.3

datafile = sys.argv[1]
temperature = sys.argv[2]

def sigma_func(Q):
    return Q**(-1)

def t_func(T):
    return R*T

def s_func(T,o,h,p,Q,q):
    return Q**(-1)*((exp(-h/(t_func(T)-R*o))+(exp((p-h)/(t_func(T)-R*o))-exp(-h/(t_func(T)-R*o)))/q)**(-2)-1)

def theta_func(sigma,s):
    return ((s+sigma)/(1+s+sqrt((1-s)**2+4*sigma*s)))*(1+(2*sigma-1+s)/(sqrt((1-s)**2+4*sigma*s)))

def theta(T,o,h,p,Q,q=16):
    return theta_func(sigma,s).subs([(sigma,sigma_func(Q)),(s,s_func(T,o,h,p,Q,q))])

print_data={}

if os.path.isfile(sys.argv[1]):
    file_extension = os.path.splitext(sys.argv[1])[1]
    if file_extension.lower() == ".csv":
        try:
            data = read_csv(sys.argv[1], header=None).values
        except:
            print_data['error_message'] = 'Could not process data, please check if the data file is in proper format'
            print(json.dumps(print_data))
            exit()
    else:
        try:
            data = np.loadtxt(sys.argv[1])
        except:
            print_data['error_message'] = 'Could not process data, please check if the data file is in proper format'
            print(json.dumps(print_data))
            exit()

try:
    x_exp, y_exp = data.T
except:
    print_data['error_message'] = 'Could not process data, please check if the data file is in proper format'
    print(json.dumps(print_data))
    exit()

if temperature:
    x_exp = x_exp+273.15

# o_guess=x_exp[0]-1
o_guess=x_exp[x_exp == min(x_exp)][0]-1
h_guess=3200.0
p_guess=1.0*h_guess
Q_guess=300.0

ff=[o_guess,h_guess,p_guess,Q_guess]

xopt = np.arange(o_guess-2, x_exp[x_exp == max(x_exp)][0]+3, 0.5, dtype=np.float64)
# myfunc = lambdify((T,o,h,p,Q),theta(T,o,h,p,Q),'numpy')
myfunc = lambdify((T,o,h,p,Q),theta(T,o*o_guess,h*h_guess,p*p_guess,Q*Q_guess),'numpy')

initial_guess=[0.75,1.2,1.2,1.0]

try:
    pars, pcov = curve_fit(myfunc, x_exp, y_exp, p0=initial_guess,  bounds=[[0.1, 0.1, 0.1, 0.01], [0.99, 2.0, 2.0, 2.0]])
    perr = np.sqrt(np.diag(pcov))
    residuals = y_exp-myfunc(x_exp, *pars)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y_exp-np.mean(y_exp))**2)
    r_squared = 1 - (ss_res / ss_tot)
    o_error=100 * perr[0] / abs(pars[0])
    h_error=100 * perr[1] / abs(pars[1])
    p_error=100 * perr[2] / abs(pars[2])
    Q_error=100 * perr[3] / abs(pars[3])
    yopt = myfunc(xopt,*pars)
except:
    print_data['error_message'] = 'Could not fit data, please check if the data is correct'
    print(json.dumps(print_data))
    exit()

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

try: r_squared
except NameError: r_squared = None

if r_squared is None:
    print_data['error_message'] = 'Could not fit data, please check if the data is correct'
else:
    print_data.update({'fit_params': {}})
    print_data.update({'fit_params_errors': {}})
    print_data['fit_params']['t0']=round(pars[0]*o_guess,2)
    print_data['fit_params']['h']=round(pars[1]*h_guess,2)
    print_data['fit_params']['h_ps']=round(pars[2]*p_guess,2)
    print_data['fit_params']['Q']=round(pars[3]*Q_guess,2)
    print_data['fit_params_errors']['t0']=round(o_error,2)
    print_data['fit_params_errors']['h']=round(h_error,2)
    print_data['fit_params_errors']['h_ps']=round(p_error,2)
    print_data['fit_params_errors']['Q']=round(Q_error,2)
    print_data['r_squared']=truncate(r_squared,4)
    print_data['sigma']=round(1/print_data['fit_params']['Q'],5)
    # print_data['xopt']=xopt
    # print_data['yopt']=yopt
    print_data['xexp']=pd.Series(x_exp).to_json(orient='values')
    print_data['yexp']=pd.Series(y_exp).to_json(orient='values')
    print_data['xopt']=pd.Series(xopt).to_json(orient='values')
    print_data['yopt']=pd.Series(yopt).to_json(orient='values')
    if o_error>50 or h_error>50 or p_error>50 or Q_error>50 or r_squared<0.5:
        print_data['warning_message'] = 'One or more parameters errors are large, please check the data again!'


def show_data():
    # return print(print_data)
    return print(json.dumps(print_data))
    # return print_data

show_data()