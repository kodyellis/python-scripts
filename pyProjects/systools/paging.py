#/usr/bin/python3

def more (text, numlines=15):
    lines = text.spiltlines()
    chunk = lines[:numlines]
    lines = lines[numlines:]

