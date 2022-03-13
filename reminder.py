import requests,discord,os,platform
from datetime import datetime
import time as t
time = datetime.now()
while True:
  if time.hour==Reminder Time  or time.hour==Second REminder time: # Remove the second one if you don't need it. Do not use quotes while entering numbers.
        discord_webhook_url= 'Webhook Url'
        Message = {
            "content": "<@Your Discord Id> This is a reminder!"
        }
        requests.post(discord_webhook_url, data=Message)
        t.sleep(20)
  else:
    print("The time hasn't came yet!") #Remove if you have limited Cpu Power.
    t.sleep(10)
        


