#!/usr/bin/env bash

$input=$1
$output=$2
rm -r $output

STARTTIME=$(date +%s)

python preprocess.py $input $output
ENDTIME=$(date +%s)
echo "Parsed all the files in $[$ENDTIME - $STARTTIME] seconds"
First = $STARTTIME+$ENDTIME

cd $output


STARTTIME=$(date +%s)

cat *.txt > AllTokensOneFile.txt

<AllTokensOneFile.txt \
tr -sc '[:alpha:]' '[\n*]' | sort |uniq -c |sort -nr >SortedByFrequency.txt

<AllTokensOneFile.txt \
tr -sc '[:alpha:]' '[\n*]' | sort |uniq -c   >SortedByTokens.txt

ENDTIME=$(date +%s)
echo "Sorting took $[$ENDTIME - $STARTTIME] seconds"



