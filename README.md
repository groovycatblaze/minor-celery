# scalable distributed task queue system

this project implements a minimal distributed task processing system inspired by celery. it uses fastapi for the api layer, redis as a message broker, and rq for asynchronous job execution.

the system allows clients to submit long-running tasks and check their status without blocking the main application.

## architecture

- fastapi api server
- redis as message broker
- rq worker for background processing
- docker-compose for orchestration

## features

- asynchronous task submission
- job id tracking
- status polling endpoint
- containerized multi-service setup
- scalable worker design

## project structure

distributed-task-queue/
│
├── app/
│   ├── main.py
│   ├── worker.py
│   ├── tasks.py
│   └── config.py
│
├── requirements.txt
├── docker-compose.yml
└── README.md

## how to run locally

### 1. clone the repository

git clone <your-repo-url>
cd distributed-task-queue

### 2. build and start services

docker-compose up --build

this will start:
- redis on port 6379
- fastapi api on port 8000
- rq worker listening for jobs

### 3. submit a task

send a post request:

POST http://localhost:8000/submit
body:
{
  "value": 5
}

you will receive a job_id.

### 4. check task status

GET http://localhost:8000/status/{job_id}

response includes:
- queued / started / finished
- result (if completed)

## scaling workers

to scale workers horizontally:

docker-compose up --scale worker=3

this will start multiple background workers consuming from the same queue.

## use cases

- background file processing
- model inference jobs
- report generation
- data transformation pipelines
- async microservice orchestration

## future improvements

- retry policies with exponential backoff
- dead letter queue support
- monitoring dashboard
- priority queues
- authentication layer

---

this project demonstrates backend system design, async task orchestration, distributed processing patterns, and containerized deployment.
