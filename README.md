# About Autocaster

This script is for sequential, seamless, looped playback of Youtube or any other web-hosted videos parsed and fetched from any amount of user selected channels, including RSS sources.

Autocaster will remember played videos and won't repeat itself.

User can select how old/recent videos should be. Filtering by video title is also available.

Currently supported platforms: Windows, Linux.

This is a very early stage of development. Features to be added:
 * A proper configurator with UI
 * Support for Android and Mac
 * Text-to-speech and/or audio playback with images with generic animation (for enriching textual content to play in 'TV emulation' scenario)


# Installation and Use

## Linux:

### 1) Install Python modules:

apt-get install python3-feedparser

pip3 install youtube-dl

apt-get install python3-pafy

pip3 install yt-dlp

### 2) Add/edit channels according to your needs and launch the script


## Windows:

### 1) Python and modules:

Download and install Python:
https://www.python.org/downloads/release/python-3103/

Go to c:\Users\ %username% \AppData\Local\Programs\Python\Python310\Scripts\ with Windows command line and execute the following:

pip install feedparser

pip install youtube-dl

pip install pafy

pip install yt-dlp


### 2) Video player:

Download MPC-HC player: https://github.com/mpc-hc/mpc-hc/releases/tag/1.7.13

To achieve seamless experience whith MPC-HC player it should be set to close itself after a video playback is over:

View -> Options -> Playback -> After playback -> select 'Exit' at dropdown menu -> OK

And also for better viewing experience:

View -> Options -> Playback -> Fullscreen -> Launch files in fullscreen

### 3) Add/edit channels according to your needs and launch the script

You may want to open it by right clicking on the script file and selecting 'Edit with IDLE' than edit it and launch using F5 keyboard button.

<!--
**autocaster/autocaster** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
