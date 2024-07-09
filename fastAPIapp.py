from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
import uvicorn


mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client["MQ_db"]
collection = db["statuses"]


app = FastAPI()

class timerange(BaseModel):
    start_time : datetime
    end_time : datetime


@app.post('/status-count/')
async def get_count(time_range:timerange):
    time_range_data = time_range.model_dump()

    start_time = time_range_data.get('start_time')
    end_time = time_range_data.get('end_time')

    pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "count": {"$sum": 1}}},
        ]
    result = collection.aggregate(pipeline)
    status_counts = {item["_id"]: item["count"] for item in result}
    return status_counts


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)