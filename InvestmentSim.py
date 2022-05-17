
# Developed by AFK-Waffles on github


import time
import random
import sys
import argparse
# -----------------------------------------------VARIABLES

Day = 1
BTC = round(random.uniform(25000,30000),2)
ETH = round(random.uniform(1900,3000),2)
DOGE = round(random.uniform(0.40,2),2)

Balance = 100

# ---------------------------------------------- VARIABLES




print("""\n▄█    ▄       ▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄█    ▄     ▄▀  
██     █       █  █▀   ▀   █     ▀▄ ▀▀▀ █    ██     █  ▄▀    
██ ██   █ █     █ ██▄▄   ▄  ▀▀▀▀▄       █    ██ ██   █ █ ▀▄  
▐█ █ █  █  █    █ █▄   ▄▀ ▀▄▄▄▄▀       █     ▐█ █ █  █ █   █ 
 ▐ █  █ █   █  █  ▀███▀               ▀       ▐ █  █ █  ███  
   █   ██    █▐                                 █   ██       
             ▐                                               
   ▄▄▄▄▄   ▄█ █▀▄▀█   ▄   █    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄      
  █     ▀▄ ██ █ █ █    █  █    █ █ ▀▀▀ █    █   █ █  ▄▀      
▄  ▀▀▀▀▄   ██ █ ▄ █ █   █ █    █▄▄█    █    █   █ █▀▀▌       
 ▀▄▄▄▄▀    ▐█ █   █ █   █ ███▄ █  █   █     ▀████ █  █       
            ▐    █  █▄ ▄█     ▀   █  ▀              █        
                ▀    ▀▀▀         █                 ▀         
                                ▀                            """)


print("=== Day {} | 9:30 AM | Stock Market Opens! ===".format(Day))
print("[ Your wallet : $ {} ]\n".format(Balance))
print("• [BTC] 1 Bitcoin = ${}\n".format(BTC))
print("• [ETH] 1 Ethereum = ${}\n".format(ETH))
print("• [ETH] 1 DogeCoin = ${}\n".format(DOGE))

Buy = input("/ What cryptocurrency will you buy? [ BTC/ETH/DOGE ]\n>>> ")
if Buy != "BTC" and Buy != "ETH" and Buy != "DOGE":
  print test
