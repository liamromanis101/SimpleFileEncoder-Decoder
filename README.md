# SimpleFileEncoder-Decoder
Encodes files into ASCII hex in order to bypass AMSI.. works against Microsoft Defender as of 05/12/2024. 

This is just for transfering plaintext files text files like .bat, .cmd, .ps1. 

# Encoder
Run as follows:
```python3 encoder.py <file to be encoded> encoded-file.txt```

# Decoder
Run as follows:
```decoder.bat encoder-file.txt```

# ToDo
Creating a batch file to use Powershell to decode the file in memory, and then execute the file in memory using powershell. 
