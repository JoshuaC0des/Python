import random
import time

btc = random.randint(18000, 124000)
eth = random.randint(1400, 4000)
link = random.randint(9, 29)

print(f"Starting prices:\nBTC: ${btc}\nETH: ${eth}\nLINK: ${link}\n")

while True:

    btc_change = random.randint(-500, 500)
    eth_change = random.randint(-50, 50)
    link_change = random.uniform(-1, 1)

    btc += btc_change
    eth += eth_change
    link += link_change

    
    link = round(link, 2)

    
    print(f"Updated prices:\nBTC: ${btc} ({btc_change:+})\nETH: ${eth} ({eth_change:+})\nLINK: ${link} ({link_change:+.2f})\n")

    
    time.sleep(10)
