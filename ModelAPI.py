import requests
import json
import ssl, urllib
from PIL import Image
from io import BytesIO
import urllib.request 
from urllib.request import urlopen

url = "https://stablediffusionapi.com/api/v3/text2img"
url2 = "https://stablediffusionapi.com/api/v3/img2img"

payload = json.dumps({
    "key": "",
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
})

headers = {
    'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

obj = json.loads(response.text)

output = obj['output']

strout = str(output)

str = strout[2:]
str2 = str[:-2]
url = str2

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)


urllib.request.urlretrieve(url, "pornstar.png") 

img = Image.open(r"pornstar.png") 
img.show()