from minicms.wsgi import *
from news.models import Article,Column

def main():
    columns_urls = [
        ("体育新闻",'sports'),
        ("社会新闻",'society'),
        ("科技新闻",'tech')
    ]
    for columns_name,url in columns_urls:
        c = Column.objects.get_or_create(name=columns_name,slug=url)[0]
        # 创建10篇新闻
        for i in range(1,11):
            article = Article.objects.get_or_create(
                title = '{}_{}'.format(columns_name,url),
                slug =  'article_{}'.format(i),
                content = "新闻详细内容：{}{}".format(columns_name,i)
            )[0]
            article.column.add()
if __name__ == "__main__":
    main()
    print('done!')