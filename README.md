# YouTubePlaylistScrapper
The code web scarpes data from a youtube playlist and returns 3 files:
1. Html Page source code
2. data.txt with video name and url
3. data.csv with video name and url

## Dependencies
* Python 3.7
* Selenium 3.141.0
* Beautiful soup (bs4) 4.9.3
* Pandas 1.2.3

#### You will have to download driver for your respective browser and save it in the same folder as your code https://sites.google.com/a/chromium.org/chromedriver/downloads (for Google-chrome).

#### I did not use requests or urllib because it was not getting the proper html for the page.
#### To run the code you just need to download main.py and change the address  of your WebDriver and Youtube Playlist.
