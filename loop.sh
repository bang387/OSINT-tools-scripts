#!/bin/bash

s=1
e=10000
n=1
for ((i = 0; i<500; i++)) #no computer crash with 500
	do	
		sed -n "$s,$e"p tel08.txt > "$n".csv;
		((s=e))
		((e=e+10000))
		((n+=1))
		#echof s: $s
		#echo e: $e
		#sed -n 1,10p 0611109104 | cat -n
	done
