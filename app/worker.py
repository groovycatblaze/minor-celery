import logging
import redis
from rq import Worker, Queue, Connection
from rq.job import Job
from rq.registry import FailedJobRegistry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

REDIS_HOST = "redis"
REDIS_PORT = 6379

def main():
    try:
        redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        
        # Test connection
        redis_conn.ping()
        logging.info("Connected to Redis successfully.")

        with Connection(redis_conn):
            queue = Queue()

            worker = Worker(
                [queue],
                connection=redis_conn,
                name="distributed-worker-1"
            )

            logging.info("Worker started. Listening for tasks...")
            worker.work(with_scheduler=True)

    except Exception as e:
        logging.error(f"Worker failed to start: {e}")

if __name__ == "__main__":
    main()
