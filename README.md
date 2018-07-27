# Cbo_Crawl
Get the weekly box office from [www.cbo.com](http://www.cbooo.cn)<br>
## Main code
`Cbo_Crawl.py`
Do the task to get the imformation we need.<br>
## Operating environment
Based on python3.5, first to install:<br>
1. selenium<br>
2. phantomjs<br>
## Operating instructions
Run `Cbo_Crawl.py`, and we will get the imformation we need.<br>
## Processing sample
* First, the code will open the file `movie_id` to get `movie name` we want to get box office. The datas are store as follow:<br><br>
movie_name　　movie_id<br>
山楂树之恋　　　4151110<br>
杜拉拉升职记　　3820191<br>
锦衣卫　　　　　3754946<br>
......<br><br>
* And then use the `movie name` to search in cbo, check if name and year are right. If it's correct, get the url of the movie by xpath.
![](https://github.com/Czt1998/Cbo_Crawl/blob/master/pic/search)
![](https://github.com/Czt1998/Cbo_Crawl/blob/master/pic/url)
* Finally get the data we want.
![](https://github.com/Czt1998/Cbo_Crawl/blob/master/pic/data)
## Sample output
内地票房<br>
[ {'周次'：...,'场均人次':...,'单周票房':...,'累计票房':...,'上映天数':...},　...]<br>
香港票房<br>
[ {'周次'：...,'场均人次':...,'单周票房':...,'累计票房':...},　...]<br>
北美票房<br>
[ {'周次'：...,'场均人次':...,'单周票房':...,'累计票房':...},　...]<br>

* For more example, check `data`.
