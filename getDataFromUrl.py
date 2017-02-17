import urllib
import urllib2
import sys
import gzip
import StringIO

login_url = 'https://cure.uniqueway.com'
guider_url = 'https://cure.uniqueway.com/guidebooks?page='
countries = 'https://cure.uniqueway.com/countries?page=';
pois = 'https://cure.uniqueway.com/new_pois/'


def catch(catch_url):
    headers = {
        'Host': ' cure.uniqueway.com',
        'Connection': ' keep-alive',
        'Upgrade-Insecure-Requests': ' 1',
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Accept': ' textml,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': ' https://cure.uniqueway.com/staffs/sign_in',
        'Accept-Encoding': ' gzip, deflate, sdch, br',
        'Accept-Language': ' zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie': ' im_flag=8ae5dc96-4231-42c7-a0d8-be274255eb40; Hm_lvt_99b16494f0d5c62886f892347d60f067=1481003654; Hm_lpvt_99b16494f0d5c62886f892347d60f067=1481081273; _gat=1; _session_id=7d5ed8055a7cecd859148d73e0706240; __profilin=p%3Dt%2Ca%3D4b279c1f2dcfb7fb8aac70b51c5ed483; _ga=GA1.2.1528737089.1481003655',
    }

    req = urllib2.Request(
        url=catch_url,
        headers=headers
    )
    response = urllib2.urlopen(req)
    the_page = response.read()
    data = StringIO.StringIO(the_page)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
    return html


# print 'Real url :' + response.geturl()


def download(url_prefix, type, number):
    for i in range(1, number):
        real_url = url_prefix + str(i)
        print
        'catch ' + str(i) + '->' + real_url
        html = catch(real_url)
        f = open('d:\\roadbooks\\' + type + '\\' + str(i) + '.html', "a+")
        f.write(html)


download(pois, 'poi', 4)