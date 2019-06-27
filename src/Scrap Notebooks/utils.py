#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import networkx as nx


def load_impact_data(
    name='impact',
    path2rawdata='',
    duplicate_subset=['ArticleID'],
    year_list=None,
    columns=None,
    dropna=None,
    isindict=None,
    verbose=False,
    ):

    if year_list is None:
        year_list = [1900] + list(range(1945, 2017))
        year_list = map(str, year_list)

    file_df_list = []
    ifile = 0

    for year in year_list:
        for df_file in os.listdir(os.path.join(path2rawdata, name)):
            fname = os.path.join(path2rawdata, name, df_file)
            subdf = pd.read_hdf(fname, mode='r')

            if type(columns) is list:
                subdf = subdf[columns]

            if type(dropna) is list:
                subdf.dropna(subset=dropna, inplace=True, how='any')

            if type(isindict) is dict:
                for (isinkey, isinlist) in isindict.items():
                    subdf = subdf[isin_sorted(subdf[isinkey], isinlist)]

                # date tag to keep most recent entry
                # filetag = df_file.split('_')[2]
                # subdf['filetag'] = filetag

                file_df_list.append(subdf)

            ifile += 1
            if verbose and ifile % verbose == 0:
                print(ifile)

    df = pd.concat(file_df_list)

    # take most recent entries according to filetag

    df.drop_duplicates(subset=duplicate_subset, keep='last',
                       inplace=True)
    
    if verbose:
        print ('Final DF Shape', df.shape)

    return df
