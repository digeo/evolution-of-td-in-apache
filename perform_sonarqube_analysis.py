import matplotlib.pylab as plt

from utils import *
from GitHubProject import *
from sonarqube_functions import *

def perform_the_analysis(repos):
        for ghp in repos:
            timemachine_metrics = get_sonarqube_timemachine_metrics_DataFrame(ghp)
            timemachine_metrics = timemachine_metrics.fillna(method='ffill')
            timemachine_metrics['normalized_td'] = timemachine_metrics['sqale_index']/timemachine_metrics['ncloc']
            timemachine_metrics = timemachine_metrics.fillna(0)
            issues = timemachine_metrics[['violations','blocker_violations','critical_violations','major_violations','minor_violations','info_violations','open_issues']]
            smells_bugs_classes = timemachine_metrics[['code_smells','bugs','classes']]
            lines_sqale = timemachine_metrics[['lines','ncloc','sqale_index']]

            complexity = timemachine_metrics[['complexity','class_complexity','file_complexity','function_complexity']]
            documentation = timemachine_metrics[['comment_lines','comment_lines_density']]
            duplications = timemachine_metrics[['duplicated_blocks','duplicated_files','duplicated_lines','duplicated_lines_density']]
            maintainability = timemachine_metrics[['code_smells','sqale_index','sqale_debt_ratio']]
            reliability = timemachine_metrics[['bugs','reliability_remediation_effort']]
            security = timemachine_metrics[['vulnerabilities','security_remediation_effort']]
            size = timemachine_metrics[['classes','directories','files','lines','ncloc','functions','statements']]

            plot(lines_sqale)
            plt.figure()
            plot(timemachine_metrics['normalized_td'])