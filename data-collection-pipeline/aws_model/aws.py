import ast
import csv

TRAIN_DATA = [line.rstrip('\n') for line in open('final.txt')]
TRAIN_DATA = [list(ast.literal_eval(blog)) for blog in TRAIN_DATA]
TRAIN_DATA = [nested_info for blog in TRAIN_DATA for nested_info in blog]
print(len(TRAIN_DATA))
TRAIN_DATA = [data for data in TRAIN_DATA if data[1]['entities'] != []]



with open("entitylist.csv", "w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Text", "Type"])
    for i in range(len(TRAIN_DATA)):
        number=0
        second_number=0
        written_before=False
        if len(TRAIN_DATA[i][1]['entities'])>1:
            entity_length=len(TRAIN_DATA[i][1]['entities'])
            for j in range(entity_length):
                if j==entity_length-1:
                    csv_writer.writerow([TRAIN_DATA[i][0][TRAIN_DATA[i][1]['entities'][number+1 if written_before==False else second_number+1][0]:TRAIN_DATA[i][1]['entities'][j][1]], TRAIN_DATA[i][1]['entities'][number+1 if written_before==False else second_number+1][2].upper()])
                    break
                if int(TRAIN_DATA[i][1]['entities'][j][1]) + 1 == int(TRAIN_DATA[i][1]['entities'][j+1][0]):
                    number=-1    
                else:
                    number=j
                    second_number=j
                    csv_writer.writerow([TRAIN_DATA[i][0][TRAIN_DATA[i][1]['entities'][0 if written_before==False else j][0]:TRAIN_DATA[i][1]['entities'][j][1]], TRAIN_DATA[i][1]['entities'][j][2].upper()])
                    written_before=True

        else:
            csv_writer.writerow([TRAIN_DATA[i][0][TRAIN_DATA[i][1]['entities'][0][0]:TRAIN_DATA[i][1]['entities'][0][1]], TRAIN_DATA[i][1]['entities'][0][2].upper()])

                

#csv_writer.writerow([TRAIN_DATA[i][0][TRAIN_DATA[i][1]['entities'][0][0]:TRAIN_DATA[i][1]['entities'][-1][1] if len(TRAIN_DATA[i][1]['entities']) > 1 else TRAIN_DATA[i][1]['entities'][0][1]], TRAIN_DATA[i][1]['entities'][0][2]]) 

