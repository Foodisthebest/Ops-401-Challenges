# Ops Challenge 06 1 0f 3

A Python script that encrypts a single file or block of text.

## Example Encrypting A Message

```bash
$ ./ops-401d-challenge06.py 
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 3
Enter the cleartext string: Hi Mom
Encrypted Message:
                  
gAAAAABlsIGp6qLI2GIkJQYTQlJcJMd_kur5tRKgYe4ocn3I7_BEEW_tNDuwVTXixSMQtaAfmfl9ShlX9lzUJCfbWok9drP59w==

                  
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 4
Enter the cleartext string: gAAAAABlsIGp6qLI2GIkJQYTQlJcJMd_kur5tRKgYe4ocn3I7_BEEW_tNDuwVTXixSMQtaAfmfl9ShlX9lzUJCfbWok9drP59w==
Decrypted Message:
                  
Hi Mom

                  
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 5
```

## Example Encrypting A File

Unencrypted `sample.txt`:
```bash
Hi Mom
```
Encrypted `sample.txt`:
```bash
gAAAAABlsIL5qZL5bl7z7oCl3A9V5ho55GBAaP35PKjYlqhNWk_70PcpNN9Yz_23GxZaKiA2FH2YQAsDkodAHHfwkOcq-wDFrA==
```
Example:
```
$ ./ops-401d-challenge06.py 
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 1
Enter the filepath to the target file: sample.txt
sample.txt encrypted successfully.
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 2
Enter the filepath to the target file: sample.txt
sample.txt decrypted successfully.
Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > 5
```

## Initial Installation Instructions

```bash
git clone $repo
cd $repo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
chmod +x ./opschallenge6.py 
```


## Simple setup

```bash
source .venv/bin/activate
```