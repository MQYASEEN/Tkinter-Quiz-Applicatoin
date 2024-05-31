import requests
parameters={
    "amount":20,
    "category":23,
    "type":'boolean',
        }
api=requests.get('https://opentdb.com/api.php',params=parameters)
api.raise_for_status()
response=api.json()

questions=response['results']
