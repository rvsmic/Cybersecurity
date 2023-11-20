# Laboratorium 7

## Linki:
[PDF Zadania](/Lab%205/lab4-student.pdf) | PDF Odpowiedzi | [Potrzebne pliki](/Lab%205/Pliki-4.zip)

## Teoria:
### Sprawdzanie sygnatur na różne sposoby
```
gpg --gen-key	<- tworze klucz
echo "HEYYYY" > test.txt
```

#### 1 sposób
```
gpg --default-key 9DAEB2C771D319175E49739D60DB5BEFF60AE8A6 --output test1.asc --detach-sign test.txt
gpg --verify test1.asc test.txt 
```

#### 2 sposób
```
gpg --default-key 9DAEB2C771D319175E49739D60DB5BEFF60AE8A6 --output test2.asc --sign test.txt 
gpg --verify test2.asc
```

#### 3 sposób
```
gpg --default-key 9DAEB2C771D319175E49739D60DB5BEFF60AE8A6 --output test3.asc --clearsign test.txt
gpg --verify test3.asc
```

## Zadania:

### 4.12

#### Importowanie klucza
```
gpg --import mallory.pub
gpg --list-keys
```

#### Sprawdzenie podpisu
```
gpg --decrypt ex4.12.sig	<- sprawdzic czy jest informacja o good signature 
```
*(lub innymi sposobami wyżej)*

### 4.13

#### Weryfikacja oprogramowania / pliku

##### Sprawdzamy fingerprint
```
gpg VeraCrypt_PGP_public_key.asc
```

##### Importujemy klucz
```
gpg --import VeraCrypt_PGP_public_key.asc
```

##### Weryfikujemy podpis
```
gpg --verify veracrypt-console-1.26.7-Debian-12-amd64.deb.sig veracrypt-console-1.26.7-Debian-12-amd64.deb
```

### 4.14

#### Weryfikacja oprogramowania / pliku przez pgp i sha256

##### Importujemy klucz
```
gpg --import KEYS
```

##### Weryfikujemy podpis
```
gpg --verify httpd-2.4.58.tar.bz2.asc httpd-2.4.58.tar.bz2
```
lub

##### Weryfikujemy sha256
```
sha256sum httpd-2.4.58.tar.bz2
cat httpd-2.4.58.tar.bz2.sha256 
```

### 4.15

#### Podpisanie klucza
```
gpg --check-sigs
gpg --default-key 9DAEB2C771D319175E49739D60DB5BEFF60AE8A6 --sign-key 26F51EF9A82F4ACB43F1903ED377C9E7D1944C66
```


