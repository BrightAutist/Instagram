# Instagram-Engagement

This Python script uses the Instagram API to scrape engagement data from a given user's Instagram account (public account, i.e. a celebrity). The script is run from the terminal in the editing program

Contents
- [Prerequisites](Prerequisites)
- [Usage](Usage)
- [Output](Output)

## Prerequisites
- Python 3.5 or higher installed
- Instaloader, to install type pip install instaloader within the terminal

## Usage
- In the script, replace the variables PROFILE_NAME with the desired Instagram username.
- You may set a limit to the number of posts you would like to view by setting the counter to 0 and the postcount to how ever many posts you would like to view.
- Once you have the username, you can run the script by executing the following command:
```Python
python scraping.py
```

## Output
The script will output a percentage of engagement per post within the terminal.
