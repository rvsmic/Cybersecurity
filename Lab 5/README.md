# Laboratorium 5

## Linki:
[PDF Zadania](/Lab%205/lab4-student.pdf) | PDF Odpowiedzi | [Potrzebne pliki](/Lab%205/Pliki-4.zip)

## Teoria:

PGP - dodatkowe szyfrowanie poczty email - wiadomości email idą przez wiele serwerów, gdzie nie ma szyfrowania

Protokół SMTP jest stary, więc PGP jest potrzebne dla bezpieczeństwa wiadomości

Jest to zaawansowane szyfrowanie asymetryczne

**GPG to darmowy odpowiednik PGP**

## Zadania:

### 4.1

#### Generowanie kluczy
```
gpg --gen-key
gpg --full-generate-key
```


### 4.2
```
gpg --full-generate-key
```

### 4.3

#### Edycja klucza
```
gpg --list-keys
gpg --edit-key E7F4196B23928DA70DBCFBF8840402D443EF589C		<- skopiowane id klucza

key 0
expire
quit

gpg --list-secret-keys
gpg -k 
```

### 4.4
```
gpg --list-keys
gpg --list-secret-keys
gpg -k 
```

### 4.5

#### Usunięcie klucza
```
gpg --delete-secret-keys 3BF9526797E2460E8DBFE7B1FAB8D302022B9168
gpg --delete-keys 3BF9526797E2460E8DBFE7B1FAB8D302022B9168 

gpg --list-keys --keyid-format SHORT
```

### 4.6
```
gpg --output michal.pubkey --armour --export michal@umcs.pl

gpg --show-keys michal.pubkey
```

### 4.7
```
gpg --output michal_bin.pubkey --export michal@umcs.pl
```

### 4.8

#### Wyslanie klucza na serwer
Najpierw wygenerować klucz jak wyżej i przekleić go do komendy
```
gpg --keyserver hkp://keyserver.ubuntu.com --send-keys E7F4196B23928DA70DBCFBF8840402D443EF589C
``` 
**Trzeba użyć 'hkp' zamiast 'https' w adresie serwera**

Potem wysłany klucz mozna znaleźć po 0x(ID) na https://keyserver.ubuntu.com

#### Importowanie klucza z serwera:
Serwer Ubuntu
```
gpg --keyserver hkp://keyserver.ubuntu.com --recv E7F4196B23928DA70DBCFBF8840402D443EF589C
```

Serwer OpenPGP + **podpis klucza**
```
gpg --keyserver hkp://keys.openpgp.org --recv FD3FAC1D1237BEB6EB235994E448A9BB9F0A7A99		<- nie dziala wiec uzywamy swojego

gpg --default-key 55B3526F237DA4DD302C1BC03B514398FCBCB2F4 --sign-key E7F4196B23928DA70DBCFBF8840402D443EF589C

gpg --check-sigs
```

### 4.9

#### Szyfrowanie pliku
```
gpg --symmetric --armor --cipher-algo AES256 --output zad4.9.enc zad4.9.txt

gpg --decrypt --output zad4.9.dec zad4.9.enc 
```

### 4.11
Generuje obu osobom klucze 
```
gpg --gen-key
```

Przykładowa wiadomość do zaszyfrowania:
```
echo "HEYYYY" > hello.txt 
```

Wysyłam do Boba:
```
gpg --encrypt --recipient CD6AA462047975849768A288BC555B14EF9685EB --armor --output hello.enc hello.txt
```

Bob odczytuje:
```
gpg --decrypt --output hello.dec hello.enc
```

### 4.12

#### Importowanie klucza z pliku
```
gpg --show-keys mallory.pub 

gpg --import mallory.pub
```
