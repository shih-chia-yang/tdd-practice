import ftplib

ftp=ftplib.FTP_TLS('tgftp.nws.noaa.gov')
print(ftp.login())
ftp.cwd('data')
print(ftp.nlst())
with open('kord.txt','wb') as file:
    ftp.retrbinary('RETR observations/metar/decoded/KORD.TXT',file.write)
