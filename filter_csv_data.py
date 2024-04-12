"""
Author: Zeeshan Mumtaz
Date: Mar 28, 2024
Description: This script is used to split a huge csv file (Dateset)
based on the publication names. It is useful to train an AI/ML model for various purposes, 
such as classification or Sentiment Analysis.

Two main libraries are used which can be installed using:

pip install pandas :    Powerful data structures for data analysis, time series, and statistics
pip install tqdm   :    Fast, Extensible Progress Meter
"""


import pandas as pd
from tqdm import tqdm
import os

def split_csv_by_publication(csv_file):
    # Count the total number of rows in the CSV file
    total_rows = sum(1 for line in open(csv_file, encoding='utf-8'))

    # total_rows = sum(1 for line in open(csv_file))

    # Chunk size for reading the CSV file
    chunksize = 10000  # Adjust as needed

    # Initialize tqdm to track progress
    progress_bar = tqdm(total=total_rows, desc='Processing')

    # Iterate over chunks of the CSV file
    for chunk in pd.read_csv(csv_file, chunksize=chunksize):
        # Group the chunk by the 'publication' column and iterate over groups
        for publication, group in chunk.groupby('publication'):
            # Write the group to a separate CSV file
            output_file = f"{publication.replace(' ', '_').lower()}_data.csv"
            group.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))
            # Update tqdm progress bar
            progress_bar.update(len(group))

    # Close tqdm progress bar
    progress_bar.close()

# Specify the CSV file
csv_file = 'all-the-news-2-1.csv'  # Update with your CSV file path

# Split the CSV file by publication
split_csv_by_publication(csv_file)
