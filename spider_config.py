USER_AGENT = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/40.0.2214.93 Safari/537.36"
)

RULES1 = {
    "item":"//ol[@class='articleList results']/li[@class='detail']",
    "item_url":"//a[@class='cLink artTitle S_C_artTitle ']/@href",

    "title":"//h1[@class='svTitle']/text()",
    "author":"//a[@class='authorName svAuthor']/text()",
    "url": "//a[@id='pdfLink']/@href",
    "email":"//a[@class='auth_mail']/@href"
}
RULES = {
    "item":"",
    "item_url":"//div[@itemprop='item']/a[@class='resultLink']/@href",
    
    "title":"//span[@class='abs_citation_title']/text()",
    "author":"//span[@class='abstract--author-name']/text()",
    "url":"//meta[@name='citation_abstract_html_url']/@content",
    "email":"//span[@class='author-refine-subtitle']/text()"
}



ENTRANCE_URL_LIST=[
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221342685&_sort=r&_st=13&view=c&md5=3970a2cb6b987d7312edecebe490ab7d&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=1140863&NEXT_LIST=1&view=c&md5=004b5b0aa66c1618e1d6f1f949bc8eef&_ArticleListID=-1221342685&chunkSize=200&sisr_search=&TOTAL_PAGES=5705&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=1140863&PREV_LIST=0&NEXT_LIST=2&view=c&md5=666b1c346a93bec4ea18d3f089ce18dc&_ArticleListID=-1221342685&chunkSize=200&sisr_search=&TOTAL_PAGES=5705&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=1140863&PREV_LIST=1&NEXT_LIST=3&view=c&md5=4ae015da12b65a0474352ad4dcab36e0&_ArticleListID=-1221342685&chunkSize=200&sisr_search=&TOTAL_PAGES=5705&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=1140863&PREV_LIST=2&NEXT_LIST=4&view=c&md5=39a204b9d72efa6798df6c37860d8659&_ArticleListID=-1221342685&chunkSize=200&sisr_search=&TOTAL_PAGES=5705&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221345131&_sort=r&_st=13&view=c&md5=58eb92e04abd788ff60e24985900b26a&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=79628&NEXT_LIST=1&view=c&md5=7e13dbecd953d1c3b8b0b2cc39498ac3&_ArticleListID=-1221345131&chunkSize=200&sisr_search=&TOTAL_PAGES=399&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=156734&NEXT_LIST=1&view=c&md5=b73fc79a5fd2e566cfb09d4a203fb682&_ArticleListID=-1221350720&chunkSize=25&sisr_search=&TOTAL_PAGES=6270&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=156734&NEXT_LIST=1&view=c&md5=b73fc79a5fd2e566cfb09d4a203fb682&_ArticleListID=-1221350720&chunkSize=200&sisr_search=&TOTAL_PAGES=784&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=156734&PREV_LIST=0&NEXT_LIST=2&view=c&md5=51e31d0c194b95995297dd656947ca0c&_ArticleListID=-1221350720&chunkSize=200&sisr_search=&TOTAL_PAGES=784&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=156734&PREV_LIST=1&NEXT_LIST=3&view=c&md5=02bd23c02e3a5063964e43e68745da55&_ArticleListID=-1221350720&chunkSize=200&sisr_search=&TOTAL_PAGES=784&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221351276&_sort=r&_st=13&view=c&md5=fdd11c4b4ccefa29e2a8e574dbba3d33&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=603788&NEXT_LIST=1&view=c&md5=109bc015b799bdd184a7b4f869bff1cd&_ArticleListID=-1221351276&chunkSize=200&sisr_search=&TOTAL_PAGES=3019&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=603788&PREV_LIST=0&NEXT_LIST=2&view=c&md5=6ba01a668472c39e1b9d3989d8f1f244&_ArticleListID=-1221351276&chunkSize=200&sisr_search=&TOTAL_PAGES=3019&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=603788&PREV_LIST=1&NEXT_LIST=3&view=c&md5=5aed46da0bc9f195f230a0eada1149ec&_ArticleListID=-1221351276&chunkSize=200&sisr_search=&TOTAL_PAGES=3019&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=603788&PREV_LIST=2&NEXT_LIST=4&view=c&md5=9b37f50c835bfe95685bae403d8f8be9&_ArticleListID=-1221351276&chunkSize=200&sisr_search=&TOTAL_PAGES=3019&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=1870&NEXT_LIST=1&view=c&md5=d943e426f79b67875bd8305f3ac6ef4e&_ArticleListID=-1221349914&chunkSize=200&sisr_search=&TOTAL_PAGES=10&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=25",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=211295&NEXT_LIST=1&view=c&md5=78ad5c9f945b0f73c4aa43e899198123&_ArticleListID=-1221349106&chunkSize=25&sisr_search=&TOTAL_PAGES=8452&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=211295&NEXT_LIST=1&view=c&md5=78ad5c9f945b0f73c4aa43e899198123&_ArticleListID=-1221349106&chunkSize=200&sisr_search=&TOTAL_PAGES=1057&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=211295&PREV_LIST=0&NEXT_LIST=2&view=c&md5=746234c263753347d426691b1a5949f6&_ArticleListID=-1221349106&chunkSize=200&sisr_search=&TOTAL_PAGES=1057&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=211295&PREV_LIST=1&NEXT_LIST=3&view=c&md5=7164c7d4c70199161091b8cf107976cf&_ArticleListID=-1221349106&chunkSize=200&sisr_search=&TOTAL_PAGES=1057&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=211295&PREV_LIST=2&NEXT_LIST=4&view=c&md5=dfb3ad29845da05de1f2dfd26cd97567&_ArticleListID=-1221349106&chunkSize=200&sisr_search=&TOTAL_PAGES=1057&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221353052&_sort=r&_st=13&view=c&md5=00e0e3b3286554f6693b30677058642f&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=240448&NEXT_LIST=1&view=c&md5=a654b89fc797577dff7dd81f5ff913a3&_ArticleListID=-1221353052&chunkSize=200&sisr_search=&TOTAL_PAGES=1203&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=240448&PREV_LIST=0&NEXT_LIST=2&view=c&md5=da82e1582e2345dc50f3b28660ef87c2&_ArticleListID=-1221353052&chunkSize=200&sisr_search=&TOTAL_PAGES=1203&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=240448&PREV_LIST=1&NEXT_LIST=3&view=c&md5=6a4d59f8cd4646bf9d8ec981335b0910&_ArticleListID=-1221353052&chunkSize=200&sisr_search=&TOTAL_PAGES=1203&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # ""
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=834&sort=r&filterType=&_chunk=0&hitCount=834&NEXT_LIST=1&view=c&md5=e36056d19e9dcbae2d51402b5db4fac6&_ArticleListID=-1221777814&chunkSize=200&sisr_search=&TOTAL_PAGES=5&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=50",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=18973&NEXT_LIST=1&view=c&md5=0bdb9bf9f7cd954d15f805e4c50d4eed&_ArticleListID=-1221776791&chunkSize=50&sisr_search=&TOTAL_PAGES=380&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221779962&_sort=r&_st=13&view=c&md5=3d5191a61848bf62367062a5382b1c67&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=1515673&NEXT_LIST=1&view=c&md5=3ea727c1e50ac1dc970bcb4d32f5a082&_ArticleListID=-1221779962&chunkSize=200&sisr_search=&TOTAL_PAGES=7579&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=1515673&NEXT_LIST=1&view=c&md5=3ea727c1e50ac1dc970bcb4d32f5a082&_ArticleListID=-1221779962&chunkSize=200&sisr_search=&TOTAL_PAGES=7579&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=1515673&PREV_LIST=0&NEXT_LIST=2&view=c&md5=2d6f7506fec28f63c17ae9b6703c49ac&_ArticleListID=-1221779962&chunkSize=200&sisr_search=&TOTAL_PAGES=7579&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=1515673&PREV_LIST=1&NEXT_LIST=3&view=c&md5=6248581c211dd8c43e5167a2c25ae077&_ArticleListID=-1221779962&chunkSize=200&sisr_search=&TOTAL_PAGES=7579&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=1515673&PREV_LIST=2&NEXT_LIST=4&view=c&md5=0341aaeec1ea7ac257ef424a163253c7&_ArticleListID=-1221779962&chunkSize=200&sisr_search=&TOTAL_PAGES=7579&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=244486&NEXT_LIST=1&view=c&md5=90fafe156efb1554c31eae063ad470b5&_ArticleListID=-1221780972&chunkSize=25&sisr_search=&TOTAL_PAGES=9780&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=244486&NEXT_LIST=1&view=c&md5=90fafe156efb1554c31eae063ad470b5&_ArticleListID=-1221780972&chunkSize=200&sisr_search=&TOTAL_PAGES=1223&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=244486&PREV_LIST=0&NEXT_LIST=2&view=c&md5=ee49cfbff3b66ab39fddaec10d5f672a&_ArticleListID=-1221780972&chunkSize=200&sisr_search=&TOTAL_PAGES=1223&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=244486&PREV_LIST=1&NEXT_LIST=3&view=c&md5=ca879e8e216cf2d19193f93fe4fe7b48&_ArticleListID=-1221780972&chunkSize=200&sisr_search=&TOTAL_PAGES=1223&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=244486&PREV_LIST=2&NEXT_LIST=4&view=c&md5=062b90e784526d55bf54b4cf62f6257a&_ArticleListID=-1221780972&chunkSize=200&sisr_search=&TOTAL_PAGES=1223&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221782674&_sort=r&_st=13&view=c&md5=06b649db863888b3b528a0e9ed8dc6f1&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=502735&NEXT_LIST=1&view=c&md5=2268795aef7bd446fde9512fdddaad09&_ArticleListID=-1221782674&chunkSize=200&sisr_search=&TOTAL_PAGES=2514&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=502735&PREV_LIST=0&NEXT_LIST=2&view=c&md5=67131f2ec9f49614acc2a74b7a23d5f8&_ArticleListID=-1221782674&chunkSize=200&sisr_search=&TOTAL_PAGES=2514&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=502735&PREV_LIST=1&NEXT_LIST=3&view=c&md5=f759cfb6fcc03fa074286d6ac4422f16&_ArticleListID=-1221782674&chunkSize=200&sisr_search=&TOTAL_PAGES=2514&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=502735&PREV_LIST=2&NEXT_LIST=4&view=c&md5=274131bf552ada75be9308848d66b3c6&_ArticleListID=-1221782674&chunkSize=200&sisr_search=&TOTAL_PAGES=2514&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221784060&_sort=r&_st=13&view=c&md5=73456704df79cea9f7a46ec697e4d03c&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=331184&NEXT_LIST=1&view=c&md5=ba3efda0796c072dda320626675f0d40&_ArticleListID=-1221784060&chunkSize=25&sisr_search=&TOTAL_PAGES=13248&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=331184&NEXT_LIST=1&view=c&md5=ba3efda0796c072dda320626675f0d40&_ArticleListID=-1221784060&chunkSize=200&sisr_search=&TOTAL_PAGES=1656&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=331184&NEXT_LIST=1&view=c&md5=ba3efda0796c072dda320626675f0d40&_ArticleListID=-1221784060&chunkSize=200&sisr_search=&TOTAL_PAGES=1656&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=331184&PREV_LIST=1&NEXT_LIST=3&view=c&md5=17f4e883f6bdca6b07f278d9b19200b9&_ArticleListID=-1221784060&chunkSize=200&sisr_search=&TOTAL_PAGES=1656&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=331184&PREV_LIST=2&NEXT_LIST=4&view=c&md5=021f0b13b2bbc79718e42da7f337bc17&_ArticleListID=-1221784060&chunkSize=25&sisr_search=&TOTAL_PAGES=13248&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200"
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=89529&NEXT_LIST=1&view=c&md5=63da4cb4daed8259fc2e3acd4586f66f&_ArticleListID=-1221786622&chunkSize=25&sisr_search=&TOTAL_PAGES=3582&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&displayPerPageFlag=t&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=89529&NEXT_LIST=1&view=c&md5=63da4cb4daed8259fc2e3acd4586f66f&_ArticleListID=-1221786622&chunkSize=200&sisr_search=&TOTAL_PAGES=448&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221786770&_sort=r&_st=13&view=c&md5=04a1552f7425d8ee7d03346826dee4ad&searchtype=a",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=191277&NEXT_LIST=1&view=c&md5=fa52dfb5d01a6e925733411908b8b3d9&_ArticleListID=-1221786770&chunkSize=200&sisr_search=&TOTAL_PAGES=957&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=191277&PREV_LIST=0&NEXT_LIST=2&view=c&md5=d85917b372ee4d7e1ff7431ae1b72db1&_ArticleListID=-1221786770&chunkSize=200&sisr_search=&TOTAL_PAGES=957&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=191277&PREV_LIST=1&NEXT_LIST=3&view=c&md5=343399a3bc61f3f5770cd3d0df30fa74&_ArticleListID=-1221786770&chunkSize=200&sisr_search=&TOTAL_PAGES=957&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=191277&PREV_LIST=2&NEXT_LIST=4&view=c&md5=f4e66b64f3eae876cd218757079e617b&_ArticleListID=-1221786770&chunkSize=200&sisr_search=&TOTAL_PAGES=957&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
    # "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221787814&_sort=r&_st=13&view=c&md5=12ba6d12003e578a723ab02e1733e792&searchtype=a"
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221808253&_sort=r&_st=5&md5=82cfc82b3cf903468bceaa8c8e891b88&searchtype=a",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=5&count=1000&sort=r&filterType=&_chunk=0&hitCount=4716718&NEXT_LIST=1&view=c&md5=62e546b5424b233661e10ea066c1a719&_ArticleListID=-1221808253&chunkSize=200&sisr_search=&TOTAL_PAGES=23584&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=5&count=1000&sort=r&filterType=&_chunk=1&hitCount=4716718&PREV_LIST=0&NEXT_LIST=2&view=c&md5=5fbe20c0b7708b48b12cb5515512d276&_ArticleListID=-1221808253&chunkSize=200&sisr_search=&TOTAL_PAGES=23584&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=5&count=1000&sort=r&filterType=&_chunk=2&hitCount=4716718&PREV_LIST=1&NEXT_LIST=3&view=c&md5=fa1b9a96d60f8fdd9b9a2d9fab778405&_ArticleListID=-1221808253&chunkSize=200&sisr_search=&TOTAL_PAGES=23584&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=5&count=1000&sort=r&filterType=&_chunk=3&hitCount=4716718&PREV_LIST=2&NEXT_LIST=4&view=c&md5=6a89c3d018a186c3b65f27170bb80ec3&_ArticleListID=-1221808253&chunkSize=200&sisr_search=&TOTAL_PAGES=23584&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221815139&_sort=r&_st=13&view=c&md5=b9d7c2eabc72cc492086ff1ae418c718&searchtype=a",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=0&hitCount=1105535&NEXT_LIST=1&view=c&md5=7fe9d7cac11b2db4efe662e80ae980c0&_ArticleListID=-1221815139&chunkSize=200&sisr_search=&TOTAL_PAGES=5528&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=1&hitCount=1105535&PREV_LIST=0&NEXT_LIST=2&view=c&md5=ac6007185292a350e54193fbbc18cfd7&_ArticleListID=-1221815139&chunkSize=200&sisr_search=&TOTAL_PAGES=5528&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=2&hitCount=1105535&PREV_LIST=1&NEXT_LIST=3&view=c&md5=6ce4f685b8355ffee389ffb9f8676894&_ArticleListID=-1221815139&chunkSize=200&sisr_search=&TOTAL_PAGES=5528&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=13&count=1000&sort=r&filterType=&_chunk=3&hitCount=1105535&PREV_LIST=2&NEXT_LIST=4&view=c&md5=da151250dc41de1266fc3b4ecb442f6f&_ArticleListID=-1221815139&chunkSize=200&sisr_search=&TOTAL_PAGES=5528&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-1221816992&_sort=r&_st=4&md5=469160ad976ba49ccfb328b0d140bc23&searchtype=a",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=4&count=1000&sort=r&filterType=&_chunk=0&hitCount=784639&NEXT_LIST=1&view=c&md5=a0f09589fd39d81a6dc4623d4e3c236e&_ArticleListID=-1221816992&chunkSize=200&sisr_search=&TOTAL_PAGES=3924&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=4&count=1000&sort=r&filterType=&_chunk=1&hitCount=784639&PREV_LIST=0&NEXT_LIST=2&view=c&md5=c52d0274757345511a721f293a8bf05c&_ArticleListID=-1221816992&chunkSize=200&sisr_search=&TOTAL_PAGES=3924&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=4&count=1000&sort=r&filterType=&_chunk=2&hitCount=784639&PREV_LIST=1&NEXT_LIST=3&view=c&md5=c0b4196098b235483c7d2c9719d6e191&_ArticleListID=-1221816992&chunkSize=200&sisr_search=&TOTAL_PAGES=3924&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200",
#     "http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&searchtype=a&refSource=search&pdfDownloadSort=r&PDF_DDM_MAX=25&_st=4&count=1000&sort=r&filterType=&_chunk=3&hitCount=784639&PREV_LIST=2&NEXT_LIST=4&view=c&md5=509ce175afd73de0486aff9be00a4434&_ArticleListID=-1221816992&chunkSize=200&sisr_search=&TOTAL_PAGES=3924&pdfDownload=&zone=exportDropDown&citation-type=RIS&format=cite-abs&bottomPaginationBoxChanged=&bottomNext=Next+%3E%3E&displayPerPageFlag=f&resultsPerPage=200"
    "http://europepmc.org/search?query=big+data&page=1&sortby=Date%2BDESC"
]

# # 抓取前多少页
# MAX_PAGE = 5

# 并发数
POOL_SIZE = 20

# 监控周期(秒),默认10分钟
WATCH_INTERVAL = 10 * 60

# 重载代理周期
PROXY_INTERVAL = 30 * 60