import schedule
import time 

def dizer_oi():
    print("Opa, tudo bem?")
    
    
schedule.every(3).seconds.do(dizer_oi)
while True:
    schedule.run_pending()
    time.sleep(1)