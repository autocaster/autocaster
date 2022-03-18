import subprocess
import random
import feedparser
import time as time_
import platform
from datetime import datetime, time
import pafy
from yt_dlp import YoutubeDL

ydl = YoutubeDL()

pafy.set_api_key ('AIzaSyCCpocnShcxNns_5nTFV-8tn5X9igz8_9k') ## Api key is needed for working with long playlists. If 15 last videos from each playlist is enough - api key is not required.

checkos = []
if (platform.system() == 'Linux'):
    checkos.append('Linux')
if (platform.system() == 'Windows'):
    checkos.append('Windows')

watched = []

watched_stream = []

def clear_watched_stream():
    del watched_stream[:]

## All channels and playlists are taken as an example. All external content, trademarks, service marks and company names are the property of their respective owners.

def youtuberss():
    try:
        ## Get last 15 videos via RSS from a YouTube channel or playlist. The link should point at .xml rss feed with playlist id at url parameters.
        ## A playlist with all channel uploads has UU at the begining, and the rest is part of a unique channel url).
        youtuberss1 = [
            'https://www.youtube.com/feeds/videos.xml?playlist_id=UUkRfArvrzheW2E7b6SVT7vQ', ## [Youtube Creators channel] all uploads playlist
            'https://www.youtube.com/feeds/videos.xml?playlist_id=PL590L5WQmH8cKGiSwITbQ7YQTNJz_eUJv', ## [Inventors @ Google] playlist at [Google channel]
            ]

        youtuberss1_feeds = []
        for url in youtuberss1:
            youtuberss1_feeds.append(feedparser.parse(url))

        youtuberss1_links = []
        for feed in youtuberss1_feeds:
            for post in feed.entries:
                ## Select videos that are no more than 50 days old
                if time_.time() - time_.mktime(post.published_parsed) < (86400*50) and \
                   (post.link) not in watched: ## Check if a video was already watched on this script run
                    youtuberss1_links.append(post.link)

        youtuberss2 = [
            'https://www.youtube.com/feeds/videos.xml?playlist_id=UU9M7-jzdU8CVrQo1JwmIdWA', ## [Android channel] all uploads playlist
            ]
        
        youtuberss2_feeds = []
        for url in youtuberss2:
            youtuberss2_feeds.append(feedparser.parse(url))

        youtuberss2_links = []
        for feed in youtuberss2_feeds:
            for post in feed.entries:
                ## Search for specific title(s) of a video to play and videos that are not older than 44 days old
                if (('Shorts').lower() in str(post.title).lower() or \
                    ('TV').lower() in str(post.title).lower()) and \
                    time_.time() - time_.mktime(post.published_parsed) < (86400*44) and \
                    (post.link) not in watched:
                        youtuberss2_links.append(post.link)

        youtuberss_all = []
        youtuberss_all.extend(youtuberss1_links)
        youtuberss_all.extend(youtuberss2_links)

        for i in youtuberss_all:
            if i in watched or \
               i in watched_stream:
                youtuberss_all.remove(i)

        if youtuberss_all:
            try:
                ytrandomlink = random.choice(youtuberss_all)
                if 'Linux' in checkos:
                    r = ydl.extract_info(ytrandomlink, download=False)
                    pafyrandomlink = [f['url'] for f in r['formats'] if f['format_id'] == '22']
                    pafyrandomlink = str(pafyrandomlink)
                    char_to_replace = {"['": "",
                                       "']": ""}
                    for key, value in char_to_replace.items():
                        pafyrandomlink = pafyrandomlink.replace(key, value)
##                    ## In case if this script is being launched in a Linux environment that is not compatible with yt_dlp module (for example, ARMv6), you can try to use a remote server with yt-dlp installed and use it as a command line tool and collect it's output as shown in the commented out section below (the chunk above should be replaced if this one is in use).
##                    command = 'ssh -i /home/pi/.ssh/serverkey.pem ec2-user@192.168.1.2 ~/.local/bin/yt-dlp --get-url -f "(mp4)[height<=720]" ' + ytrandomlink
##                    args = command.split(' ')
##                    getytdlplink = subprocess.Popen(args, stdout=subprocess.PIPE,universal_newlines=True)
##                    time_.sleep(3)
##                    pafyrandomlink = set(getytdlplink.stdout)
##                    pafyrandomlink = str(pafyrandomlink)
##                    char_to_replace = {"set([": "",
##                                       "\\n": "",
##                                       "{": "",
##                                       "\\": "",
##                                       "}": "",
##                                       "])": ""}
##                    for key, value in char_to_replace.items():
##                        pafyrandomlink = pafyrandomlink.replace(key, value)
                if 'Windows' in checkos:
                    r = ydl.extract_info(ytrandomlink, download=False)
                    pafyrandomlink = [f['url'] for f in r['formats'] if f['format_id'] == '22']
                    pafyrandomlink = str(pafyrandomlink)
                    char_to_replace = {"['": "",
                                       "']": ""}
                    for key, value in char_to_replace.items():
                        pafyrandomlink = pafyrandomlink.replace(key, value)
                if 'm3u8' in str(pafyrandomlink): ## Adding a video that is not yet in mp4 format (being streamed on a channel or being converted) to a temporarily ignored list
                    watched_stream.append(ytrandomlink)
                    youtuberss_all.remove(ytrandomlink)
                    None
                else:
                    if 'Linux' in checkos:
                        play = subprocess.Popen(['sudo', 'omxplayer', str(pafyrandomlink)])
                    if 'Windows' in checkos:
                        play = subprocess.Popen(["c:\Program Files\MPC-HC\mpc-hc64.exe", str(pafyrandomlink)])
                    watched.append(ytrandomlink)
                    youtuberss_all.remove(ytrandomlink)
                    play.wait()
            except:
                watched_stream.append(ytrandomlink)
                None
    except:
        pass

def youtubeapi():
    try:
        ## Selecting random video from a playlist using youtube api and pafy module. Each playlist should not contain more than ~1200 videos. If there are more, parsing will fail.
        ## In this case direct playlist url is used as in a browser.
        youtubeapi1 = [
            'https://www.youtube.com/playlist?list=UUWIzrKzN4KY6BPU8hsk880Q', ## [Life at Google] all uploads
            ]
        plurl = random.choice(youtubeapi1)
        playlist = pafy.get_playlist2(plurl)
        print(len(playlist))
        for item in range(len(playlist)):
            ytrandomitem = random.choice(range(len(playlist)))
            print(ytrandomitem)
            pafyrandid = playlist[ytrandomitem].videoid
            pafyrandid = "https://www.youtube.com/watch?v=" + pafyrandid
            print(pafyrandid)
            if (pafyrandid) not in watched:
                if 'Linux' in checkos:
                    r = ydl.extract_info(pafyrandid, download=False)
                    pafyrandomlink = [f['url'] for f in r['formats'] if f['format_id'] == '22']
                    pafyrandomlink = str(pafyrandomlink)
                    char_to_replace = {"['": "",
                                       "']": ""}
                    for key, value in char_to_replace.items():
                        pafyrandomlink = pafyrandomlink.replace(key, value)
                if 'Windows' in checkos:
                    r = ydl.extract_info(pafyrandid, download=False)
                    pafyrandomlink = [f['url'] for f in r['formats'] if f['format_id'] == '22']
                    pafyrandomlink = str(pafyrandomlink)
                    char_to_replace = {"['": "",
                                       "']": ""}
                    for key, value in char_to_replace.items():
                        pafyrandomlink = pafyrandomlink.replace(key, value)
                if 'Linux' in checkos:
                    play = subprocess.Popen(['sudo', 'omxplayer', str(pafyrandomlink)])
                if 'Windows' in checkos:
                    play = subprocess.Popen(["c:\Program Files\MPC-HC\mpc-hc64.exe", str(pafyrandomlink)])
                watched.append(pafyrandid)
                play.wait()
                return
            else:
                None
    except:
        pass

while 1 != 0:
    try:
        ## Loop for checking fresh videos and playing them
        while 1 != 0:
                if time(12,1) <= datetime.now().time() <= time(13,1) or \
                   time(15,1) <= datetime.now().time() <= time(16,1) or \
                   time(18,1) <= datetime.now().time() <= time(19,1) or \
                   time(21,1) <= datetime.now().time() <= time(22,1):
                    clear_watched_stream() ## Clearing the list of videos that were temporarily denied from playing because of not being converted to mp4 format by YouTube at the time of initial access. 
                youtuberss()
                print ('youtubeRSS ok')
                youtubeapi()
                print ('youtubeAPI ok')
    except:
        None
