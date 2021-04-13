#! /usr/bin/env python

import pandas as pd
import argparse

import gspread
from gspread_dataframe import get_as_dataframe

#from IPython import embed

# Local imports
from helper import primary_tags


def main():
    parser = argparse.ArgumentParser(description='Pulls data from Google spreadsheet into Pandas DataFrame and dumps to CSV.',
                                     formatter_class=lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog)
                                     )
    parser.add_argument('--output', '-o', type=str, default='output.csv', help='Output filename. Will be overwritten if it exists.')
    args = parser.parse_args()

    gc = gspread.oauth()
    sh = gc.open("Supply_Cost_Projections")
    dfs = []
    for worksheet in sh.worksheets():
        if worksheet.title.lower() in primary_tags:
            df_ = get_as_dataframe(worksheet, evaluate_formulas=True)
            token_line_indices = df_.index[df_.id.map(lambda x: str(x).startswith('-- Above this line:'))].tolist()
            assert len(token_line_indices) == 1, 'Could not find special "-- Above this line:..." line in worksheet: %s' % worksheet.title
            token_line_index = token_line_indices[0]
            df_ = df_[:token_line_index]
            dfs.append(df_)
            print('Loaded worksheet: "%s"' % worksheet.title)
    df = pd.concat(dfs, ignore_index=True)
    df.fillna('', inplace=True)

    with open(args.output, 'w') as ff:
        df.to_csv(ff, index=False, float_format='%g')
        print('Saved DataFrame to', args.output)


if __name__ == '__main__':
    main()
