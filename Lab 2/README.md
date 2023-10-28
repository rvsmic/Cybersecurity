# Laboratorium 2

## Linki:
[PDF Zadania](Lab%201/lab1-student.pdf) | [PDF Odpowiedzi](Lab%201/lab1-admin.pdf) | [Potrzebne pliki](Lab%202/Pliki-1.zip)

## Teoria:

### Łamanie hashy:
* johntheripper - wersja jumbo z githuba
* hashcat - nie działa w pracowni

**Podczas łamania hashy warto sprawdzić jaki algorytm został użyty:**
[Baza przykładowych hashy](https://hashcat.net/wiki/doku.php?id=example_hashes)

### Słowniki z hasłami
/usr/share/wordlists/rockyou.txt.gz

*rozpakowac gzip -d rockyou.txt.gz*

### Reguły programu johntheripper

Można edytowac /etc/john/john.conf żeby dodawać swoje reguły

np. dla zadania 1.5 dodaliśmy na koniec tego pliku:
```
[Incremental:ZADANIE15]
File=$JOHN/utf8.chr
MinLen=3
MaxLen=3
CharCount=196
```

## Zadania:

### 1.5
```
crunch 3 3 abc + 468 ?%: -t @%^ > z15.txt

while read line; do echo -n "$line" | openssl dgst -sha3-512; done < z15.txt
```

### 1.6
```
john hash16.txt     <- czasem zadziala

john --format=raw-md5 hash16.txt

john --format=raw-md5 --wordlist="/usr/share/wordlists/rockyou.txt" hash16.txt

john --show --format=raw-md5 hash16.txt
```

### 1.7
```
john --list=formats 

john --format=raw-sha256 --wordlist="/usr/share/wordlists/rockyou.txt" hash17.txt

john --show --format=raw-sha256 hash17.txt
```

### 1.8
```
openssl dgst -md5 gparted-live-1.5.0-6-amd64.iso

md5sum gparted-live-1.5.0-6-amd64.iso

sha1sum gparted-live-1.5.0-6-amd64.iso
```

### 1.9
**[Skrypt python](zad19.py)**

### 1.13
```
hashcat -a 0 -m 0 hash16.txt /usr/share/wordlists/rockyou.txt
```

### 1.14
```
john z2.shadow

john z2.shadow --wordlist="/usr/share/wordlists/rockyou.txt"
```

### 1.15
```
john --incremental:ZADANIE15 z5.shadow
```