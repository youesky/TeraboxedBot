from os import path
from re import findall
from requests import Session
from http.cookiejar import MozillaCookieJar
from urllib.parse import urlparse, parse_qs

from plugins.helper.ext_utils.exceptions import DirectDownloadLinkException


def terabox(url):
    if not path.isfile('cookies.txt'):
        raise DirectDownloadLinkException("ERROR: cookies.txt not found")
    try:
        jar = MozillaCookieJar('cookies.txt')
        jar.load()
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    cookies = {}
    for cookie in jar:
        cookies[cookie.name] = cookie.value
    details = {'contents':[], 'title': '', 'total_size': 0}
    details["header"] = ' '.join(f'{key}: {value}' for key, value in cookies.items())

    def __fetch_links(session, dir_='', folderPath=''):
        params = {
            'app_id': '250528',
            'jsToken': jsToken,
            'shorturl': shortUrl
            }
        if dir_:
            params['dir'] = dir_
        else:
            params['root'] = '1'
        try:
            _json = session.get("https://www.1024tera.com/share/list", params=params, cookies=cookies).json()
        except Exception as e:
            raise DirectDownloadLinkException(f'ERROR: {e.__class__.__name__}')
        if _json['errno'] not in [0, '0']:
            if 'errmsg' in _json:
                raise DirectDownloadLinkException(f"ERROR: {_json['errmsg']}")
            else:
                raise DirectDownloadLinkException('ERROR: Something went wrong!')

        if "list" not in _json:
            return
        contents = _json["list"]
        for content in contents:
            if content['isdir'] in ['1', 1]:
                if not folderPath:
                    if not details['title']:
                        details['title'] = content['server_filename']
                        newFolderPath = path.join(details['title'])
                    else:
                        newFolderPath = path.join(details['title'], content['server_filename'])
                else:
                    newFolderPath = path.join(folderPath, content['server_filename'])
                __fetch_links(session, content['path'], newFolderPath)
            else:
                if not folderPath:
                    if not details['title']:
                        details['title'] = content['server_filename']
                    folderPath = details['title']
                item = {
                    'url': content['dlink'],
                    'filename': content['server_filename'],
                    'path' : path.join(folderPath),
                }
                if 'size' in content:
                    size = content["size"]
                    if isinstance(size, str) and size.isdigit():
                        size = float(size)
                    details['total_size'] += size
                details['contents'].append(item)
    with Session() as session:
        try:
            _res = session.get(url, cookies=cookies)
        except Exception as e:
            raise DirectDownloadLinkException(f'ERROR: {e.__class__.__name__}')
        if jsToken := findall(r'window\.jsToken.*%22(.*)%22', _res.text):
            jsToken = jsToken[0]
        else:
            raise DirectDownloadLinkException('ERROR: jsToken not found!.')
        shortUrl = parse_qs(urlparse(_res.url).query).get('surl')
        if not shortUrl:
            raise DirectDownloadLinkException("ERROR: Could not find surl")
        try:
            __fetch_links(session)
        except Exception as e:
            raise DirectDownloadLinkException(e)
    return details['contents'][0]['url'], details['title'], details['total_size']
