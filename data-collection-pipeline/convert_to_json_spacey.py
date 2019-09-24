import plac
import logging
import argparse
import sys
import os
import json
import pickle
import subprocess

@plac.annotations(input_file=("Input file", "option", "i", str), output_file=("Output file", "option", "o", str))



def main(input_file=None, output_file=None):
    try:
        training_data = []
        lines=[]
        with open(input_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            new_entities = []
            continuous = False
            for annotation in data['annotation']:
               
                point = annotation['points'][0]
    #            print ('point')
   #             print (point)
                labels = annotation['label']
 #               print ('labels')
  #              print (labels)
                if not isinstance(labels, list):
                    labels = [labels]

                for label in labels:
#                    print (entities)
                    
                    entities.append(tuple((point['start'], point['end'] + 1 ,label)))


            first=0
            last=0
 #           print (entities)
            for z in range(len(entities)):
#                print (z)
 #               last=z
                if z==len(entities) -1:
                    if continuous==True:
                        new_entities.append(adding_continous(entities[first:last+2]))
                    else:
#                       print (adding_continous(entities[z:z+3]))
                        new_entities.append(adding_continous(entities[z:z+3]))
                    break
                if int(entities[z][1])+1==int(entities[z+1][0]):
                    continuous=True
                    
                    if z==0:
                        first=z
                    last=z
                else:
#                    print (entities[0 if first==0 else first:z+1 if last==0 else last+1])
                    new_entities.append(adding_continous(entities[0 if first==0 else first:z+1 if last==0 else last+1]))
                    continuous=False
                    first=z+1
             


            new_entities=list(filter(None.__ne__, new_entities))
            training_data.append((text, {"entities" : new_entities}))

      #  subprocess.run("", shell=True, check=True)
        print(training_data)

        fp=open(output_file,'w')
        json.dump(training_data,fp)
 
#       print(training_data)

    except Exception as e:
        logging.exception("Unable to process " + input_file + "\n" + "error = " + str(e))
        return None

def adding_continous(c_list):
    if c_list==[]:
        pass 
    elif len(c_list)==1:

        return c_list[0]
    else:
        return (c_list[0][0], c_list[len(c_list)-1][1], c_list[0][2])


if __name__ == '__main__':
    plac.call(main)
