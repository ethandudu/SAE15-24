import struct
import os
filename = '/home/sae/SAE24/Ethan/Vt_DEMO_power_on/ethernet.result_data'

binary_cursor = 0

def read_binary_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data


def type():
    with open(filename, 'rb') as f:
        global binary_cursor
        binary_cursor += 40
        f.seek(binary_cursor)
        data = f.read(2)
        type = "Unknown"
        if data == b'\x08\x00':
            type = "UDP"
        elif data == b'\x08\x06':
            type = "ARP"
        print("Type :", type)

def mac():
    with open(filename, 'rb') as f:
        f.seek(34)
        data = f.read(6)
        #convert to MAC address
        data = ':'.join('{:02x}'.format(x) for x in data)
        print("MAC Source :", data)


def size():
    with open(filename, 'rb') as f:
        f.seek(24)
        data = f.read(4)
        #convert to int
        data = struct.unpack('!I', data)[0]
        print("Size :", data)


def filesize(filename):
    return os.stat(filename).st_size

def main():
    mac()
    type()
    size()
    print("Taille du fichier :", filesize(filename)/1000000, "Moctets")


main()