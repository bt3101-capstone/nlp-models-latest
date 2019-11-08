import ast
import csv

TRAIN_DATA = [line.rstrip('\n') for line in open('final_test.txt')]
TRAIN_DATA = [list(ast.literal_eval(blog)) for blog in TRAIN_DATA]
TRAIN_DATA = [nested_info for blog in TRAIN_DATA for nested_info in blog]
print(len(TRAIN_DATA))
TRAIN_DATA = [data for data in TRAIN_DATA if data[1]['entities'] != []]


file = open("raw_file_1.txt","w") 

for i in range(len(TRAIN_DATA)):
    if len(TRAIN_DATA[i][1]['entities'])==1:
        file.write(TRAIN_DATA[i][0]+"\n")

file.close() 
