import struct
import os
import mysql.connector
import config
import time
import math
import csv
import json
from datetime import datetime


conn = mysql.connector.connect(host=config.host, user=config.user, password=config.password, database=config.database)
cursor = conn.cursor()


filename = config.filename

FileNumber = 0
tramecnt = 0
binarycursor = 0
arp = 0
udp = 0
liste_arp = []

def filesize(filename):
    return os.stat(filename).st_size


def size():
    with open(filename, 'rb') as f:
        global binarycursor
        localcursor = binarycursor + 24
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!I', data)[0]
        return data


def type():
    global arp
    global udp
    with open(filename, 'rb') as f:
        localcursor = binarycursor + 40
        f.seek(localcursor)
        data = f.read(2)
        if data == b'\x08\x00':
            udp += 1
            return "UDP"
        elif data == b'\x08\x06':
            arp += 1
            return "ARP"
        else:
            return "Ukn"
        

def ARP():
    global liste_arp
    global tramecnt
    global FileNumber

    with open(filename, 'rb') as f:
        #FrameDate
        localcursor = binarycursor + 8
        f.seek(localcursor)
        data = f.read(8)
        data = struct.unpack('!d', data)[0]
        FrameDate = data

        #Bench_3
        localcursor += 8
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!I', data)[0]
        # returns 3 values, we only want the second one
        Bench_3 = 1

        #Bench_5
        localcursor += 4
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!I', data)[0]
        Bench_5 = data

        #FrameSize
        localcursor += 4
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!I', data)[0]
        FrameSize = data

        #MAC_Dest
        localcursor += 4
        f.seek(localcursor)
        data = f.read(6)
        data = struct.unpack('!6B', data)
        #convert to MAC address
        data = ':'.join(format(x, '02x') for x in data)
        MAC_Dest = str(data)

        #MAC_Source
        localcursor += 6
        f.seek(localcursor)
        data = f.read(6)
        data = struct.unpack('!6B', data)
        #convert to MAC address
        data = ':'.join(format(x, '02x') for x in data)
        MAC_Source = str(data)

        #Field_1
        localcursor += 6
        f.seek(localcursor)
        data = f.read(2)
        data = struct.unpack('!H', data)[0]
        #convert to hex
        data = hex(data)
        Field_1 = str(data)
        
        #Field_2
        localcursor += 2
        f.seek(localcursor)
        data = f.read(2)
        data = struct.unpack('!H', data)[0]
        Field_2 = data
        
        #Field_3
        localcursor += 2
        f.seek(localcursor)
        data = f.read(2)
        data = struct.unpack('!H', data)[0]
        Field_3 = data

        #Field_4
        localcursor += 2
        f.seek(localcursor)
        data = f.read(1)
        data = struct.unpack('!B', data)[0]
        Field_4 = data

        #Field_5
        localcursor += 1
        f.seek(localcursor)
        data = f.read(1)
        data = struct.unpack('!B', data)[0]
        Field_5 = data

        #Field_6
        localcursor += 1
        f.seek(localcursor)
        data = f.read(2)
        data = struct.unpack('!H', data)[0]
        Field_6 = data

        #MAC_Sender
        localcursor += 2
        f.seek(localcursor)
        data = f.read(6)
        data = struct.unpack('!6B', data)
        #convert to MAC address
        data = ':'.join(format(x, '02x') for x in data)
        MAC_Sender = str(data)

        #IP_Sender
        localcursor += 6
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!4B', data)
        #convert to IP address
        data = '.'.join(map(str, data))
        IP_Sender = str(data)

        #MAC_Target
        localcursor += 4
        f.seek(localcursor)
        data = f.read(6)
        data = struct.unpack('!6B', data)
        #convert to MAC address
        data = ':'.join(format(x, '02x') for x in data)
        MAC_Target = str(data)

        #IP_Target
        localcursor += 6
        f.seek(localcursor)
        data = f.read(4)
        data = struct.unpack('!4B', data)
        #convert to IP address
        data = '.'.join(map(str, data))
        IP_Target = str(data)

        liste_arp.append((FileNumber, tramecnt, FrameDate, Bench_3, Bench_5, FrameSize, MAC_Dest, MAC_Source, Field_1, Field_2, Field_3, Field_4, Field_5, Field_6, MAC_Sender, IP_Sender, MAC_Target, IP_Target))



def UDP():
    global liste_udp
    with open(filename, 'rb') as f:
        localcursor = binarycursor + 8
        
        

def main():
    # Initialisation des variables
    timestart = time.time()
    global binarycursor
    global FileNumber
    global liste_arp
    global tramecnt
    tramecnt = 1
    liste = []

    # Récupération de la dernière valeur de FileNumber
    cursor.execute("SELECT MAX(FileNumber) FROM `frames`")
    FileNumber = int(cursor.fetchone()[0]) + 1

    # Calcul du temps d'exécution
    timefetch = round(time.time() - timestart, 2)
    print("Temps de récupération de la dernière valeur de FileNumber : ", timefetch, "secondes")
    timenext = time.time()

    # Lecture de la trame et insertion de l'index dans la bdd
    while binarycursor < filesize(filename):
        sizelocal = size()
        typelocal = type()
        tramecnt += 1
        liste.append((FileNumber, tramecnt, sizelocal, typelocal))
        if typelocal == "ARP":
            ARP()
        elif typelocal == "UDP":
            UDP()
        binarycursor += sizelocal + 28 #28 octets de header

    cursor.executemany("INSERT INTO `frames` (`FileNumber`, `FrameNumber`, `Size`, `Type`) VALUES (%s, %s, %s, %s)", liste)
    conn.commit()
    print("Trames index insérées avec succès")    
    
    cursor.executemany("INSERT INTO `arp` (`FileNumber`, `FrameNumber`, `FrameDate`,`Bench_3`, `Bench_5`, `FrameSize`, `MAC_Dest`, `MAC_Source`, `Field_1`, `Field_2`, `Field_3`, `Field_4`, `Field_5`, `Field_6`, `MAC_Sender`, `IP_Sender`, `MAC_Target`, `IP_Target`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", liste_arp)
    conn.commit()
    print("Trames ARP insérées avec succès")
  

    # Calcul du temps d'exécution
    timeinsert = round(time.time() - timenext, 2)
    print("Temps d'insertion des trames : ", timeinsert, "secondes")
    timetotal = round(time.time() - timestart, 2)
    print("Temps total d'execution : ", timetotal, "secondes")

main()
