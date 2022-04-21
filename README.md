# Chapters Converter
Convert Adobe Premiere Chapter Markers into YouTube Timestamps
This will take in chapter marker TXT files exported from Adobe Premiere and convert them into a YouTube descritpion friendly format.

## Development Guide
### Running the source code directly
1. Install Python 3.4 or newer
2. In a console window, run either:<br>
    - `pip install -r requirements`<br>
or<br>
    - `python -m pip install -r requirements`
4. Either:<br>
    - Double-click on the `main.py` file to open it if Python is your default handler for `*.py` files
    - Right-click and do `Open with`and select `Python`
    - In your console window, type `python main.py` and hit enter
5. Select all the TXT files you want converted. You have to select them all at once, as the old selection will get removed. You can also write the paths to the files inside the text box (entries should be separated by a semi-colon).
6. Hit the `Start` button and you're done!

1. Install Python 3.4 or newer
2. In a console window, run either:<br>
    - `pip install -r requirements`<br>
or<br>
    - `python -m pip install -r requirements`
3. Iinstall `pyinstaller` with either:<br>
    - `pip install pyinstaller`<br>
or<br>
    - `python -m pip install pyinstaller`<br>
4. Build the app with the following command: `pyinstaller -y --dist src/out --clean -F -n Chapter_Converter --noconsole src/main.py`
5. Run the executable as you would for your given operating system. The executable will be found in `src/out/`
6. Select all the TXT files you want converted. You have to select them all at once, as the old selection will get removed. You can also write the paths to the files inside the text box (entries should be separated by a semi-colon).
7. Hit the `Start` button and you're done!