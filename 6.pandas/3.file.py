from pandas import Series
import pandas as pd


def csv_file():
    f_df = pd.read_csv('6.pandas/test.csv', na_values=["missing"])  # 读入 Dataframe
    print(f_df)
    print(f_df['Sex'].value_counts()['male'])
    print(f_df['Sex'].describe())
    print(f_df['Age'].sum())
    print(f_df['Age'].isnull().value_counts())
    print(f_df['PassengerId'].isnull().value_counts())
    print(f_df['Cabin'].isnull().value_counts())
    print(f_df.isnull().value_counts())


# csv_file()


def read_chunker():
    chunker = pd.read_csv('6.pandas/test.csv', chunksize=100)  # 分成100行一块读出
    print(type(chunker))
    total = 0
    statistic = Series([])
    for piece in chunker:  # 每个piece 是一个 DataFrame
        print("num:", piece.index.size)
        print(piece['Sex'].value_counts())
        total += piece.index.size
        statistic = statistic.add(piece['Sex'].value_counts(), fill_value=0)
    print("total:", total)
    print(statistic)


# read_chunker()


def write_file():
    chunker = pd.read_csv('6.pandas/test.csv', chunksize=100)  # 分成100行一块读出
    next(chunker).to_csv('6.pandas/output.csv', sep=',')


write_file()
