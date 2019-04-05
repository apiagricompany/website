import sys
import requests
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime
import locale

def feeder(feed_url, theme_path):
    feed_content = requests.get(feed_url)
    feed = feedparser.parse(feed_content.text)
    num_entries = len(feed.entries)
    if num_entries > 0:
        file_path = "{}/templates/feeds.html".format(theme_path)

        with open(file_path, 'w+') as file:
            for i in range(0,min(3, num_entries)):
                post = feed.entries[i]
                #soup = BeautifulSoup(post.content[0].value, 'html.parser')
                #image_url = soup.find('img')['src']
                published_date =datetime.strptime(post.published, '%a, %d %b %Y %H:%M:%S %z')
                lc = locale.getlocale()
                locale.setlocale(locale.LC_ALL, 'pt_BR')
                html ='''
                    <article class="column is-4">
                    <a href="{0}" target="_blank"><div class="card">
                        <header  class="card-header">
                            <p class="card-header-title is-centered is-size-5">{1}</p>
                        </header>
                        <div class="card-content">
                            <div class="content">
                                <p class="is-size-6 has-text-justified">{2}</p>
                            </div>
                        </div>
                        <footer class="card-footer">
                            <p class="subtitle is-7 card-footer-item"><time datetime="{3}">{4}</time></p>
                        </footer>
                    </div></a>
                    </article>'''.format(post.link, post.title, post.summary, published_date.strftime('%Y-%m-%d'), published_date.strftime('%c'))
                file.write(html)

                locale.setlocale(locale.LC_ALL, lc)

def main():
    feed_url = sys.argv[1]
    theme_path = sys.argv[2]
    feeder(feed_url, theme_path)

if __name__ == "__main__":
    main()


