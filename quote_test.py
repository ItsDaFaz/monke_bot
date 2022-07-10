import requests


def randomQuote():
    quote_url="https://api.quotable.io/random"
    querystring = {"tags":"inspirational"}
    

   #quote_response=requests.request("GET", quote_url, headers=headers, params=querystring)
    quote_response=requests.request("GET", quote_url, params=querystring)
    quote_dict=quote_response.json()
    print(quote_dict['content'],quote_dict['author'])
    return quote_dict['content'],quote_dict['author']

print("kire bhai")
randomQuote()
