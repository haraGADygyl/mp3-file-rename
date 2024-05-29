import os
import re
import eyed3


def rename_mp3_files(directory):
    # Get a list of all MP3 files in the directory
    mp3_files = [f for f in os.listdir(directory) if f.endswith(".mp3")]

    for mp3_file in mp3_files:
        file_path = os.path.join(directory, mp3_file)

        # Load metadata using eyed3
        audiofile = eyed3.load(file_path)

        if audiofile.tag:
            artist = audiofile.tag.artist
            track_title = audiofile.tag.title
            track_number = audiofile.tag.track_num[0] if audiofile.tag.track_num else ""

            # Remove any invalid characters from the filename
            artist = re.sub(r'[\\/*?:"<>|]', "", artist)
            track_title = re.sub(r'[\\/*?:"<>|]', "", track_title)
            track_number = re.sub(r'[\\/*?:"<>|]', "", str(track_number).zfill(2))

            # Rename the file
            new_filename = f"{artist.title()} - {track_number} - {track_title}.mp3"
            new_file_path = os.path.join(directory, new_filename)

            os.rename(file_path, new_file_path)
            print(f"Renamed '{mp3_file}' to '{new_filename}'")


if __name__ == "__main__":
    target_directory = ""
    rename_mp3_files(target_directory)
