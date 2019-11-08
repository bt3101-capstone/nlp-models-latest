
#removes last char of string
#echo "${a%?}"
#sed -i.bak 's/.$//' weblinks.txt
#sed 's/.$//' weblinks.txt > web2links.txt

while read line;
    do echo $line;
    python curatour.py $line "${line##*/}"_scraped_raw.txt
    java -cp stanford-ner.jar edu.stanford.nlp.process.PTBTokenizer "${line##*/}"_scraped_raw.txt > "${line##*/}"_scraped_raw.tok
    perl -ne 'chomp; print "$_\tO\n"' "${line##*/}"_scraped_raw.tok > "${line##*/}"_scraped_raw.tsv
    cut -f1 "${line##*/}"_scraped_raw.tsv | paste -sd " " - > "${line##*/}"_scraped_raw_2.txt
    python mapping.py $"${line##*/}"_scraped_raw_2.txt  "${line##*/}"_scraped_raw.tsv



    python convert_to_json.py "${line##*/}"_scraped_raw.tsv "${line##*/}"_scraped_raw.json
    python convert_to_json_spacey.py -i "${line##*/}"_scraped_raw.json -o "${line##*/}"_scraped_raw_final.json >> final_test.txt
   # sed -i.bak 's/$/,/' final.json
   # echo -n ',"' >> final_web_link.json
   # echo -n $line >> final_web_link.json
   # echo -n '",' >> final_web_link.json
done < weblink_test.txt


