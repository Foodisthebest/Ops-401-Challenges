# Ops Challenge 06 1 0f 3

A Python script that encrypts a single file or block of text.

```bash
$ ./opschallenge7.py --help
usage: opschallenge7 [-h] (-E | -D) -k KEY [-m [MESSAGE ...] | -f FILE | -F FOLDER]

Helpful file encryption tool.

options:
  -h, --help            show this help message and exit
  -E, --ENCRYPT         Encrypt
  -D, --DECRYPT         Decrypt
  -k KEY, --key KEY     Location of key file
  -m [MESSAGE ...], --message [MESSAGE ...]
                        Message
  -f FILE, --file FILE  Location of file to Decrypt/Encrypt
  -F FOLDER, --FOLDER FOLDER
                        Location of folder to Decrypt/Encrypt

Thanks for using opschallenge7! :)
```

## Example Encrypting and Decrypting A Message

With the -E -m flags we encrypt the message 'Hi Mom'.

```bash
$ ./opschallenge7.py -k mykey2.key -E -m Hi Mom
gAAAAABluDaOqx5V_d7sbxbwx_uOqt0QRPp5IXJfrIO1nD8MbrGQoc4Pj_V08lwbwepPyPmjfsflhPH2MrN6WJH79TqVAeVqIg==
```

With the -D -m flags we decrypt the encrypted message.

```bash
$ ./opschallenge7.py -k mykey2.key -D -m gAAAAABluDaOqx5V_d7sbxbwx_uOqt0QRPp5IXJfrIO1nD8MbrGQoc4Pj_V08lwbwepPyPmjfsflhPH2MrN6WJH79TqVAeVqIg==
Hi Mom
```

## Example Encrypting and Decrypting a File

With the -E -f flags we encrypt the file.

```bash

$ cat mysample.txt 
Hi this is a file dedicated to loving cake.

$ ./opschallenge7.py -k mykey2.key -E -f mysample.txt 
File /home/woodstock/Ops-401-Challenges/opschallenge06/mysample.txt encrypted successfully.

$ cat mysample.txt 
gAAAAABluDfJCdmQz3KsZrmzRFGbLxJh9otjDFjvozDiwTo3xJtFy_SZWAvFVDNh96O5EnsJpygsbqryaFjaInl-BtvFz0niZBqm5cDcVcNMzIFvSBWENGamwyoUlGbgbSMy28Klmtcg

```

with the -D -f flags we decrypt the file.

```bash
$ ./opschallenge7.py -k mykey2.key -D -f mysample.txt 
File /home/woodstock/Ops-401-Challenges/opschallenge06/mysample.txt decrypted successfully.

$ cat mysample.txt 
Hi this is a file dedicated to loving cake.
```

## Example Encryping and Decrypting a Folder

With the -E -F flags we encrypt a folder.

```bash
$ ./opschallenge7.py -k mykey2.key -E -F test 
Folder /home/woodstock/Ops-401-Challenges/opschallenge06/test encrypted successfully.
```

With the -D -F flags we decrypt the folder contents.

```bash
$ ./opschallenge7.py -k mykey2.key -D -F test 
Folder /home/woodstock/Ops-401-Challenges/opschallenge06/test decrypted successfully.
```