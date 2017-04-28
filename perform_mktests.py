import matplotlib.pylab as plt
import numpy as np
from scipy.stats import norm as nrm, mstats

from utils import *
from GitHubProject import *
from sonarqube_functions import *

def perform_mktests(repos):
    print ('Project Name (TD - trend, h, p, z) (normalized TD - trend, h, p, z)')
    for ghp in repos:
    #     print(ghp.repo)
        timemachine_metrics = get_sonarqube_timemachine_metrics_DataFrame(ghp)
        timemachine_metrics = timemachine_metrics.fillna(method='ffill')
        timemachine_metrics['normalized_td'] = timemachine_metrics['sqale_index']/timemachine_metrics['ncloc']
        timemachine_metrics = timemachine_metrics.fillna(0)
        timemachine_metrics = timemachine_metrics[timemachine_metrics.index.weekday==6]
        alpha=0.01
        #print(ghp.repo, mk_test(timemachine_metrics['violations'],alpha=alpha), mk_test(timemachine_metrics['blocker_violations'],alpha=alpha), mk_test(timemachine_metrics['critical_violations'],alpha=alpha), mk_test(timemachine_metrics['major_violations'],alpha=alpha), mk_test(timemachine_metrics['minor_violations'],alpha=alpha), mk_test(timemachine_metrics['info_violations'],alpha=alpha), mk_test(timemachine_metrics['open_issues'],alpha=alpha), mk_test(timemachine_metrics['complexity'],alpha=alpha), mk_test(timemachine_metrics['class_complexity'],alpha=alpha), mk_test(timemachine_metrics['file_complexity'],alpha=alpha), mk_test(timemachine_metrics['function_complexity'],alpha=alpha), mk_test(timemachine_metrics['comment_lines'],alpha=alpha), mk_test(timemachine_metrics['comment_lines_density'],alpha=alpha), mk_test(timemachine_metrics['duplicated_blocks'],alpha=alpha), mk_test(timemachine_metrics['duplicated_files'],alpha=alpha), mk_test(timemachine_metrics['duplicated_lines'],alpha=alpha), mk_test(timemachine_metrics['duplicated_lines_density'],alpha=alpha), mk_test(timemachine_metrics['code_smells'],alpha=alpha), mk_test(timemachine_metrics['sqale_index'],alpha=alpha), mk_test(timemachine_metrics['sqale_debt_ratio'],alpha=alpha), mk_test(timemachine_metrics['bugs'],alpha=alpha), mk_test(timemachine_metrics['reliability_remediation_effort'],alpha=alpha), mk_test(timemachine_metrics['vulnerabilities'],alpha=alpha), mk_test(timemachine_metrics['security_remediation_effort'],alpha=alpha), mk_test(timemachine_metrics['classes'],alpha=alpha), mk_test(timemachine_metrics['directories'],alpha=alpha), mk_test(timemachine_metrics['files'],alpha=alpha), mk_test(timemachine_metrics['lines'],alpha=alpha), mk_test(timemachine_metrics['ncloc'],alpha=alpha), mk_test(timemachine_metrics['functions'],alpha=alpha), mk_test(timemachine_metrics['statements'],alpha=alpha), mk_test(timemachine_metrics['normalized_td'],alpha=alpha))
        print(ghp.repo, mk_test(timemachine_metrics['sqale_index'],alpha=alpha), mk_test(timemachine_metrics['normalized_td'],alpha=alpha))
    #     res = sm.tsa.seasonal_decompose(timemachine_metrics['normalized_td'])
    #     residual = res.residual
    #     seasonal = res.seasonal
    #     trend = res.trend

def mk_test(x, alpha = 0.05):  
    """
    
    http://michaelpaulschramm.com/simple-time-series-trend-analysis/
    
    Input:
        x:   a vector of data
        alpha: significance level (0.05 default)

    Output:
        trend: tells the trend (increasing, decreasing or no trend)
        h: True (if trend is present) or False (if trend is absence)
        p: p value of the significance test
        z: normalized test statistics 

    Examples
    --------
      >>> x = np.random.rand(100)
      >>> trend,h,p,z = mk_test(x,0.05) 
    """
    n = len(x)

    # calculate S 
    s = 0
    for k in range(n-1):
        for j in range(k+1,n):
            s += np.sign(x[j] - x[k])

    # calculate the unique data
    unique_x = np.unique(x)
    g = len(unique_x)

    # calculate the var(s)
    if n == g: # there is no tie
        var_s = (n*(n-1)*(2*n+5))/18
    else: # there are some ties in data
        tp = np.zeros(unique_x.shape)
        for i in range(len(unique_x)):
            tp[i] = sum(unique_x[i] == x)
        var_s = (n*(n-1)*(2*n+5) + np.sum(tp*(tp-1)*(2*tp+5)))/18

    if s>0:
        z = (s - 1)/np.sqrt(var_s)
    elif s == 0:
            z = 0
    elif s<0:
        z = (s + 1)/np.sqrt(var_s)

    # calculate the p_value
    p = 2*(1-nrm.cdf(abs(z))) # two tail test
    h = abs(z) > nrm.ppf(1-alpha/2) 

    if (z<0) and h:
        trend = 'decreasing'
    elif (z>0) and h:
        trend = 'increasing'
    else:
        trend = 'no trend'

    return trend, h, p, z
    #return trend, z