# USING URLLIB to do all the common socket work and make the page look like a file
import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
