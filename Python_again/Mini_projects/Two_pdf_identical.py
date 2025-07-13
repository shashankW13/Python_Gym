import difflib
import hashlib
from difflib import SequenceMatcher

def hash_file(file1, file2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(file1, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h1.update(chunk)

    with open(file2, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file(r'E:\Python refresher\Python_again\Mini_projects\files\Hello_world_how.pdf',
                       r'E:\Python refresher\Python_again\Mini_projects\files\Hello_World.pdf')

if msg1 == msg2:
    print('equal')
else:
    print('not equal')
