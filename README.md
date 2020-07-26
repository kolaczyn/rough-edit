# Rough Editor

## Description

It's a little program that I'm developing to help me make compilations a lot easier. It relies on subtitles which Youtube automatically generates.

## How it works

You give the program a phrase (or regex) and it then searches for it in the subtitles and based on that it generates and runs a script called ```rip.sh``` which compiles the relevant parts into one **folder** (folder, not file; it doesn't splice them).
User can then make a compilation video from the generated clips. There is no need to go through every single video and search for the relevant phrase.

## Installation

This application uses the following pieces of software:

* [Bash](https://www.gnu.org/software/bash/),
* [Python 3](https://www.python.org/),
* [youtube-dl](https://github.com/ytdl-org/youtube-dl/),
* [ffmpeg](https://ffmpeg.org/).

On e.g. Arch Linux you can download this application and install needed dependencies with the following commands:
```
sudo pacman -S --needed youtube-dl ffmpeg python
git clone https://github.com/kolaczyn/rough-edit.git
```
Linux and MacOS users obviously don't need to worry if you they have Bash.
If you're on Windows I recommend using [Git Bash](https://gitforwindows.org/). And don't forget to add the dependencies to your PATH.

## Included scripts

* ```download.sh``` — downloads both subtitles and videos of a Youtube playlist.
* ```convert.sh``` — converts the subtitles from ```.vtt``` to ```.srt```.
* ```gen-script.py``` — the main program, generates clips in which the searched phrase occurs.
* ```clean.sh``` — cleans up the **generated** files e.g. if you want to rerun the program. It doesn't delete the downloaded files.



## How to use it

1. Use ```bash download.sh``` to download subs and videos of a Youtube playlist. Usage example:
 ```bash download.sh https://www.youtube.com/playlist?list=PL-p5XmQHB_JQ5YQYI7zI1uVSepG-0UPL-```
 It puts subtitles into the ```../subs``` folder and footage into the ```.../original``` folder.

2. If the subtitles are in ```.vtt``` format, just run:
 ```bash convert.sh```
 This step is needed, because the program doesn't support other formats.

3. Use ```gen-script.py``` to generate relevant clips. Here's how you use that script:
    * The first argument you pass is the searched phrase, for example ```okay```. You can also use regex, but keep in mind that I'm using ```grep``` to find phrases, which doesn't support metacharacters like ```\w``` or ```\s``` are not supported.
    * The second argument is either ```fast``` or ```slow```. The ```fast``` takes less than five seconds to run, but the footage it generates is of bad quality: sound is not synchronized, image is missing, etc. The ```slow``` takes on my machine roughly 1 hour per 15 hours of footage, but the generated footage is perfect. I recommend first running first ```fast```, check if that's what you want to render, then in ```slow``` mode.
    * The third and the final argument tell how much padding you want around the searched phrase. Keep in mind that if you pass in ```5```, it doesn't mean there will be about 10 seconds. If you don't give the third argument, it uses a default value of 10 seconds.

4. That's it. Generated clips are inside ```../output``` folder. They are sorted in chronological order. You can start editing.
If you want to make another batch keep in mind that ```gen-script.py``` automatically runs ```clean.sh``` script which deletes the content of the ```output``` folder. It **doesn't** delete the original footage, subtitles and any of your other data. Or at least it should behave this way.

### Usage example

```
bash download.sh https://www.youtube.com/playlist?list=PL-p5XmQHB_JQ5YQYI7zI1uVSepG-0UPL-
bash convert.sh
python gen-script.py okay fast 5
# Now I check out the generated footage
# If I'm satisfied with the output, I use the slow mode
python  gen-script.py okay slow 5
```

## Limitations

Like I said, the program heavily relies on Youtube's auto-generated subtitles. So when the phrase you want to search for is not a word from a dictionary you have to find a workaround. You can find yourself moments when a Youtuber says the phrase and see how the subtitle generator interprets it. Keep in mind there can be a few ways the phrase is interpreted.
Let's say you want to search for a phrase 'hermitcaft'. The sub generator interprets it as 'hermit craft' and 'hermit crab'. So you could for example just search for the phrase 'hermit'. It's still better than nothing.

## Disclaimer

I am not a professional developer. The script here may be suboptimal or it may delete all of your unprotected files. You don't know what code a random person on the Internet wrote. So I recommend reviewing the source code before you run it. It's not very long, it's less than a 200 lines of code. 

## TODO list
* Add installation instructions for other Linux distros, MacOS and Windows.
* Make it so ```rough-editor``` istall itself in the PATH and you can e.g. type ```rough-editor Laughter fast 5``` in the terminal and it then runs the program on the current folder.
* Allow to specify quality of downloaded videos.
* Give an option to first download subtitles, search for the phrase and only download relevant videos from the playlist. Should be relatively easy.
* Stop using grep and switch to program which lets you utilize all of xegex magic.
* Make conversion faster; fix the slow method and make it fast and reliable.
* Make the program run differently if the files are .mp4 and .mkv. Don't remember why I wrote that.
* Handle situation if the subtitles don't exist but the corresponding video does.
* Search for other edge cases and fix them.