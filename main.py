from selenium import webdriver
import bs4 as bs
import time
import os.path
from os import path
import pandas as pd 

#Starting the browser
browser = webdriver.Chrome('/home/Desktop/chromedriver') #change the path to the location of your driver

#Getting the source code
browser.get("https://www.youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe") #link to your playist

html_file = browser.page_source
time.sleep(2)


if path.exists("page_data.html"):
    f = open("page_data.html","w")
    f.write(html_file)
    
else:
    f = open("page_data.html","x") #this code will only create a file if a file with same name is NOT present in the directory
    f.write(html_file)
    
f.close

#closing the browser
browser.close()

with open('./page_data.html') as html_file:
    soup = bs.BeautifulSoup(html_file, 'lxml') #you might need to install lxml parser which can be done by "pip3 install lxml"

anchor_tag = soup.find_all('a', class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")#gets the list of all anchor tags

#At the time of writing this code the class gave me the desired output which might change as youtube keeps updating
#so it is suggested that you inspect the webpage and get the proper class if the code doesn't work

#print(anchor_tag)

"""data_list = []
name_list = []
url_list = []
for i in range(len(anchor_tag)):
    data_list.append(anchor_tag[i].attrs['aria-label'])
    url_list.append("https://www.youtube.com/"+anchor_tag[i].attrs['href'])
    name_list.append(anchor_tag[i].attrs['title'])"""

data = pd.DataFrame({"Name":[],"Url":[]})

for i in range(len(anchor_tag)):
    data = data.append({'Url': "https://www.youtube.com"+anchor_tag[i].attrs['href'],'Name': anchor_tag[i].attrs['title']}, ignore_index=True)   


#print(data_list)
#print(name_list)
#print(url_list)

#Writing the data in a text file
if path.exists("data.txt"):
    f1 = open("data.txt",'w')
    for i in range(len(anchor_tag)):
        f1.write("Name: " + str(anchor_tag[i].attrs['title']) + " Url:" + "https://www.youtube.com"+str(anchor_tag[i].attrs['href']) + " \n")
    f1.close
else:
    f1 = open("data.txt",'x')
    for i in range(len(anchor_tag)):
        f1.write("Name: " + str(anchor_tag[i].attrs['title']) + " Url:" +"https://www.youtube.com"+str(anchor_tag[i].attrs['href']) + " \n")
    f1.close

#df = pd.DataFrame(list(zip(name_list,url_list)), columns =['Name', 'Url'])
data.to_csv("./data.csv")
