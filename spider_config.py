USER_AGENT = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/40.0.2214.93 Safari/537.36"
)

RULES = {
    "item":"//ol[@class='articleList results']/li[@class='detail']",
    "item_url":"//a[@class='cLink artTitle S_C_artTitle ']/@href",

    "title":"//h1[@class='svTitle']/text()",
    "author":"//a[@class='authorName svAuthor']/text()",
    "url": "//a[@id='pdfLink']/@href",
    "email":"//a[@class='auth_mail']/@href"
}



ENTRANCE_URL_LIST=[
   "http://www.sciencedirect.com/search?qs=Aggregation&show=100&sortBy=relevance",
	"http://www.sciencedirect.com/search?offset=100&qs=Aggregation&show=100&sortBy=relevance",
	"http://www.sciencedirect.com/search?offset=200&qs=Aggregation&show=100&sortBy=relevance",
	"http://www.sciencedirect.com/search?offset=300&qs=Aggregation&show=100&sortBy=relevance"
   ]


# # 抓取前多少页
# MAX_PAGE = 5

# 并发数
POOL_SIZE = 20

# 监控周期(秒),默认10分钟
WATCH_INTERVAL = 10 * 60

# 重载代理周期
PROXY_INTERVAL = 30 * 60