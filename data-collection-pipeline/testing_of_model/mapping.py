import json
import logging
import sys
import subprocess
import re


def is_phrase_in(phrase, text):
    return re.search(r"\b{}\b".format(phrase), text, re.IGNORECASE) is not None


mapping='activities_composite_labels_dict.json'

with open(mapping, 'r') as f:
    mappings=json.load(f)

file = open(sys.argv[1], "r") 
blog_text=file.read().lower()
#print (blog_text)
#words = blog_text.split(' ')

mappings=dict(mappings)
for entity,name in mappings.items():
 #   entity=entity.lower()
    try:
        if is_phrase_in(entity, blog_text) is True:
            print (entity)
            for m in re.finditer(entity, blog_text,re.IGNORECASE):
                if entity.lower()==blog_text[m.start():m.end()]:
                    print(m.start(), m.end())
                    start_words=blog_text[0:m.start()]
                    start_words=start_words.split(' ')
                    end_words=blog_text[0:m.end()]
                    end_words=end_words.split(' ')

                    number_of_words_for_start=len(start_words)
                    number_of_words_for_end=len(end_words) +1
                    
 #                   in_between_words=number_of_words_for_end-number_of_words_for_start 
                    print (number_of_words_for_start)
                    print (number_of_words_for_end)
                    idx=0
                    for val  in range(number_of_words_for_start,number_of_words_for_end):
                        idx+=1
                        bash_cmd="sed -i.bak $'%ds/.*/%s\t%s/' %s" % (val,entity.split()[idx-1],name,sys.argv[2])
                        print (bash_cmd)
                        subprocess.run(bash_cmd, shell=True, check=True)
                        

                        print (entity)
                        print (name)
    except:
          print ('error')
 #         print (entity)
          #print (name)
                
#             subprocess.run('ls -l',shell=True, check=True)
#use m.start() to find the index of blog_text then use split.() to count number of words. do the same for m.end()


          
#replace the 1 with your line number which is end - start 
#sed $'1s/.*/replacement-line\tasd/' local-things-to-do-in-hanoi-vietnam_scraped_raw.tsv > new_file.tsv

