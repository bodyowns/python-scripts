"""
___.              .___
\_ |__   ____   __| _/__.__.
 | __ \ /  _ \ / __ <   |  |
 | \_\ (  <_> ) /_/ |\___  |
 |___  /\____/\____ |/ ____|\N{TRADE MARK SIGN}
     \/            \/\/
"""
from bs4 import BeautifulSoup
from itertools import count
import requests

url = 'http://alpha.wallhaven.cc/search?categories=101&sorting=favorites&order=desc&page='
jpg = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg'
png = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.png'

print("""
\n
#######################################################
#             Downloading Wallpapers from             #
#                     wallhaven.cc                    #
#                                                     #
#                 by - Noje Sebastian                 #
#######################################################
\n
"""
)

status = '\r Page: {:0>2} - Img {:0>2} / 24 [{:.<24}]'.format

pics = input("Number of pages you want to download? (24 pics / page): ")
print("\n")
for i in range(1, int(pics) + 1):
    soup = BeautifulSoup(requests.get(url + str(i)).text, "lxml")
    figs = soup.find_all('figure')
    for j, fig in enumerate(figs, 1):
        print(status(i, j, j*'*')),
        name = fig.find('a').get('href').rsplit('/', 1)[1]
        r = requests.get(jpg % name)
        if r.status_code == 404:
            r = requests.get(png % name)
            name += '.png'
        else:
            name += '.jpg'
        with open('%03d-%02d-%s' % (i, j, name), 'wb') as f:
            f.write(r.content)
