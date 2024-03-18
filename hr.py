import os
from pydub import AudioSegment
from datetime import datetime, timedelta


def check():
    INPUT_FOLDER = "./Shz_1h"
    OUTPUT_FOLDER = "./Shz_in"
    DURATION = 5
    shzH = os.listdir(INPUT_FOLDER)
    for file in shzH:
        complete = file.split("_")

        name = complete[0]
        date = complete[1]
        time = complete[2].split(".")[0]
        ext = complete[2].split(".")[1]

        y, m, d = [int(i) for i in date.split("-")]
        h, mi, s = [int(i) for i in time.split("-")]

        delta = datetime(y, m, d, h, mi, s)

        audio = AudioSegment.from_file(f"{INPUT_FOLDER}/{file}")
        for i in range(0, int(audio.duration_seconds) * 1000, DURATION * 1000):
            segment = audio[i : i + DURATION * 1000]
            segment.export(
                f"{OUTPUT_FOLDER}/{name}_{delta.strftime('%Y-%m-%d_%H-%M-%S')}.{ext}",
                format="wav",
            )
            delta += timedelta(seconds=DURATION)
        os.remove(f"{INPUT_FOLDER}/{file}")
