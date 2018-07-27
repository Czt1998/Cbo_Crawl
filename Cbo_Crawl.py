# coding utf-8
import re
import time
import urllib.request
from selenium import webdriver

# driver = webdriver.PhantomJS(executable_path='./phantomjs')
driver = webdriver.Chrome()


def Cbo_Crawl(movie_name,movie_year):
    url = 'http://www.cbooo.cn/search?k=' + urllib.request.quote(movie_name)
    driver.get(url)
    time.sleep(1)
    urls = driver.find_elements_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li")
    print(len(urls))
    for i in range(1,urls.__len__()+1,1):
        name = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/a").text
        name = str(name).split(' ')[0]
        year_text = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/span").text
        year_text = str(year_text)
        year = str(re.findall('.*?(.*?)年',year_text))[-6:-2]
        print(name)
        print(year)
        print(type(year))
        if name == movie_name and year == str(movie_year):
            print("found")
            url = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/a").get_attribute("href")
            print(url)
            Get_data(url,movie_name,movie_year)
            break
        else:
            print("continue")


def Get_data(url,movie_name,movie_year):
    print("used")
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='mainbox fr']/div/ul/li[2]").click()
    market = driver.find_elements_by_xpath("//div[@id='tabcont2']/h4")
    for i in range(1,market.__len__()+1,1):
        data_week = list()
        weeks = driver.find_elements_by_xpath("//div[@id='tabcont2']/table[" + str(i) + "]/tbody/tr")
        for j in range(2,weeks.__len__()+1,1):
            info = driver.find_elements_by_xpath("//div[@id='tabcont2']/table[" + str(i) + "]/tbody/tr[" + str(j) + "]/td")
            print(len(info))
            week = info[0].text
            date = week
            print(date)
            ave_people = info[1].text
            print(ave_people)
            week_money = info[2].text
            print(week_money)
            total_money = info[3].text
            print(total_money)
            try:
                days = info[4].text
            except:
                days = -1
            print(days)
            week_dict = {'周次':date,
                         '场均人次':ave_people,
                         '单周票房':week_money,
                         '累计票房':total_money,
                         '上映天数':days}
            data_week.append(week_dict)
        market_name = driver.find_element_by_xpath("//div[@id='tabcont2']/h4[" + str(i) + "]").text
        if i == 1:
            market_name = market_name[0:4]
        Store(market_name,data_week,movie_name,movie_year)

def Store(market_name,data_week,movie_name,movie_year):
    print("------store-----")
    with open("./data/" + str(movie_year) + "/" + movie_name + ".txt","a+") as w:
        w.writelines(str(market_name) + '\n')
        w.writelines(str(data_week) + '\n')
if __name__ == '__main__':
    count = 0
    for year in range(2010,2018):
        with open("./movie_id/" + str(year) + ".txt", "r") as r:
            lines = r.readlines()
            for line in lines:
                movie_name = line.split('')[0]
                Cbo_Crawl(movie_name, year)
