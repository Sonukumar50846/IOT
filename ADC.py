from gpiozero import MCP3008
import time

pot = MCP3008(7)

while True:
    print(pot.value * 100)
    time.sleep(1)
