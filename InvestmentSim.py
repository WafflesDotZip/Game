
# Developed by AFK-Waffles on github


import time
import random
import sys
# -----------------------------------------------VARIABLES

Day = 1
BTC = round(random.uniform(25000,30000),2)
ETH = round(random.uniform(1900,3000),2)
DOGE = round(random.uniform(0.40,2),2)
Afford = 0
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

Valid = ["BTC","ETH","DOGE"] # Outline all valid answers

while True:
  Buy = input("[>] What cryptocurrency will you buy? [ BTC/ETH/DOGE ]\n>>> ")
  Buy = Buy.upper()
  if not Buy in Valid: # IF BUY ( the input ) is not a valid andwer :
    print("[ERROR] Invalid response! Select either [ BTC / ETH / DOGE ]\n")
    continue
  if Buy in Valid: # IF answer is valid :
    break
# ----------------------------------------- CALCULATE AFFORDABILITY 

if Buy == "BTC":
  Afford = round(Balance / BTC,5)

if Buy == "ETH":
  Afford = round(Balance / ETH,5)

if Buy == "DOGE":
  Afford = round(Balance / DOGE,5)

# ---------------------------------------------
while True:
  try:
    Amount = float(input("[>] How much cash will you invest into {} ? You have ${}.\n>>> ".format(Buy,Balance)))
  except ValueError:
    print("[ERROR] Invalid response! Must be a number.\n")
    continue

