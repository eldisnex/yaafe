from time import sleep
from s import process
from hr import check
import os

if not os.path.isdir("Shz_1h"):
    os.mkdir("Shz_1h")
if not os.path.isdir("Shz_in"):
    os.mkdir("Shz_in")
if not os.path.isdir("Shz_out"):
    os.mkdir("Shz_out")
if not os.path.isdir("Shz_processed"):
    os.mkdir("Shz_processed")

while True:
    check()
    process()
    sleep(1)
