# cli-yt-downloader
A little code snippet I made for personal use. Allows the user to download Youtube videos through the command line. 

# Features
- Download on highest or lowest resolution allowed by the PyTube library
- Download only audio

# Dependencies and usage
- This app uses both the PyTube3 and PyFiglet external libraries, altough the latter is not really necessary.
- If for some reason you're using this and don't want to use PyFiglet, you can comment lines 9 and 52. Otherwise:

```
pip install pytube3 pyfiglet
```

- You can start the app by using:
```
cd cli-yt-downloader
cd src
python CLI_Downloader.py
```

- Supported command line arguments:
```
-l: switches to lowest quality mode.
-a: switches to audio mode (only the audio is downloaded as a mp4 file);
```

# Screenshot
<p align="center">
      <img width="544" height="416" src="https://i.imgur.com/9gFyxSZ.png"><br></br>
</p>
