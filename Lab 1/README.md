# Laboratorium 1

## Linki:
[PDF Zadania](/Lab%201/lab1-student.pdf) | [PDF Odpowiedzi](/Lab%201/lab1-admin.pdf) | [Potrzebne pliki](/Lab%202/Pliki-1.zip)

## Teoria:

Hash powinien zawsze dać to samo wyjście z danego wejścia

### Właściwości funkcji hashującej:
- łatwo otrzymać hash z tekstu jawnego
- niemożliwe otrzymać tekst jawny z hasha
- hash zawsze określonej długości
- mała zmiana tekstu jawnego powoduje dużą zmianę hasha

```
hello --> (openssl,   md5) --> xasda
hello --> (generator, md5) --> xasda
Hello --> (openssl,   md5) --> dfgdf
```

### Przy hashowaniu trzeba uważac na znak nowej linii na końcu wiadomości!

```
echo -n "hello" > ex1.txt
```
a nie 
```
echo "hello" > ex1.txt
```
żeby nie dodało newline

### | -  pipe / potok - jeżeli chcemy ominąć użycie pliku

```
echo -n "hello" | base64
echo -n "hello" | openssl dgst -md5 
echo -n "hello" | base64 | cut -c 2
```

## Zadania:

### 1.1
```
openssl rand -base64 4

openssl dgst -md5 ex1.txt

openssl rand -base64 4 | openssl dgst -md5
```

### 1.2
```
head /dev/urandom | base64 | tr -cd [:alnum:] | head -c 16 | openssl dgst -md5

cat /dev/urandom | base64 | head -n 1 | tr -cd [:alnum:] | cut -c -16 | openssl dgst -md5
```

### 1.3
```
crunch 3 3 0123456789 > setki.txt
```
~~crunch 3 3 0123456789 | openssl dgst -sha1 > setki.txt~~
```
while read line; do echo -n "$line" | openssl dgst -sha1; done < w1.txt
```

