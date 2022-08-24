import requests as req

In [2]: from fontTools.ttLib import TTFont

In [3]: url = 'http://www.porters.vip/confusion/
   ...: movie.html'

In [4]: woff_url = 'http://www.porters.vip/confu
   ...: sion/font/movie.woff'

In [5]: repons=req.get(url).text

In [6]: resp = req.get(woff_url)

In [7]: with open('字体解密.woff','wb') as f:
   ...:          f.write(resp.content)
   ...:

In [8]: base_fonts_dict = {'uniE9C7':'7', 'uniF5
   ...: 7B':'1', 'uniE7DF':'2', 'uniE339':'6', '
   ...: uniE624':'9', 'uniEA16':'5', 'uniF19A':'
   ...: 3', 'uniEE76':'0', 'uniF593':'4', 'uniEF
   ...: D4':'8'}

In [9]: base_fonts_dict = {'&#x' + i[0][3:].lowe
   ...: r():i[1] for i in base_fonts_dict.items(
   ...: )}

In [10]: for i in base_fonts_dict:
    ...:     repons=repons.replace(i,base_fonts_
    ...: dict[i])
    ...:

In [11]: print(repons)
