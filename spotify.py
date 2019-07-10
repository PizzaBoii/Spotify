import requests
import json
import spotify_token as st
import time

add_one = False

path = # you need to create a json file
username = ''# username 
password= ''# password 
data = st.start_session(username, password)

print ("initiation program sequence ")
song_name="  " 
not_ad=True
def newSong(song_name):
    if song_name not in player_data['songs']:
        player_data['songs'][song_name]={}
        player_data['songs'][song_name]['played']=1
        player_data['songs'][song_name]['popularity']=json_data['item']['popularity']


def GetData(data):

    token = data[0]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,
    }


    return requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)


response = GetData(data)
protocol = response.status_code
text = (response.text)

if protocol == 200 and '"item" : null' not in text:
    json_data = (json.loads(response.text))
    song_name = json_data['item']['name']
counter = 0
song_c=0
while True:

    counter+=1
    if counter%50==0:
        data = st.start_session(username, password)



    with open(path, 'r') as f:
        player_data = json.load(f)

    response = GetData(data)
    protocol = response.status_code
    text =  (response.text)

    if '"item" : null' in text and not_ad:
        add_one=True
        not_ad=False
        print (f"this add is the {player_data['ads']} that you recieved ")


    if protocol==200 and '"item" : null' not in text:
        not_ad=True

        if add_one:
            player_data['ads']+=1
            add_one=False



        json_data = (json.loads(response.text))
        old_song=song_name
        song_name=json_data['item']['name']
        if old_song!=song_name:
            song_c+=1
            if song_name not in player_data['songs']:
                newSong(song_name)
            else:
                player_data['songs'][song_name]['played'] += 1
            song_length_sec= int(json_data['item']['duration_ms']/1000)
            player_data['total_length']+=song_length_sec
            print (f"{song_c}. length:{int (song_length_sec/60)}: {song_length_sec%60}, {song_name}")


            with open(path, "w") as write_file:
                json.dump(player_data, write_file)
                time.sleep(5)
