from bs4 import BeautifulSoup
import urllib2
import datetime
import os


class GetElevenSelectFiveNumber(object):
    def __init__(self, date):
        self.date = date
        self.getUrl(self.date)

    def getUrl(self, date):
        url = r'http://chart.cp.360.cn/kaijiang/kaijiang?lotId=166406&spanType=2&span=%s_%s' % (
            date, date)
        htmlContent = self.getResponseContent(url)
        try:
            soup = BeautifulSoup(htmlContent, 'lxml')
            table = soup.find('table')
            rows = table.find_all('tr')
            file = open("result/" + date, "w")
            for row in rows[1:-2]:
                if row.find('td', {"class": "gray"}) is not None:
                    order = row.find('td', {"class": "gray"}).get_text()
                    left_number = row.find(
                        'em', {"class": "orange"}).get_text()
                    right_number = row.find('em', {"class": "blue"}).get_text()
                    number = "%s %s" % (left_number, right_number)
                    file.write("%s_%s => %s\n" % (date, order, number))
            file.close()
        except AttributeError:
            print ("Get lottery of %s failed!" % date)

    def getResponseContent(self, url):
        try:
            response = urllib2.urlopen(url.encode('utf-8'))
        except:
            print("Get content of %s failed!" % url)
        else:
            return response.read()


def get_all_date(begin, end):
    all_date = []
    begin_date = datetime.datetime.strptime(begin, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        all_date.append(date_str)
        begin_date = begin_date + datetime.timedelta(days=1)
    return all_date
	
	
if __name__ == '__main__':
    all_date = get_all_date("2017-02-04", "2017-05-21")
    if not os.path.exists("result"):
        os.mkdir("result")
    for date in all_date:
        GetElevenSelectFiveNumber(date)