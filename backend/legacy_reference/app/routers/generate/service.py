from app.database.database import db
from app.stock_comparison import BestStocks
import datetime
from app.config import AppConfig
from bson import ObjectId, json_util
import json

dt = datetime.datetime.now().strftime("%y%m%d")


async def check_in_db(date: str = dt):
    """check if stock prediction has todays date in db."""

    data = db["prediction"].find({"predictions.date": date})
    result = await data.to_list(length=None)
    if not result:
        pd = BestStocks(extended_model_path="models_221211/")
        p = pd.generate()
        print("IN HERE")
        with open("app/Learningapp/best_stocks.json", "w") as f:
            json.dump(parse_json(p), f, indent=4)
        res = await db["prediction"].insert_many([x for x in p])
        res_ids = res.inserted_ids
        data = db["prediction"].find({"_id": {"$in": res_ids}})
        result = await data.to_list(length=None)
    return result


def parse_json(data):
    return json.loads(json_util.dumps(data))
