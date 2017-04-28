def print_project_stats(repos):
    for ghp in repos:
        timemachine_metrics = get_sonarqube_timemachine_metrics_DataFrame(ghp)
        timemachine_metrics = timemachine_metrics.fillna(method='ffill')
        timemachine_metrics = timemachine_metrics.fillna(0)
        timemachine_metrics = timemachine_metrics[timemachine_metrics.index.weekday==6]
        print(ghp.repo_id, ghp.repo, len(timemachine_metrics.index), timemachine_metrics['lines'].iloc[0],timemachine_metrics['ncloc'].iloc[0],timemachine_metrics['classes'].iloc[0], timemachine_metrics['lines'].iloc[-1],timemachine_metrics['ncloc'].iloc[-1],timemachine_metrics['classes'].iloc[-1])