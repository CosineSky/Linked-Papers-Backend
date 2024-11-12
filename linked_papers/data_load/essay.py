import numpy as np
import pandas as pd
from ..models import Essay
from sqlalchemy import create_engine


def convert_to_blob(row):
    vector = row.values.astype(np.float32)
    return vector.tobytes()


def load_csv():
    df_essays = pd.read_csv('./csv/papers.csv')
    df_feats = pd.read_csv('./csv/feats.csv', header=None)
    df_feats.columns = [f'feature_{i + 1}' for i in range(128)]
    df_feats['features'] = df_feats.apply(convert_to_blob, axis=1)
    df = pd.concat([df_essays, df_feats['features']], axis=1)
    print("load_csv() finished!")
    return df


def load_essay():
    # Establish database connection.
    engine = create_engine('sqlite:///db.sqlite3')

    # Writing dataframe into database.
    df = load_csv()
    df.to_sql('linked_papers_essay', con=engine, if_exists='replace', index=False)

    # Convert dataframe into Essay object list.
    papers = [
        Essay(title=row['title'],
              abstract=row['abstract'],
              publish_year=row['year'],
              category=row['category'],
              features=row['features'])
        for index, row in df.iterrows()
    ]

    # Insertion.
    Essay.objects.bulk_create(papers)
    print("load_essay() finished!")
