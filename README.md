# Facebook Messages Counter 📘📩

## What's that?
A simple program for counting messages sent via Facebook.
The program automatically counts messages in private and group conversations and sorts them by the number of all messages sent. It runs locally and does not connect to the network. **It does not collect any data, it only creates a txt report, which is saved only in the place selected by the user**.

## How to use?

For the program to count your messages, you need to download your data from Facebook. To do this you need to:

### Downloading data
1. Click on your avatar in the upper right corner on Facebook.
2. "Settings and privacy"
3. "Settings"
4. From the left panel, select "Download information"
5. "Request file for download"
6. Select the account whose data you are interested in
7. Now you can choose what types of data you want to download. At the current level of application development, it is recommended to download only messages from the entire period, with low multimedia quality (shortest waiting time).
8. **Be sure to select the JSON format.**
9. Once you have downloaded all the zip archives, merge them into one folder.

### Running app
1. Select the folder from which messages are to be counted (inbox by default).
2. Select where you want to save your txt report.
3. Enter your name and surname used on Facebook (the program will be able to provide you with more detailed statistics).

## Requirements to run directly with Python:
- Python 3.12.1
- PyQt5 5.15.10

Created and tested on these versions, it is possible that it works on older ones.

If you have any questions, feel free to ask.

## Plan for upcoming improvements:
- more detailed statistics such as the number of words and characters
- sorting according to messages sent in a given period
- counting photos, videos, gifs, etc.