import giphy_client as gc
from giphy_client.rest import ApiException
from dotenv import load_dotenv
import os
from random import randint





load_dotenv()


api_instance = gc.DefaultApi()
api_key = os.getenv('GIPHY_KEY')
query = 'monkey'
fmt = 'gif'

try:
    response = api_instance.gifs_search_get(api_key,query,limit=1,offset=randint(1,10),fmt=fmt)
    gif_id = response.data[0]
    print(gif_id)
    #print(type(gif_id))
    gif_url = gif_id.images.downsized.url
    #print(gif_url)
    print(gif_id.text)
except ApiException:
    print("Exception when calling DefaultApi->gifs_search_get: ")
