# Describe: Open default browser and search for an address

import webbrowser, sys, pyperclip

sys.argv

# check if command line arguments are passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://maps.google.com/maps?q='+  address)
