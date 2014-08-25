##coding=utf8
##Date  =2014-08-21
##Author=Sanhe


import os
import sqlite3
import datetime, time

def initial(fname):
    if os.path.exists(fname):
        conn = sqlite3.connect(fname)
        c = conn.cursor()
        cmd = \
        """
        CREATE TABLE death_records
        (
        ID TEXT PRIMARY KEY NOT NULL,
        lastname TEXT NOT NULL,
        firstname TEXT NOT NULL,
        dob DATE NOT NULL
        dod DATE NOT NULL
        location TEXT
        collection TEXT)
        """
    else:
        print '%s not exist' % fname

initial(fname)
