*** MQ Status Monitoring System
This project consists of a set of Python scripts that implement a basic message queue system using RabbitMQ and MongoDB. The system includes a producer that sends status messages, a consumer that processes these messages and stores them in a MongoDB collection with a timestamp, and a FastAPI application that allows querying the stored status data.

*** Files
* consumer.py: Consumes messages from a RabbitMQ queue and stores them in MongoDB with a timestamp.
* producer.py: Generates and publishes status messages to the RabbitMQ queue.
* fastAPIapp.py: A FastAPI application that provides an API to query the stored status data based on a time range.

*** Requirements
To run this project, you need to have the following software installed:

** Python 3.9+
** RabbitMQ
** MongoDB

You can install the required Python packages using the requirements.txt file provided.

*** Setup
1. Install dependencies:
pip install -r requirements.txt

2. Start RabbitMQ Server:
Make sure the RabbitMQ server is running on localhost.

3. Start MongoDB Server:
Make sure the MongoDB server is running on localhost.

*** Running the Scripts
1. Start the Producer:
python producer.py

2. Start the Consumer:
python consumer.py

3. Start the FastAPI Application:
uvicorn fastAPIapp:app --reload

The FastAPI application will be available at http://localhost:8000.

Author
Ravi G%upta

*** Running the Scripts



