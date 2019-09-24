from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import boto3
import json
import sys


url = sys.argv[1]
print (sys.argv[2])
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    print ('hi')
    visible_texts = filter(tag_visible, texts)  
    print ('hi2')
    return u" ".join(t.strip() for t in visible_texts)

res = requests.get(url)
html = res.content

text = text_from_html(html)
file= open(sys.argv[2],"w")
print (sys.argv[2])
file.write(text)
file.close()



#comprehend = boto3.client(service_name='comprehend')
#
#print('Calling DetectEntities')
#print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
#print('End of DetectEntities\n')
