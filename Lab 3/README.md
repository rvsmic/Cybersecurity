# Laboratorium 3

## Linki:
[PDF Zadania](Lab%203/lab2-student.pdf) | [PDF Odpowiedzi](Lab%203/lab2-admin.pdf) | [Potrzebne pliki](Lab%203/Pliki-2.zip)

## Teoria:

Szyfrowanie powinno zawsze dać to samo wyjście z danego wejścia przy tym samym kluczu - **działa również w drugą stronę**

### Właściwości funkcji szyfrującej:
- łatwo otrzymać tekst zaszyfrowany z tekstu jawnego
- łatwo otrzymać tekst jawny z tekstu zaszyfrowanego
- do szyfrowania używa się pewnego klucza za pomocą którego potem następuje odszyfrowanie
- hello --> (klucz) --> asdas
asdas --> (klucz) --> hello

## Zadania:

### 2.1

#### Zaszyfrowanie
```
openssl enc

openssl enc -aes-256-ecb -in ex2.1.txt -K 5268db004820e65f0d224d86b207b01b02f787d2b8ff060ef63de965ca595f14 | base64
lub
openssl enc -aes-256-ecb -in ex2.1.txt -K 5268db004820e65f0d224d86b207b01b02f787d2b8ff060ef63de965ca595f14 -a

openssl enc -aes-256-ecb -in ex2.1.txt -K 5268db004820e65f0d224d86b207b01b02f787d2b8ff060ef63de965ca595f14 -a -out ex2.1.enc
```

#### Odszyfrowanie
```
openssl enc -d -aes-256-ecb -in ex2.1.enc -out ex2.1.dec -a -K 5268db004820e65f0d224d86b207b01b02f787d2b8ff060ef63de965ca595f14
```

### 2.2
```
openssl enc -d -aes-256-ecb -in ex2.2.enc -K 8b5636e632bf3c0f2cb2becd9a1113a80198e7aa3e01dfda047abf26f1be2dd0 -a

openssl enc -d -aes-256-ecb -in ex2.2.enc -K 8b5636e632bf3c0f2cb2becd9a1113a80198e7aa3e01dfda047abf26f1be2dd0 -a -out ex2.2.dec

cat ex2.2.dec | base64 -d
```

### 2.4
```
openssl enc -d -aes-256-cbc -in ex2.4.enc -kfile ex2.4.pass -pbkdf2 -out ex2.4.dec -a 

cat ex2.4.dec | base64 -d
```

### 2.9
```
zip2john ex2.9.zip > ex2.9.john

john ex2.9.john --wordlist=/usr/share/wordlists/rockyou.txt 
```

### 2.10
```
crunch 5 6 1234567890 > slownik.txt

zip2john ex2.10.zip > ex2.10.john

john ex2.10.john --wordlist=slownik.txt
```

### 2.12
Najpierw:
```
openssl list --cipher-commands | xargs -n1 > ciphers.txt
```
a potem:

**[Skrypt](skrypt.sh)**

### 2.13
```
openssl enc -d -seed-ecb -K 43326a0f538c1e210dcc87fc8988ace3 -a -in ex2.13.txt -out ex2.13.png
```