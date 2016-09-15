# ShortBox
Host files with size &lt; 150 mb for maximum two days  <br>
You will get a shortened url to the file and a url to delete the file from server

## Clone the repository 

`git clone https://github.com/DefCon-007/ShortBox.git`

## Install the required modules 

NOTE : Use python 3.x 

`cd ShortBox`

`pip3 install -r requirements.txt`

## Using the script

`python3 main.py <full path to file>`

The file will then be uploaded and afterwards you will be asked to 'optionally' provide a url 

![alt tag](http://i.imgur.com/TaMfuo8.png)

If you will leave this field blank it will automatically use the filename
<br><br>
Afterwards you will get the required two links :
<br><br>
Link to file : `http://tinyurl.com/SB-<Given name | filename>`
<br>and<br> 
Link to delete file : `http://tinyurl.com/del-<Given name | filename>`
