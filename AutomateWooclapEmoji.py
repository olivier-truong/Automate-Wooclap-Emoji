import requests, json, time
from random import randbytes, choice
from sys import argv
from threading import Thread

class Emoji:

    like = "👍"
    hearth = "❤️"
    fire = "🔥"
    omg = "😯"
    cotillons = "🎉"

    def random():
        return choice(["👍", "❤️", "🔥", "😯", "🎉"])

    names = {
            "like": like,
            "hearth": hearth,
            "fire": fire,
            "omg": omg,
            "cotillons": cotillons,
            "random": random
    }

    def get(name: str) -> any:
        if name in Emoji.names:
            return Emoji.names[name]
        else:
            return random

    def exists(name: str) -> str | None:
        return name in Emoji.names


global _spam
_spam = True

def generateToken():
    return "".join(str(x % 10) for x in randbytes(12))


def getRandomUag():
    return choice([{"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.3", "pct": 63.11}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Mobile/15E148 Safari/604.", "pct": 8.25}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/360.1.737798518 Mobile/15E148 Safari/604.", "pct": 5.83}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/134.0.6998.99 Mobile/15E148 Safari/604.", "pct": 4.85}, {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/27.0 Chrome/125.0.0.0 Mobile Safari/537.3", "pct": 3.88}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.", "pct": 3.4}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.", "pct": 1.94}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Mobile/15E148 Safari/604.", "pct": 1.94}, {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.3", "pct": 1.46}, {"ua": "Mozilla/5.0 (Android 14; Mobile; rv:136.0) Gecko/136.0 Firefox/136.", "pct": 0.97}, {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.3", "pct": 0.97}, {"ua": "Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.15.0.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/15.0.4.312 Mobile Safari/537.3", "pct": 0.97}, {"ua": "Mozilla/5.0 (Android 15; Mobile; rv:136.0) Gecko/136.0 Firefox/136.", "pct": 0.49}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e YisouSpider/5.0 Safari/602.", "pct": 0.49}, {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.", "pct": 0.49}, {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.3", "pct": 0.49}, {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3", "pct": 0.49}] + [{"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.10 Safari/605.1.1", "pct": 43.03}, {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3", "pct": 21.05}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3", "pct": 17.34}, {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3", "pct": 3.72}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Trailer/93.3.8652.5", "pct": 2.48}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.", "pct": 2.48}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.", "pct": 2.48}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.", "pct": 2.48}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.", "pct": 1.24}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.1958", "pct": 1.24}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.", "pct": 1.24}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.3", "pct": 1.24}])["ua"]



def getEvIdByName(name: str, u_ag: str, token: str):
    r = requests.get(f"https://app.wooclap.com/api/presentation/events/{name}/authentications", headers={"User-Agent": u_ag, "Authorization": f"bearer z{token}", "Cookie": 'wc__cookie-consent={"functionality":false,"performance":false,"tracking":false}'})

    return r.json().get("_id")

def postParticipants(ev_id: str, u_ag: str, token: str):
    r = requests.post(f"https://app.wooclap.com/api/presentation/events/{ev_id}/participants", headers={"User-Agent": u_ag, "Authorization": f"bearer z{token}", "Cookie": 'wc__cookie-consent={"functionality":false,"performance":false,"tracking":false}'}, json={"origin":"banner"})

    return (r, r.headers, r.text)

def lacheUnEmoji(ev_id: str, u_ag: str, token: str, emoji: str):
    r = requests.post(f"https://app.wooclap.com/api/presentation/events/{ev_id}/reactions", json={"emoji": emoji}, headers={"User-Agent": u_ag, "Authorization": f"bearer z{token}"})
    return (r, r.headers, r.text)



def spamWithOneParticipant(name: str, emoji: any, worker_id = "XY", sleepTime = 0.55):
    global _spam
    if name.startswith("https"):
        # https://app.wooclap.com/<Name>?from=instruction-slide
        name = name.split("/")[3].split("?")[0]
    token = generateToken()
    head = f"[WORKER n°{worker_id}] "
    print(head, "Token:", token)

    u_ag = getRandomUag()
    print(head, "User-Agent:", u_ag)

    ev_id = getEvIdByName(
        name, u_ag,
        token
    )
    print(head, "Event_Id:", ev_id)

    print(
        head, "Register new participant:",
        postParticipants(ev_id, u_ag, token)[0]
    )

    while _spam:

        if type(emoji) == str:
            print(head, lacheUnEmoji(ev_id, u_ag, token, emoji)[0], f"           (emoji = {emoji})")
        else:
            rEmoji = emoji()
            print(head, lacheUnEmoji(ev_id, u_ag, token, rEmoji)[0], f"           (emoji = {rEmoji})")
        time.sleep(sleepTime)

def spamRandom(name: str, nTh = 2, creationSleepTime = 0.2):
    ths = []

    for i in range(nTh):
        ths.append(Thread(target=spamWithOneParticipant, args=(name, Emoji.random, i,)))
        ths[-1].start()

        time.sleep(creationSleepTime)

if __name__ == '__main__':
    spamRandom(input("Event Name / Link >/ "), int(input("Number of Thread(s) >/ ")))
