fname=$1

while read cipher; do
	echo $cipher
	openssl enc -d -$cipher -in ex2.12.enc -K a35febba42490abe -a
done < $fname
