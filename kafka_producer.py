from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "sensor_id": random.randint(1, 5),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 90), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("sensor_data", data)
    print("Dato enviado:", data)

    time.sleep(2)