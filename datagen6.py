import json
from time import sleep
from kafka import KafkaProducer
import time
import random
import string


if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers=['35.225.83.11:9094'], api_version=(0, 10))

    count = 0


    while (1 == 1):
        count = count + 1
        x = "INSBI"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        partition_field = int(x[5:6])

        s = {
              "id": x,
              "name": random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters),
              "Time": int(round(time.time())),
              "partition_field": partition_field
            }
        #print(s)
        producer.send('my-datagen1-topic', json.dumps(s).encode('utf-8'))
        sleep(0.001)
        #if count == 5:
            #break





