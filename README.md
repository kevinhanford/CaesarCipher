<h1>Caesar Cipher</h1>

<h2>Description</h2>
The project consists of a simple Python script that emulates the widely know Caesar cipher that was used by the roman general Julius Caesar in order to protect messages of military significance from prying eyes. The script has several command line arguments to invoke the functionality and is intended to demonstrate the functionality of the Caesar cipher through the use of Python.


<h2>Languages and Utilities Used</h2>

- <b>Python 3.7.4</b>

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Usage</h2>

To get the code run this from the command line:

```commandline
git clone https://github.com/kevinhanford/CaesarCipher.git
```

Once that is done, in the main directory where `caesar_cipher.py` is located run:

```commandline
python caesar_cipher.py -h
```

The following will be displayed:

```commandline
usage: caesar_cipher.py [-h] -m M -s S

optional arguments:
  -h, --help  show this help message and exit
  -m M        The mode (encrypt or decrypt)
  -s S        The shift value
```

There is an Example.txt file provided that contains the message to be encrypted:

Hello, World!

To encrypt the message run the following:

```commandline
python .\caesar_cipher.py -m encrypt -s 1
```

The encrypted contents will be written to a Encrypted.txt file:

Ifmmp, Xpsme!

To decrypt the message run the following:

```commandline
python .\caesar_cipher.py -m decrypt -s 1
```

The decrypted contents will be written to a Decrypted.txt file:

Hello, World!

Note:
In order to change the message to encrypt just update the Example.txt file and run through steps again.
