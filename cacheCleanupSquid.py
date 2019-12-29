#!/usr/bin/env python3
# -*- coding; utf-8 -*-
from time import sleep
import os

class CacheSquid:
    def limparCache(self):
        os.system("/etc/init.d/squid3 stop")
        
        sleep(15)
        
        os.system("mv /var/spool/squid3 /var/spool/squid3.del")
        
        os.system("mkdir /var/spool/squid3")
        
        os.system("chmod 777 /var/spool/squid3")
        
        os.system("/var/spool/squid3 -z")
        
        sleep(3000)
        
        os.system("/etc/init.d/squid3 start")
        
        os.system("rm -rf /var/spool/squid3.del")

def main():
    cs = CacheSquid()
    cs.limparCache()

if __name__ == '__main__':
    main()
    




