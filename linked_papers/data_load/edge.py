import numpy as np
import pandas as pd
from ..models import Edge
from sqlalchemy import create_engine


def load_csv():
    df = pd.read_csv('./csv/edge.csv', header=None)
    df.columns = ["essay_id", "cited_id"]
    print("load_csv() finished!")
    return df


def load_edge():
    # Establish database connection.
    engine = create_engine('sqlite:///db.sqlite3')

    # Writing dataframe into database.
    df = load_csv()
    df.to_sql('linked_papers_edge', con=engine, if_exists='replace', index=False)

    # Convert dataframe into Essay object list.
    papers = [
        Edge(essay_id=row['essay_id'],
              cited_id=row['cited_id'])
        for index, row in df.iterrows()
    ]

    # Insertion.
    Edge.objects.bulk_create(papers)
    print("load_edge() finished!")
