import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil
import cgi

serviceAccountKey = '../../labo2-nickboon-23-firebase-adminsdk-3gyi0-c3a166f0f9.json'
databaseURL = 'https://labo2-nickboon-23.firebaseio.com'


try:
    # Fetch the service account key JSON file contents
    firebase_cred = credentials.Certificate(serviceAccountKey)

    # Initalize the app with a service account; granting admin privileges
    firebase_admin.initialize_app(firebase_cred, {
    'databaseURL': databaseURL
    })

    # As an admin, the app has access to read and write all data
    firebase_ref_cols = db.reference('cols')
    firebase_ref_rows = db.reference('rows')
    firebase_ref_arcade_characters = db.reference('current_character')
except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# constants
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# transform pattern to matrix
def pattern_to_matrix(pattern):
  matrix = []
  for p in range(0,64):
        bit = int(pattern[p])
        color = COLOR_BLUE if bit == 1 else COLOR_BLACK
        matrix.append(color)
  return(matrix)

def cb(self):
  current_pattern = firebase_ref_arcade_characters.get()
  current_matrix = pattern_to_matrix(current_pattern)
  sense_hat.set_pixels(current_matrix)

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main(pattern):
  firebase_ref_arcade_characters.listen(cb)
  while True:
    pattern_to_matrix(pattern)
    sleep(20)
        
if __name__ == "__main__":
    try:
        pattern = firebase_ref_arcade_characters.get()
        main(pattern)
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sense_hat.clear()
        sys.exit(0)