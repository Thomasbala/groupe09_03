import datetime

type_event = input("Type d'événement : ")
description = input("Description : ")
now = datetime.datetime.now()
log_entry = f"[{now}] - {type_event}: {description}\n"

with open("logs.txt", "a") as f:
    f.write(log_entry)
print("Événement journalisé dans logs.txt")