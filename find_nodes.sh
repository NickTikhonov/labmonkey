#!/bin/bash
dump_users() {
	ssh -o ConnectTimeout=1 $1.cs.st-andrews.ac.uk "who | grep -v 'unknown'" 2> /dev/null
}

for i in {001..100};
do
	dump_users pc2-$i-l
done

for i in {001..100};
do
	dump_users pc3-$i-l
done