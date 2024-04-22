import argparse
import os
from pytube import YouTube
import ffmpeg
import requests

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='Youtube link to Spotify converter',
                                     description='Uploads a youtube link to a spotify playlist')
    
    parser.add_argument('url', nargs='?')
    parser.add_argument('-n', '--name', help='save the url as the provided name')
    parser.add_argument('-f', '--file', help='accepts a text file of urls')

    return parser

def parse_file(filename) -> list:
    print("Parsing file...")
    urls = list()
    print("Validating urls...")

    with open(filename, "r") as file:
        for url in file.readlines():            
            if url != "" and validate_url(url):
                urls.append(url)
            else:
                print("Invalid url found in file: {url}")
        print("Parsing and Validation complete")

        return urls

def validate_url(url: str) -> bool:
    if url.find("youtube.com") != -1:
        return True
    return False

def create_downloads_folder() -> str:
    download_path = os.getcwd() + '/Song Downloads'
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    os.chdir(download_path)

    return download_path


def destroy_downloads_folder() -> None:
    # TODO: Fix removing nonempty directory
    os.rmdir(os.getcwd() + '/Song Downloads')

def set_thumbnail(filename: str, thumbnail_url: str) -> None:
    image_data = requests.get(thumbnail_url).content

    if image_data != None:
        print("Thumbnail found. Setting thumbnail...")
        thumbnail = filename.removesuffix('.mp4') + ".jpg"
        with open(thumbnail, "wb") as handler:
            handler.write(image_data)

        # TODO: Fix the thumbnail not being set
        video = ffmpeg.input(filename)
        cover = ffmpeg.input(thumbnail)
        (
            ffmpeg
            .output(video, cover, filename, c='copy', **{'c:v:1': 'jpg'}, **{'disposition:v:1': 'attached_pic'})
            .global_args('-map', '0')
            .global_args('-map', '1')
            .global_args('-loglevel', 'error')
            .run()
        )

def download_mp4(url: str, output_path: str, filename: str | None) -> None:
    # create a temp folder to store the mp4 files
    yt = YouTube(url)
    # TODO: play around with the on_progress_callback to show download progress


    if filename:
        filename += ".mp4"
    else:
        filename = yt.title + ".mp4"

    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    if audio:
        audio.download(output_path=output_path, filename=filename)
    else:
        print("No audio stream found for {url}.")

    if yt.thumbnail_url != None:
        set_thumbnail(filename, yt.thumbnail_url)

def main():
    parser = setup_parser()
    args = parser.parse_args()

    url = args.url
    name = args.name   
    downloads_path = create_downloads_folder()

    if args.file:
        urls = parse_file(args.file)
        for url in urls:
            download_mp4(url, output_path=downloads_path, filename=name)
    else:
        download_mp4(url, output_path=downloads_path, filename=name)



if __name__ == "__main__":
    main()