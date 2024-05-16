import argparse
import json
import typing
import hid

def getDevice():
    print()

def main():
    pid = 8217
    vid = 20785

    hid.enumerate()

    device = hid.Device(vid, pid)

    print(device)

main()