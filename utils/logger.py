from datetime import datetime

def log(message):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")