# Laboratorium 6

## Linki:
[PDF Zadania](/Lab%206/zad4.pdf) | PDF Odpowiedzi

## Zadania:

### 4.16

#### Generowanie kluczy

##### Domyślny sposób
```
gpg --gen-key
```

##### Ustawienie specyfikacji klucza
```
gpg --full-generate-key
```

```
gpg --list-keys  
gpg --list-secret-keys
```

#### Eksportowanie klucza
```
gpg --output mrus.key --armour --export mmmmmm@gmail.com
```

#### Importowanie klucza
```
gpg --import mrus.key
```

#### Eksportowanie klucza na serwer
```
gpg --keyserver hkp://keys.openpgp.org --send-keys 5CA635D8A49C32D1268AC824658C1419F3C9C3B3
```

#### Importowanie klucza z serwera
```
gpg --keyserver hkp://keys.openpgp.org --recv 5CA635D8A49C32D1268AC824658C1419F3C9C3B3
```

#### Szyfrowanie pliku
```
gpg --encrypt --recipient A839B3064FD7B2A96114A849C48C61030504BA78 --armour --output heh.enc heh.txt
```

#### Deszyfrowanie pliku
```
gpg --decrypt --output heh.dec heh.enc 
```

