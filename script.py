from bs4 import BeautifulSoup
import csv
import os

# Placer le script dans le meme repertoire que les fichiers d'historique
directory = os.path.dirname(os.path.realpath(__file__))

# Creation du tableau et des noms de colonnes
output_rows = []
output_rows.append(("Date", "Time", "Sender", "Message"))

for html_file in os.listdir(directory):
    filename = os.fsdecode(html_file)

    if filename.endswith(".html"):
        html = open(filename).read()
        soup = BeautifulSoup(html, features="html.parser")

        msgs = soup.findAll("div", {"class": "message default clearfix"})
        for msg in msgs:
            row = []

            # Date et heure
            time = msg.find("div", {"class": "pull_right date details"}).attrs["title"]
            date, time = time.split()
            row.extend((date, time))

            # Expediteur
            row.append(msg.find("div", {"class": "from_name"}).text.strip())

            # Message
            date_msg = msg.find("div", {"class": "text"}).text
            if ": " in date_msg:
                msg_alone = date_msg.split(": ")[1].strip()
            else:
                msg_alone = date_msg.strip()
            row.append(msg_alone)

            output_rows.append(row)

with open("output.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(output_rows)
