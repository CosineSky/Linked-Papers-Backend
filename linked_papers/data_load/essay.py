import pandas as pd
from ..models import Essay
from sqlalchemy import create_engine


def load_essay():
    # 假设你已经有一个DataFrame
    df = pd.DataFrame({
        'title': ['Paper 1', 'Paper 2', 'Paper 3'],
        'abstract': ['Abstract 1', 'Abstract 2', 'Abstract 3'],
        'publish_year': [2018, 2019, 2020],
        'category': [1, 2, 3]
    })

    # 创建数据库连接，SQLite数据库文件路径
    engine = create_engine('sqlite:///db.sqlite3')

    # 将DataFrame写入数据库（如果表存在会覆盖，若不存在则会创建）
    df.to_sql('linked_papers_essay', con=engine, if_exists='replace', index=False)

    # 将DataFrame行转换为Essay对象列表
    papers = [
        Essay(title=row['title'],
              abstract=row['abstract'],
              publish_year=row['publish_year'],
              category=row['category'])
        for index, row in df.iterrows()
    ]

    # 批量插入
    Essay.objects.bulk_create(papers)
