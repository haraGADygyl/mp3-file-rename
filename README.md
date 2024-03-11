# MP3 File Renamer

This Python script is designed to rename MP3 files in a directory based on their metadata using the [eyed3](https://github.com/nicfit/eyeD3) library.

## Requirements

Ensure you have the required Python packages installed by running:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the `main.py` script.
2. Navigate to the directory containing the script.
3. Run the script with Python:

```bash
python main.py
```

Make sure to replace `target_directory` in the script with the path to the directory containing your MP3 files.

## Notes

- This script uses the `eyed3` library to load and manipulate MP3 file metadata.
- It renames the files based on the artist, track number, and song name metadata.
- Invalid characters in the metadata will be removed from the filenames.
- The output format is set to `<artist> - <track number> - <track name>`

## License

This project is licensed under the [MIT License](LICENSE).
