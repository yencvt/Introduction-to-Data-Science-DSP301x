import pandas as pd
import numpy as np

answer_key = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'
arr_scores = []

def mark(row):
    arr_key = answer_key.split(',')
    scores = 0
    i=0
    for col in row:
        if i != 0 and col:
            if col == arr_key[i-1]:
                scores +=4
            else:
                scores -= 1
        i=i+1
    arr_scores.append([row[0], scores]) 

def write(df):
    rpPath = filename.strip()+'_grades.txt'
    with open(rpPath,'w') as f:
        for index, r in df.iterrows():
            f.write(str(r[0]) + ', ' + str(r[1]))
            f.write('\n')

filename = input("Enter a filename: ")
if filename:
    filePath = filename.strip()+'.txt'
    total_valid = 0
    total_invalid = 0
    arrlist = []
    with open(filePath, 'r') as file:
        print("Successfully opened ", filename)
        print('**** ANALYZING ****')
            
        for line in file:
            result = line.split(',')
            arrlist.append(result)
        file.close()
        df = pd.DataFrame(arrlist)
        
        invalid_1 =df.loc[(df.count(1) != 26)]
        invalid_2 = df.loc[(df[0].str.get(0) != 'N') | (~df[0].str[1:].str.isnumeric()) | (df[0].str.len() != 9)]
        valid = df.loc[(~df[0].isin(invalid_1[0])) & (~df[0].isin(invalid_2[0]))]
        
        valid.apply(lambda row:  mark(row), axis=1)
        df_scores = pd.DataFrame(arr_scores)
        df_scores = df_scores.sort_values([1], ascending=[True]).reset_index(drop=True)
        
        total_invalid = len(invalid_1) + len(invalid_2)
        total_valid = len(valid)
        mean_scores = round(df_scores[1].mean(), 2)
        highest_scores = df_scores[1].max()
        lowest_scores = df_scores[1].min()
        range_scores = highest_scores-lowest_scores
        median_score = np.median(df_scores[1])

        write(df_scores)
        print('Invalid line of data: does not contain exactly 26 values:')
        print(invalid_1)
        print('Invalid line of data: N# is invalid:')
        print(invalid_2)
        print('**** REPORT ****')
        print('Total valid lines of data: ', total_valid)
        print('Total invalid lines of data: ', total_invalid)
        print('Mean (average) score: ', mean_scores)
        print('Highest score: ', highest_scores)
        print('Lowest score: ', lowest_scores)
        print('Range of scores: ', range_scores)
        print('Median score: ', median_score)
else:
    print("Filename cannot be empty.")
