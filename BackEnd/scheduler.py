import schedule
import time
from main import Main

class Scheduler:
    chamada = Main()
    schedule.every(5).seconds.do(chamada.acionar)
    schedule.every(5).seconds.do(chamada.acionarWP)

    while True:
        schedule.run_pending()
        print("Chamada de main")
        time.sleep(10)
