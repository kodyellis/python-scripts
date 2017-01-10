#!/usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser , sys , clipboard
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # joins arguments enter
else:
    address = clipboard.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
