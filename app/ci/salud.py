import json
import time
from urllib.error import URLError
from urllib.request import urlopen


for intento in range(30):
    try:
        with urlopen("http://127.0.0.1:8000/salud", timeout=2) as respuesta:
            documento = json.load(respuesta)
        break
    except URLError:
        if intento == 29:
            raise
        time.sleep(1)
