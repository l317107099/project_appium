import requests

class Hub():
    def __init__(self):
        self.url = "https://c1v-h.phncdn.com/hls/videos/201912/21/270295361/,480P_2000K,240P_400K,_270295361.mp4.urlset/"
        self.proxies = {
            "http":"http://103.133.177.83:25",
        }
"TViVYi8ztjXbsA2udgRNIe6jwQQZmAyPzofSWsTuh1qM7U_2KolEFyOc-zu1ylEqjBFBf0w38M8zucnzpZAkUPrguZg-73MwKoE9GffVFHRpD2zMAp7u2wv9f62_IMIN4o-JjnGS8KOOkT1vseQHjYoXrSALf2GuBXZsVXTIVE9A8bRkdXqW0gjJjuAu5HWSH-hJ_fa22ZwEudJSTpAJHA"
"TViVYi8ztjXbsA2udgRNIe6jwQQZmAyPzofSWsTuh1qM7U_2KolEFyOc-zu1ylEqjBFBf0w38M8zucnzpZAkUPrguZg-73MwKoE9GffVFHRpD2zMAp7u2wv9f62_IMIN4o-JjnGS8KOOkT1vseQHjYoXrSALf2GuBXZsVXTIVE9A8bRkdXqW0gjJjuAu5HWSH-hJ_fa22ZwEudJSTpAJHA"
"TViVYi8ztjXbsA2udgRNIe6jwQQZmAyPzofSWsTuh1qM7U_2KolEFyOc-zu1ylEqjBFBf0w38M8zucnzpZAkUPrguZg-73MwKoE9GffVFHRpD2zMAp7u2wv9f62_IMIN4o-JjnGS8KOOkT1vseQHjYoXrSALf2GuBXZsVXTIVE9A8bRkdXqW0gjJjuAu5HWSH-hJ_fa22ZwEudJSTpAJHA"
    def get_extm3u(self):
        index = self.url +"index-f1-v1-a1.m3u8?TViVYi8ztjXbsA2udgRNIe6jwQQZmAyPzofSWsTuh1qM7U_2KolEFyOc-zu1ylEqjBFBf0w38M8zucnzpZAkUPrguZg-73MwKoE9GffVFHRpD2zMAp7u2wv9f62_IMIN4o-JjnGS8KOOkT1vseQHjYoXrSALf2GuBXZsVXTIVE9A8bRkdXqW0gjJjuAu5HWSH-hJ_fa22ZwEudJSTpAJHA"

        response = requests.get(url= index,proxies = self.proxies)
        with open("index.m3u8","wb") as f:
            f.write(response.content)

if __name__ == '__main__':
    hub = Hub()
    hub.get_extm3u()
