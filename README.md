# BugsArtworkExtractor

Command line tool for extracting high resolution album art from [Bugs!](https://music.bugs.co.kr/), a Korean digital music platform.

## Requirements

* Python 3.7 (Recommended)

## Usage

Navigate to an album on Bugs! that you wish to extract album art for and copy the URL. Then use it in the following command:

```bash
python main.py -i 'https://music.bugs.co.kr/album/12345678'
```

## Example

```bash
python main.py -i 'https://music.bugs.co.kr/album/20291511'
```