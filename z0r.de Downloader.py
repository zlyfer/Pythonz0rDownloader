# If modules not found use following in console:
# pip install requests
# pip install os

import requests
import os

def user_exit():
    input("Press any key to exit.")
    exit()

def download(filename):
    if os.path.exists('z0r/%s.swf' % filename):
        return (['Skip'])
    file = open('z0r/' + filename + '.swf', 'wb')
    link = 'http://z0r.de/L/z0r-de_'
    image = requests.get(link + filename + '.swf').content
    file.write(image)
    file.close()
    if os.path.exists('z0r/%s.swf' % filename):
        filesize = os.path.getsize('z0r/%s.swf' % filename)
        if filesize < 5000:
            os.remove('z0r/%s.swf' % filename)
            return (['End'])
        return (['Success', filesize // 1000])
    else:
        return (['Error'])

if not os.path.exists('z0r'):
    print ("Creating folder 'z0r'.")
    os.mkdir('z0r')
    if not os.path.exists('z0r'):
        print ("Failed creating folder 'z0r'.")
        user_exit()
    else:
        print ("Folder 'z0r' created.")

file = 0
tried = 0
msg = [0]
while tried < 3:
    msg = download("%s" % file)
    if msg[0] == "End":
        tried += 1
        print ("x %s: (%s/3)" % (file, tried))
    elif msg[0] == "Success":
        tried = 0
        print ("+ %s: %s KB." % (file, msg[1]))
    elif msg[0] == "Skip":
        tried = 0
        print ("~ %s" % file)
    file += 1

print ("\nDone.")
user_exit()