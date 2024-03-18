import os
from time import sleep
import asyncio
from shazamio import Shazam
import json
from time import sleep
from database import insert, close


async def analize(file) -> dict:
    shazam = Shazam()
    out = await shazam.recognize(file)
    return out


def process():
    INPUT_FOLDER = "./Shz_in"
    OUTPUT_FOLDER = "./Shz_out"
    PROCESSED_FOLDER = "./Shz_processed"
    MARK = "_processed"

    shzIn = os.listdir(INPUT_FOLDER)

    for file in shzIn:
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(analize(f"{INPUT_FOLDER}/{file}"))
        jsonName = f"{file.split('.')[0]}.json"
        with open(f"{OUTPUT_FOLDER}/{jsonName}", "w") as f:
            f.write(json.dumps(r))
        complete = file.split("_")

        name = complete[0]
        date = complete[1]
        time = complete[2].split(".")[0]

        insert(name, f"{date} {time.replace('-', ':')}", jsonName)
        os.rename(
            f"{INPUT_FOLDER}/{file}",
            f"{PROCESSED_FOLDER}/{file.split('.')[0]}{MARK}.{file.split('.')[1]}",
        )
        sleep(2.9)
    close()
