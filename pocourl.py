    # @ pr0fsr
    
    # pr0fsr007@gmail.com
    
def showbanner():
	    print("""
   ___                           _ 
  / _ \___   ___ ___  /\ /\ _ __| |
 / /_)/ _ \ / __/ _ \/ / \ \ '__| |
/ ___/ (_) | (_| (_) \ \_/ / |  | |
\/    \___/ \___\___/ \___/|_|  |_|
                                   
                           @ pr0fsr
                           
PocoUrl is a url shortener powered by tinyurl.com
    
Usage: python3 pocourl.py [ URL ]
       python3 pocourl.py http://google.com  
""")
def importerror():
        print("""
   ___                           _ 
  / _ \___   ___ ___  /\ /\ _ __| |
 / /_)/ _ \ / __/ _ \/ / \ \ '__| |
/ ___/ (_) | (_| (_) \ \_/ / |  | |
\/    \___/ \___\___/ \___/|_|  |_|
                                   
                           @ pr0fsr

No Module found! 
[+] pip3 install -r requirements.txt
""")
try:
	import sys
	import pyshorteners
	origurl=str(sys.argv[1])
	objects=pyshorteners.Shortener()
	shorturl=objects.tinyurl.short(origurl)
	print("\t[+] ORIGINAL URL: "+origurl)
	print("\t[+] POCOURL: "+shorturl)
except IndexError:
	showbanner()
except ImportError:
    importerror()

