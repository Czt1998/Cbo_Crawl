# coding utf-8
import re
import time
import os
import urllib.request
from selenium import webdriver

driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()


def Cbo_Crawl(movie_name,movie_year):
    url = 'http://www.cbooo.cn/search?k=' + urllib.request.quote(movie_name)
    driver.get(url)
    time.sleep(1)
    urls = driver.find_elements_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li")
    for i in range(1,urls.__len__()+1,1):
        name = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/a").text
        name = str(name).split(' ')[0]
        year_text = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/span").text
        year_text = str(year_text)
        year = str(re.findall('.*?(.*?)年',year_text))[-6:-2]
        print(name),
        print(year)
        if name == movie_name and year == str(movie_year):
            print("found")
            url = driver.find_element_by_xpath("//div[@class='row borbg pad02 mar30']/ul/li[" + str(i) + "]/a").get_attribute("href")
            print(url)
            Get_data(url,movie_name,movie_year)
            break
        else:
            print("continue")


def Get_data(url,movie_name,movie_year):
    print("fuction used")
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='mainbox fr']/div/ul/li[2]").click()
    market = driver.find_elements_by_xpath("//div[@id='tabcont2']/h4")
    for i in range(1,market.__len__()+1,1):
        data_week = list()
        weeks = driver.find_elements_by_xpath("//div[@id='tabcont2']/table[" + str(i) + "]/tbody/tr")
        market_name = driver.find_element_by_xpath("//div[@id='tabcont2']/h4[" + str(i) + "]").text
        if market_name != '香港票房':
            star = 2
        else:
            star = 1
        for j in range(star,weeks.__len__()+1,1):
            info = driver.find_elements_by_xpath("//div[@id='tabcont2']/table[" + str(i) + "]/tbody/tr[" + str(j) + "]/td")
            week = info[0].text
            date = week
            ave_people = info[1].text
            week_money = info[2].text
            total_money = info[3].text
            try:
                days = info[4].text
            except:
                days = -1
            if days !=-1:
                week_dict = {'周次': date,
                             '场均人次': ave_people,
                             '单周票房': week_money,
                             '累计票房': total_money,
                             '上映天数': days}
            else:
                week_dict = {'周次': date,
                             '场均人次': ave_people,
                             '单周票房': week_money,
                             '累计票房': total_money}
            data_week.append(week_dict)
        market_name = market_name[0:4]
        print(market_name)
        print(data_week)
        Store(market_name,data_week,movie_name,movie_year)

def Store(market_name,data_week,movie_name,movie_year):
    print("------store-----")
    with open("./data/" + str(movie_year) + "/" + movie_name + ".txt","a+") as w:
        w.writelines(str(market_name) + '\n')
        w.writelines(str(data_week) + '\n')
if __name__ == '__main__':
    os.mkdir("./data")
    for year in range(2010,2018):
        os.mkdir("./data/" + str(year))
        with open("./movie_id/" + str(year) + ".txt", "r") as r:
            lines = r.readlines()
            for line in lines:
                movie_name = line.split('')[0]
                try:
                    Cbo_Crawl(movie_name, year)
                except Exception as e:
                    with open("./Movie_failed.txt","a+") as w:
                        w.writelines(movie_name + ' ' +str(year) + '\n')
                        w.writelines(str(e))
                        w.writelines('\n')
                    continue
