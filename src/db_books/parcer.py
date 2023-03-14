# Import pandas
import pandas as pd

# Read CSV file into DataFrame
# лол VScode запускает файл с окружением корня, поэтому путь буду писать целиком

df = pd.read_csv('./src/db_books/data/books.csv')

df_keys = {val: ind for ind,val in enumerate(list(df.columns))}

import math

def super_int(el):
    if math.isnan(el):
        return 0
    else:
        return int(el)
    
def super_float(el):
    if math.isnan(el):
        return 0
    else:
        return float(el)

if __name__ == "__main__":
    from model import Books

    for val in df.values:
        new_book = Books(title = val[df_keys['title']],
                         authors = val[df_keys['authors']],
                         categories = val[df_keys['categories']],
                         thumbnail = val[df_keys['thumbnail']],
                         description = val[df_keys['description']],
                         published_year = super_int(val[df_keys['published_year']]),
                         average_rating = super_float(val[df_keys['average_rating']]),
                         num_pages = super_int(val[df_keys['num_pages']]))
        new_book.save()
