#类别表
create table t_sciencedirect_journals_class(
'class_id' int,
'subject_name' varchar(50),   #   主题、科目
'son_subject_name' varchar(50),    #  子 主题、科目
'grandson_subject' varchar(50),   #  孙子 主题、科目
'main_url' varchar(100),   #   主页中每个选项的URL    /science/journal/22126716
)

#URL关系表
create table t_sciencedirect_journals_url(
'url_id' int,
'main_url' varchar(100),   #   主页中每个选项的URL    /science/journal/22126716
'main_name' varchar(100),    #  主页中每个选项名字     AASRI Procedia
'parent_url' varchar(100),   #  主页每个选项链接下的对应的卷URL   http://www.sciencedirect.com/science/journal/22126716     #href: /science/journal/22126716/9
'article_url' varchar(100),   #   每卷对应的期刊的URL，唯一性    http://www.sciencedirect.com/science/article/pii/S2212671614001024
)

#期刊内容表
create table t_sciencedirect_journals_url(
'content_id' int,
'article_url' varchar(100),   #   期刊论文的唯一URL http://www.sciencedirect.com/science/article/pii/S2212671614001024
'publication_title' varchar(100),    #   AASRI Procedia
'size_m' varchar(100),   #  Volume 9, 2014, Pages 2-7
'article_title' varchar(100),   #   A New Texture Analysis Approach for Iris Recognition
'author_group' varchar(200),     #多个作者信息
'doilink' varchar(50),    #链接  http://dx.doi.org/10.1016/j.actbio.2017.01.035
'abstract_author' text,    #摘要
'keywords' varchar(100)  #关键词
)