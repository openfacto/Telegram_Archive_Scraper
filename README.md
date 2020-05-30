# Telegram_Archive_Scraper

A simple Python script to parse a Telegram archive and export it as a csv file.

The following columns will be created : Date, Time, Sender, Message.
If the message contains only media (picture, video, cat GIF, etc.), the "Message" column will be empty for the corresponding row.

Source : https://openfacto.fr/2020/05/27/export-de-telegram-au-format-csv-introduction-a-beautifsoup/


## How to use

Export your Telegram conversation/group as an HTML file using the desktop version of Telegram.
https://desktop.telegram.org/

Note for Mac users : Do not use the "store" version of Telegram Version, but the official one.

This will create a bunch of html files in a directory.

Then run :
- ```python3 script.py``` to parse html files in the current directory.
- ```python3 script.py -d <path/to/your_directory>``` to parse files in another directory.
- ```python3 script.py -f <path/to/your_html_file>``` if you want to parse a specific file.

This will export the messages as a csv file.
