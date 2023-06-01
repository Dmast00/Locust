from bs4 import BeautifulSoup
import urllib

def get_hidden_elements(response):
        # look for aspNetHidden elements
        soup = BeautifulSoup(response.text, 'html.parser')
        view_st = urllib.parse.quote(soup.find(id="__VIEWSTATE")['value'], safe='')
        view_st_gen = urllib.parse.quote(soup.find(id="__VIEWSTATEGENERATOR")['value'], safe='')
        # event_val = urllib.parse.quote(soup.find(id="__EVENTVALIDATION")['value'], safe='')
        # returns the payload elements
        return view_st, view_st_gen #, event_val


# Return headers requests
def get_headers(www, route):
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '194183',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        # # 'DNT': '1',
        # 'Host': www,
        # 'Origin': www,
        # 'Referer': www + route,
        # 'Upgrade-Insecure-Requests': '1'
        # # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
        "Host": ""+www,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "514",
        "Origin": ""+www,
        "Connection": "keep-alive",
        "Referer": ""+www+""+route,
        "Cookie": "ASP.NET_SessionId=ukorehpfkcfowzposl54qqqw",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    }
    return headers
