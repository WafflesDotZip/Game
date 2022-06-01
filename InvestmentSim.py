
# Developed by AFK-Waffles on github


import time
import random
import sys
# -----------------------------------------------VARIABLES

Day = 1
BTC = round(random.uniform(25000,30000),2)
ETH = round(random.uniform(1900,3000),2)
DOGE = round(random.uniform(0.40,2),2)

WalletBTC = 0
WalletETH = 0
WalletDOGE = 0

Afford = 0
Balance = 100

# ---------------------------------------------- VARIABLES




#print("""\n▄█    ▄       ▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄█    ▄     ▄▀  
#██     █       █  █▀   ▀   █     ▀▄ ▀▀▀ █    ██     █  ▄▀    
#██ ██   █ █     █ ██▄▄   ▄  ▀▀▀▀▄       █    ██ ██   █ █ ▀▄  
#▐█ █ █  █  █    █ █▄   ▄▀ ▀▄▄▄▄▀       █     ▐█ █ █  █ █   █ 
# ▐ █  █ █   █  █  ▀███▀               ▀       ▐ █  █ █  ███  
#   █   ██    █▐                                 █   ██       
#             ▐                                               
#   ▄▄▄▄▄   ▄█ █▀▄▀█   ▄   █    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄      
#  █     ▀▄ ██ █ █ █    █  █    █ █ ▀▀▀ █    █   █ █  ▄▀      
#▄  ▀▀▀▀▄   ██ █ ▄ █ █   █ █    █▄▄█    █    █   █ █▀▀▌       
# ▀▄▄▄▄▀    ▐█ █   █ █   █ ███▄ █  █   █     ▀████ █  █       
#            ▐    █  █▄ ▄█     ▀   █  ▀              █        
#                ▀    ▀▀▀         █                 ▀         
#                                ▀                            """)

print(r"""_________                        __                        
\_   ___ \_______ ___.__._______/  |_  ____                
/    \  \/\_  __ <   |  |\____ \   __\/  _ \               
\     \____|  | \/\___  ||  |_> >  | (  <_> )              
 \______  /|__|   / ____||   __/|__|  \____/               
        \/        \/     |__|                              
  _________.__              .__          __                
 /   _____/|__| _____  __ __|  | _____ _/  |_  ___________ 
 \_____  \ |  |/     \|  |  \  | \__  \\   __\/  _ \_  __ \
 /        \|  |  Y Y  \  |  /  |__/ __ \|  | (  <_> )  | \/
/_______  /|__|__|_|  /____/|____(____  /__|  \____/|__|   
        \/          \/                \/                   """)

print("")
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
  if Amount > Balance:
    print("[ERROR] Insufficient balance.\n")
    continue
  if Amount <= Balance:
#----------------------------------------------
    if Buy == "BTC":
      WalletBTC += round(Amount / BTC,5)
      Purchased = round(Amount / BTC,5)
      

    if Buy == "ETH":
      WalletETH += round(Amount / ETH,5)
      Purchased = round(Amount / ETH,5)
  
    if Buy == "DOGE":
      WalletDOGE += round(Amount / DOGE,5)
      Purchased = round(Amount / DOGE,5)
      
    Balance -= Amount
#------------------------------------------------
    print("\n[!! $ !!] You have converted ${} to {} {}.".format(Amount,Purchased,Buy))
    print("┏────── Your Wallet ──────┓\n┠ USD  ▌$ {}\n┠ BTC  ▌₿ {}\n┠ ETH  ▌Ξ {}\n┠ DOGE ▌Ð {}\n┗─────────────────────────┛".format(Balance,WalletBTC,WalletETH,WalletDOGE))
    break
