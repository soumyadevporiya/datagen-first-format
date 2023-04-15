import json
from time import sleep
from kafka import KafkaProducer
import time
import random
import string

if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers=['35.225.83.11:9094'], api_version=(0, 10))

    big_count = 0

    while 1 == 1:
        count = 0
        cust_id = []
        name = []
        Time = []
        partition_field = []
        while 1 == 1:
            count = count + 1
            x = "INSBI" + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9)) + \
                str(random.randint(0, 9))
            cust_id.append(x)
            name.append(random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters) +
                        random.choice(string.ascii_letters))
            Time.append(int(round(time.time())))
            partition_field.append(int(x[5:7]))

            if count == 2000:
                break

        s = {
            "id": cust_id,
            "name": name,
            "Time": Time,
            "partition_field": partition_field
        }
        # print(s)
        producer.send('my-datagen1-topic', json.dumps(s).encode('utf-8'))
        big_count = big_count + count
        sleep(0.1)
        print("Big Count:  " + str(big_count))
        if big_count == 10000000:
            if producer is not None:
                producer.close()
            break
