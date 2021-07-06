import requests, uuid, json
import pandas as pd

final_list= []

# Add your subscription key and endpoint
subscription_key = "******************************"
endpoint = "https://api.cognitive.microsofttranslator.com/"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "centralindia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'te'
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


# You can pass more than one object in body.

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

df = pd.read_csv('data/FinalKB Telugu.csv')

for i in range(8776,len(df)):
    argument = df.iloc[i][30]
    body = [{
    'text': 'Hello!'
    }]
    if(argument != "NaN"):
        body[0]['text'] = str(argument)
    else:
        final_list.append('NaN')

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    final_list.append(response[0]['translations'][0]['text'])

    data = list(zip(final_list))
    df1 = pd.DataFrame(data,columns=['storyline'])
    df1.to_csv('bingtrivia1.csv')