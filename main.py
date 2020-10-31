import os
import feedparser
import qbittorrentapi

PIRATE_BAY_BASE_URL = 'https://www.pirate-bay.net/search?q='
SEARCH_STRING = 'discovery'
TPB_RSS = 'https://tpb.party/rss/top100/205'
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def main():
    d = feedparser.parse(TPB_RSS)
    entries = d['entries']
    for entry in entries:
        if SEARCH_STRING in entry.title.lower():
            print(f'The downloaded title is: {entry.title}')
            print(f'The download link is: {entry.link}')

            qbt_client = qbittorrentapi.Client(host=HOST, port=PORT,
                                               username=USERNAME, password=PASSWORD)
            try:
                qbt_client.auth_log_in()
            except qbittorrentapi.LoginFailed as e:
                print(e)

            print(f'qBittorrent: {qbt_client.app.version}')
            print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')

            save_path = '/mnt/mydisk/HD/TempDownloads/torrent_1.torrent'
            qbt_client.torrents_add(urls=entry.link, save_path=save_path)


if __name__ == "__main__":
    main()
