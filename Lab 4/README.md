# Laboratorium 4

## Linki:
[PDF Zadania](/Lab%204/lab3-student.pdf) | PDF Odpowiedzi | [Potrzebne pliki](/Lab%204/Pliki-3.zip)

## Teoria:

### Szyfrowanie symetryczne:
```
hello --> (alg. szyfr, KLUCZ) --> asdas
asdas --> (alg. szyfr, KLUCZ) --> hello
```

### Szyfrowanie asymetryczne:
```
hello --> (alg. szyfr, KLUCZ_PUBLICZNY) --> asdas
asdas --> (alg. szyfr,  KLUCZ_PRYWATNY) --> hello
```

#### Klucze - publiczny i prywatny:
```
OSOBA A: K_PUBL_A, K_PRYW_A
OSOBA B: K_PUBL_B, K_PRYW_B
```

#### Przesłanie kluczy:
```
OSOBA A --> wysyła K_PUBL_A --> OSOBA B
OSOBA B --> wysyła K_PUBL_B --> OSOBA A
```

#### Przeslanie wiadomości:
```
osoba A --> alg(wiad_1, K_PUBL_B) --> osoba B ~> odszyfrowuje z K_PRYW_B
osoba B --> alg(wiad_2, K_PUBL_A) --> osoba A ~> odszyfrowuje z K_PRYW_A
```

#### Podpisy wiadomości:
```
osoba A --> alg(wiad_1, K_PRYW_A <~podpis) --> osoba B
```

### Nie da się odszyfrować wiadomości jeżeli posiadamy tylko klucz publiczny  - potrzebny jest prywatny klucz!

## Zadania:

### 3.1
### Generowanie pary kluczy
Generuje się klucz prywatny - z niego się generuje klucz publiczny
```
openssl genrsa -out pair.pem 2048
```

### Wyodrębnienie klucza publicznego**
```
openssl rsa -in pair.pem -pubout
openssl rsa -in pair.pem -pubout -out pub.key
```

### Zapis do pliku klucza prywatnego
```
openssl rsa -in pair.pem --text > priv.key 
```

### 3.2
```
openssl ecparam -list_curves

openssl ecparam --name prime256v1 --genkey

openssl ecparam --name prime256v1 --genkey -out pairec.pem
```

### 3.3

#### Struktura polecenia szyfrującego
```
openssl rsautl -encrypt -inkey .. -pubin -in ...-a > zapis
```

#### Szyfrowanie:
```
openssl rsautl -encrypt -inkey ex3.3pub.key -pubin -in ex3.3.txt | base64

openssl rsautl -encrypt -inkey ex3.3pub.key -pubin -in ex3.3.txt | base64 > plik.prywatny

openssl rsautl -encrypt -inkey ex3.3pub.key -pubin -in ex3.3.txt -out zad3.3.szyfr
```

#### Porównanie z odpowiedzią za pomocą hasha
Jeżeli pliki mają taką samą zawartość to ich hashe będą takie same
```
cat ex3.3.enc | base64 > x.txt
```

### 3.4
```
openssl rsautl -decrypt -in ex3.4.enc -inkey ex3.4keys.pem -out ex3.4.dec 

cat ex3.4.dec | base64 -d
```

### 3.5

#### Wyeksportowanie klucza publicznego z pary kluczy
```
openssl rsa -in ex3.5keys.pem -pubout -out ex3.5.pubkey
```

#### Weryfikacja podpisu
```
openssl pkeyutl -verify -sigfile ex3.5.sig -in ex3.5.txt -inkey ex3.5keys.pem
```