import csv
from time import time
import pandas as pd

def csv_to_list(file_name):
    folder = 'test/'
    file_name = folder + file_name
    df = pd.read_csv(file_name, delimiter=',')
    data = []
    data.append(df.columns.to_list())
    values = df.values.tolist()
    for val in values:
        data.append(val)
    return data

def list_to_table(list):
    table = """<table class="table table-hover">\n"""
    header = list[0]
    table += """  <tr>\n"""
    for column in header:
        table += """   <th>{0}</th>\n""".format(str(column).strip())
    table += """  </tr>\n"""
    row_data = list[1:]
    for line in row_data:
        table += """  <tr>\n"""
        for column in line:
            table += """    <td>{0}</td>\n""".format(str(column).strip())
        table += """  </tr>\n"""
    table += """</table>"""
    return table

def list_to_string(data):
    string = ""
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (j != (len(data[0])-1)):
                string += str(data[i][j]) + ","
            else:
                string += str(data[i][j])
        if (i != (len(data)-1)):
            string += '\n'
    return string

def string_to_list(input_string):
    result = []
    string = input_string.decode('UTF-8')
    rows = string.split('\n')
    for row in rows:
        cols = row.split(',')
        cols_list = []
        for col in cols:
            cols_list.append(col)
        result.append(cols_list)
    return result

def selection_sort(data, col_idx, orientation):
    start_time = time()
    N = len(data)
    for i in range(1,N):
        min_idx = i
        for j in range(i+1,N):
            if (orientation == "asc"):
                if data[min_idx][col_idx] > data[j][col_idx]:
                    min_idx = j
            else:
                if data[min_idx][col_idx] < data[j][col_idx]:
                    min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]   
    execution_time = time() - start_time     
    return data, execution_time

def bubble_sort(data, col_idx, orientation):
    start_time = time()
    N = len(data)
    for i in range(1,N-1):
        for j in range(1,N-i):
            if (orientation == "asc"):
                if data[j][col_idx] > data[j+1][col_idx]:
                    data[j], data[j+1] = data[j+1], data[j]
            else: 
                if data[j][col_idx] < data[j+1][col_idx]:
                    data[j], data[j+1] = data[j+1], data[j]
    execution_time = time() - start_time     
    return data, execution_time

def insertion_sort(data, col_idx, orientation):
    start_time = time()
    N = len(data)
    for i in range(1, N):
        key = data[i]
        j = i-1
        if (orientation == "asc"):
            while j > 0 and key[col_idx] < data[j][col_idx]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        else:
            while j > 0 and key[col_idx] > data[j][col_idx]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    execution_time = time() - start_time     
    return data, execution_time