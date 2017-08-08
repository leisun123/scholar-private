# Scholar Info Crawler

## `Version requirement`

```
python 3.5+
```


## `Deploy`

```
git clone https://github.com/IsolationWyn/scholar.git
cd scholar
pip install -r requirement
```

## `Introduction`

> ### 1. 精细解析爬取模式
>  #### ScholarConfig 模块下创建 {major}_{organization}_rule.py, 在此编写对应信息的xpath解析式
> Example:

```
RULES = {
    "item_url":"//td[@class='name']/a/@href",
    "avatar":"//img[@class='alignright']/@src",
    "name":"//h1[@class='page-title']/text()",
    "title":"//section[@class='entry-content clearfix']/span/h3/text()",
    "phone":"//section[@class='entry-content clearfix']/span/span[2]/text()",
    "email":"//section[@class='entry-content clearfix']/span/span[3]/a/text()",
    "website":"//section[@class='entry-content clearfix']/span/span[4]/a/text()",
    "keywords":"//section[@class='entry-content clearfix']/span/span[6]/a/text()",
    "cooperation":"//section[@class='entry-content clearfix']/span/span[7]/a/text()"

}


BASE_URL =  "http://tmi.utexas.edu/people/type/faculty/"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20
```


>  #### CustomPaser 模块下创建 {major}_{organization}_parser.py,数据清洗

> ####  TaskFeed 模块下创建 {major}_{organization}_task.py


```
graph LR;
    feed_page_queue-->|put|page_queue;
    page_queue-->|get|page_loop;

    feed_info_queue-->|put|info_queue;
    info_queue-->|get|item_loop;

    crawl_info-->|put|parm_queue;
    parm_queue-->|get|db_save_loop
```
> #### page_queue 一级链接队列
> #### info_queue 二级学者条目链接队列
> #### crawl_info 学者信息json存储队列


---

> ### 2. Scrapely建模爬取

> #### SampleData 模块下建立 {major}_{organization}.py
> Example:

```
#学者列表入口
base_url = 'http://ame.nd.edu/people/faculty'
#特征训练示例学者入口
sample_url = 'https://engineering.nd.edu/profiles/hfernando'
#条目链接
item_url_rule = "//a[@class='external-link']/@href"

#填补缺失
bio_rule = "//h2[text()='Biography']/following-sibling::*/text()"
phone_rule = "//*[@id='content-core']/div[1]/div[2]/p[2]"

#示例数据
data = {"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Harindra Fernando",
        "title":"Wayne and Diana Murdy Endowed Professor",
        "phone":"574-631-9346",
        "email":"Fernando.10@nd.edu",
        "website":"http://www.nd.edu/~dynamics/",
        "cooperation":"College of Engineering",
        "keywords":"Department of Aerospace and Mechanical Engineering"
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "Department of Aerospace and Mechanical Engineering"
```
> CustomPaser 模块下建立 {major}_{organization}_parser.py, 数据清洗

> 入口程序调度实例


```
    BIONyuTask = CommonTask(website_name=BIONyuClass.__name__,
                   custom_parser=BIONyuClass,
                   base_url=base_url,
                   sample_url=sample_url,
                   data=data,
                   item_url_rule=item_url_rule,
                   default_url="http://engineering.nyu.edu",
                   is_url_joint=True
                   )
    BIONyuTask.run()
```

