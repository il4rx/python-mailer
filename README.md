# Requirements
Before you execute this script, you should download the library first, the important library to download is 
`smtp sever`, `pyfiglet`, `os`, `time`,`datetime`, and `platform`. the script is only work when the library is on or downloaded.
for `colorama` this library is not very important, on this case used for the display only. if you wan't to remove the **colorama**
from the line, you should remove the line that include ***import colorama*** and ***from colorama import Fore, Back, Style***
then removve the text while include the following text : `Fore, Back, Style`.

# How to Download
before you download the library, you should download python on your desktop, you should go to [Python Download](https://www.python.org/downloads/) to download. after you have download python, you will go to setup `pip`. pip stands for "preferred installer program". after you installed PIP, you should download
this all library. For the free documentation : [Python MIMEBase Documentation](https://docs.python.org/3/library/email.mime.html),

**colorama :** To download colorama, you should type [in python prompt] `pip install colorama`. this will download automaticaly <br>
**pyfiglet :** To download pyfiglet, you should type [in python prompt] `pip install pyfiglet`. this will download automaticaly <br>
**platform :** To download platform, you should type [in python prompt] `pip install platform`. this will download automaticaly <br>
<br>
`smtp` is automaticaly downloaded when you download python, but to activated the smtp server you need to use the following command
```py
$ python -m smtpd -c DebuggingServer -n localhost:1025
```
<br>
After you setup the smtp sever you is done, for os , time ,datetime is automaticaly downloaded when you start the python from the first time.
<br><br>
