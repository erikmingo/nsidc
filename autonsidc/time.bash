

# rm -rf crawls

start=`date +%s`

#bin/nutch crawl bin/urls -dir crawl -depth 4 -topN 16 -solr http://10.0.2.2:8983/solr/
ls -la

end=`date +%s`

runtime=$((end-start)) 

#how to make times, fetch2_queue2_modebyHost_
echo $runtime > times.txt

