path = ''
import json


def toString(song_name):
  return f"{song_name}\ntimes listening to it:{player_data['songs'][song_name]['played']}\npopularity:{player_data['songs'][song_name]['popularity']}\n\n"




def biggest_area(areas,num):
    new_areas=areas.copy()
    list = []
    if new_areas != []:
        for w in range (num):
            mx = max(new_areas)
            for i in range (len(new_areas)):
                if new_areas[i]>-1:
                    if new_areas!=[]:
                            if new_areas[i] == mx:
                                new_areas[i]=-99
                                list.append(i)
    return (list)

#def min_dist()





#####################################
#1: general info
#2: mosts listened songs
#3: most popular songs
#4:
#5:
#########################################
while True:
    with open(path, 'r') as f:
        player_data = json.load(f)

    command = int(input ("type command:  "))
    if command ==1:
        count = 0
        c = 0
        for song in player_data['songs']:
            c += player_data['songs'][song]['played']
            count+=1

        time = player_data['total_length']

        hours = int(time / 3600)
        minutes = int((time % 3600) / 60)

        print(f" GENERAL INFORMATION\n listened to {c} songs,{count} different songs\n length of these songs: {hours}  hours  and {minutes} minutes\n ads:{player_data['ads']} (ads num is low because its a new feature)")


    if command==2:
        pops=[]
        song_names = []
        for song in player_data['songs']:

            pops.append(player_data['songs'][song]['played'])
            song_names.append(song)
        bigs = biggest_area(pops,5)
        for i in bigs:
            print (f"{song_names[i]}.     listening times:{pops[i]}")
    if command==3:
        pops=[]
        song_names = []
        for song in player_data['songs']:

            pops.append(player_data['songs'][song]['popularity'])
            song_names.append(song)
        bigs = biggest_area(pops,10)
        for i in bigs:
            print (f"{song_names[i]}. popularity:{pops[i]}")







