from utils import *
from GitHubProject import *
import pandas as pd

# Functions for getting SonarQube timemachine metrics
def get_sonarqube_timemachine_metrics_DataFrame(ghp):
    json_data = get_sonarqube_timemachine_metrics(ghp)
    cells = get_cells(json_data)
    return transform_timemachine_metrics_to_series(cells)

def get_sonarqube_timemachine_metrics(ghp):
    return get_rest_response(ghp.timemachine_metrics_url + METRICS)

def get_cells(json_data):
    return json_data[0]['cells']  # cells - metric values

def get_colls(json_data):
    return json_data[0]['cols']  # cols - Metrcs

def get_no_of_versions(cells):
    return len(cells)

def transform_timemachine_metrics_to_series(cells):
    date_range_index = get_date_range_index_for_timemachine_metrics(cells)
    df = pd.DataFrame(index=date_range_index)
    for metric_index in range(0, metrics_list_length):
        s = pd.Series(index=date_range_index)
        for item in cells:
            s[pd.Timestamp(item.get('d')).date()] = item.get('v')[metric_index]
        df[METRICS_LIST[metric_index]] = s
    return df


def get_date_range_index_for_timemachine_metrics(cells):
    project_dates = get_project_dates(cells)
    min_project_date = min(project_dates)
    max_project_date = max(project_dates)
    return pd.date_range(start=min_project_date.date(), end=max_project_date.date(), freq='D')

def get_project_dates(cells):
    dates = []
    for item in cells:
        dates.append(pd.Timestamp(item.get('d')))
    return dates