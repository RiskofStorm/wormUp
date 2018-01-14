class GoogleSpellcheker(object):

    @staticmethod
    def __get_page(url):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/63.0.3239.84 Safari/537.36'
        headers = {'User-Agent': user_agent, }
        req = Request(url, None, headers)
        page = urlopen(req)
        html_page = str(page.read())
        page.close()
        return html_page

    @staticmethod
    def correct(text):
        html = GoogleSpellcheker.__get_page('http://www.google.com/search?hl=en&q=' + quote(text))
        correct_sent = re.search(r'(?:Showing results for|Did you mean|Including results for)[^\0]*?<a.*?>(.*?)</a>',
                                 html)
        if len(correct_sent.group(1)) != len(text):
            corrected = text
        else:
            corrected = correct_sent.group(1)
            corrected = re.sub(r'<.*?>', '', corrected)
            corrected = unescape(corrected)
        return corrected
