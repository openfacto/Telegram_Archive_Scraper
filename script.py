from bs4 import BeautifulSoup
import csv
import os
import argparse
import sys


def parse_html(filename):
    output_rows = []
    html = open(filename).read()
    soup = BeautifulSoup(html, features="html.parser")

    msgs = soup.findAll("div", {"class": "message default clearfix"})
    for msg in msgs:
        row = []

        # Date and time
        time = msg.find("div", {"class": "pull_right date details"}).attrs["title"]
        date, time = time.split()
        row.extend((date, time))

        # Sender
        row.append(msg.find("div", {"class": "from_name"}).text.strip())

        # Message
        msg_text = msg.find("div", {"class": "text"})
        if msg_text:
            row.append(msg_text.text.strip())
        else:
            # You have probably exported only text messages
            # and those where no text message is found are actually images, videos, etc. posted
            row.append("")

        output_rows.append(row)

    return output_rows



def main():
    parser = argparse.ArgumentParser(description="""A simple Python script to parse a Telegram archive and export it as a csv file.
By default, it takes the html files (Telegram archive) from the current directory.""")
    parser.add_argument("-f", "--file", help="Html file alone, contening the messages to scrap.")
    parser.add_argument("-d", "--directory", help="Directory containing the html files.")

    args = parser.parse_args()
    directory = ""
    filename  = ""
    
    # Location of the Telegram archive
    if args.directory:
        if os.path.isdir(args.directory):
            directory = args.directory
            if not directory.endswith('/'):
                directory = directory + '/'
        else:
            print("Parameter does not exist or is not a directory.")
            sys.exit()
    elif args.file:
        if os.path.isfile(args.file):
            filename = args.file
        else:
            print("Parameter does not exist or is not a file.")
            sys.exit()
    else:
        # If no agurment is supplied, use the current directory
        directory = os.path.dirname(os.path.realpath(__file__)) + '/'

    output_rows = []
    output_rows.append(("Date", "Time", "Sender", "Message"))

    if directory:
        for html_file in os.listdir(directory):
            filename = os.fsdecode(directory + html_file)
            if filename.endswith(".html"):
                rows = parse_html(filename)
                output_rows.extend(rows)
    elif filename:
        output_rows = parse_html(filename)

    with open("output.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(output_rows)


if __name__== "__main__":
    main()
