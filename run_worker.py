from redis import Redis
from rq import Queue
from rq.worker import SimpleWorker

# Connect to Redis
redis_conn = Redis(
    host="localhost",
    port=6379
)

# Connect to the default queue
queue = Queue("default", connection=redis_conn)

# Create the worker
worker = SimpleWorker([queue], connection=redis_conn)

print("🚀 Worker started. Waiting for jobs...")

# Start listening for jobs
worker.work()