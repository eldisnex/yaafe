from time import sleep
from s import process
from hr import check

while True:
    check()
    process()
    sleep(1)
