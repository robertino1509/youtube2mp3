# youtube2mp3
Small script in python that download and extract mp3 from youtube

## Getting Started and requirement

1. Install python in your system [https://www.python.org/](https://www.python.org/)

Es: in Linux debian system:
```
sudo apt-get install python3
```
2. Dowload and install youtube-dl [https://rg3.github.io/youtube-dl/download.html](https://rg3.github.io/youtube-dl/download.html)

Es: in UNIX system:
```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl
```

### Installing

1. Copy youtube2mp3.py in your system. 
2. Edit youtube2mp3.py and chage "URL_DESTINATION" (line 7) with your default destination (es: "/home/pi/mp3/").
3. Save.

## Running

```
./youtube2mp3.py url_video
```
Where "url_video" is the youtube video

youtube2mp3.py support multiple url video and/or multiple list video

Es. multiple video :

```
./youtube2mp3.py url_video1 url_video2 url_video3 url_video4
```
Es. multiple list:

```
./youtube2mp3.py url_list_video1 url_list_video2 url_list_video3 url_list_video4
```

## Authors

Roberto Aiello [www.robertoaiello.net](http://www.robertoaiello.net/)

youtube-dl is released into the public domain by the copyright holders [https://github.com/rg3/youtube-dl](https://github.com/rg3/youtube-dl)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
