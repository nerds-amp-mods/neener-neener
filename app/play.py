import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# cid = '45f077e1ee63424abe797d5507a5c012'
# secret = 'a516d6de7f3f4231a8ac377fafdf1eaf'
# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp.start_playback('5d1025b96c84b06a125938304b8ec5f79ac70209',{"contet_uri":"spotify:playlist:4AhV6PWmFNXgN6BAa3LlSc"} )
# Generate New Access token.
headers = {"Accept": "application/json",
"Content-Type": "application/json",
"context_uri": "spotify:album:1Je1IMUlBXcx1Fz0WE7oPT",
"Authorization": "Bearer BQASP2HwH0RKPT-Hj8fNidRavMs03ZTxiDFT8xgKb0A-SqkRwYnBIfst0GE-ZOSHycZ156sucopGa7suLULXh2OT_Ns6zHaF_-yWL83G9K63QXsR8k0pw-EP4bVtOlELBnmzVS0ihEFESq2oGW-N4d0YNaH5rUjpyVTERDvbTEEF0q5I06Qh1xEzjpRq30xUDyIlrJ9eECUwuoIH1-lsdapLhsgWAifpmNhcJXP3c-MOsgMyPnyxyg7C1bbgNgo3Bg1UvQgUogLFinGWhK6LUVo7bhXGTGNTmp66"}

# Function returns json
def func_request(request_endpoint,headers):
    base_url = "https://api.spotify.com"
    req_json = (requests.get(base_url + request_endpoint, headers = headers)).json()
    return req_json

def func_request_put(request_endpoint,headers):
    base_url = "https://api.spotify.com"
    req_json = (requests.put(base_url + request_endpoint, headers = headers))
    return req_json


# Me
request_endpoint = "/v1/me"
req = func_request(request_endpoint,headers)
print(req['display_name'] + " is a " + req['product'] + " User")
print(req)

# User Devices
request_endpoint = "/v1/me/player/devices"
# req = func_request(request_endpoint,headers)
# print(req)

# User Toggle Play
request_endpoint = "/v1/me/player/play"
req = func_request_put(request_endpoint,headers)
print(req)









# device_data = r.json()['devices']
# for device in device_data:
#     headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer BQDGjVegqHUQuzyEa0WHw-o6VDieLi0s31UB4Ur_GS6skKGt1f_iFr57gHM2izmhRp3FLM6naNCI_HLVkHCnFwkorKXqX6zkDlJa9WbpgSy_wgQ86VfCXSh2RYQco-2Y6lkYGmiDXJ8_MHMs3Diefv2QrCeHGjGrYQ21NszruEPYoeSpC2DrASpQMH2Hn3_r9e2DmsUhF7vrphz2jlsmXQ7FCq_PPpWZOD99mLiZ7FgBhYci4Gr0S8hKRk5nEUZCTcf2qqYSye_iHpt7rrY6qiCLeWYgC0W_PQxG",
#     "context_uri": "spotify:playlist:31FWVQBp3WQydWLNhO0ACi",
#     "device_id" : device['id']
#     }
#     r = requests.put("https://api.spotify.com/v1/me/player/play", headers = headers)
#     print(r.json())
#     # sp.start_playback(device['id'], {"context_uri": "spotify:album:1Je1IMUlBXcx1Fz0WE7oPT"})

