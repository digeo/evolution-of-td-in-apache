import requests
import json

def get_rest_response(rest_url):
    response = requests.get(rest_url)
    return json.loads(response.text)

def jsonDate_to_date(date):
    return datetime.datetime.fromtimestamp(date / 1e3)

def get_date(date):
    return pd.Timestamp(date).date()

def plot(plt):
    plt.plot(figsize=(15,10))