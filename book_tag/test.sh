#!/bin/bash

for file in $(awk '{print $1}' ./md_list.txt);do
	grep '{\#.*}' $file
	# sed -i 's/{\#.*}//' $file
done
