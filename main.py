import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-u', '--url', nargs="?",
                    help="Bugs! album URL", required=True)
parser.add_argument('-r', '--resolution', nargs="?",
                    help="Artwork resolution override", default="3000")
args = parser.parse_args()

artwork_base_url = f'https://image.bugsm.co.kr/album/images/{args.resolution}'

album_url = args.url
album_id = album_url.split('/')[-1].split('?')[0]
id = album_id[0:-2]

artwork_url = f'{artwork_base_url}/{id}/{album_id}.jpg'
webbrowser.open(artwork_url, new=1)
