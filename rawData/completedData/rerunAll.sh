#!/bin/bash
for i in $(\ls -d completedData/*)
do
	python calculate.py $i
done
