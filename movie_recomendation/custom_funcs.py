import pandas as pd 
from sklearn.model_selection import StratifiedShuffleSplit


def initial_sss(df, label, test_size, out_file):
    """
    This funtion splits data into three parts:
     - train_df(dataframe containing both train data and labels)
     - test_df(dataframe containing just test data to be passed to predict on)
     - test_df_y_true(labels for test_df)
    Function uses StratifiedShuffleSplit from sklearn.model_selection
    :param df: pandas.DataFrame to be split
    :param label: name of the label column
    :param test_size: int from 0 to 1, percentage of data thats gonna be in test_df
    :param out_file: pathlib.Path() object, absolute path to directory where the split data shoould go
    :return: None
    """

    sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size,
                                 random_state=42)

    print(f'Spliting data: \n With shape of: {df.shape} \n Label being: {label} \n Output path: {out_file}')

    for train_index, test_index in sss.split(df, df[label]):
        train_df = df.iloc[train_index]
        test_df = df.iloc[test_index]

    print(f'Train shape: {train_df.shape}')
    print(f'Test shape: {test_df.shape}')

    train_df.to_csv(out_file / 'train_df.csv', index=False)
    test_df.drop(label, 1).to_csv(out_file / 'test_df.csv', index=False)
    test_df[label].to_csv(out_file / 'test_df_y_true.csv', index=False)

    print('Split successful')
