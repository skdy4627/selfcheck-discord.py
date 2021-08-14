import hcskr
import schedule
import time
from pymongo import MongoClient

con = MongoClient('mongodb://localhost:27017/')
user = con.user
user_users = user.users
num = con.num
num_nums = num.nums

data = num_nums.find_one({"_id": "numid"})
num_data = data["num"]

def selfcheckf():
    for i in range(0, num_data):
        user_data = list(user_users.find().sort("_id", 1).skip(i).limit(1))
        data = user_data[0]
        hcskr.selfcheck(data['name'], data['birthday'], data['area'], data['schoolname'], data['level'], data['password'], "seewoo")


schedule.every().monday.at("05:00").do(selfcheckf)
schedule.every().tuesday.at("05:00").do(selfcheckf)
schedule.every().wednesday.at("05:00").do(selfcheckf)
schedule.every().thursday.at("05:00").do(selfcheckf)
schedule.every().friday.at("05:00").do(selfcheckf)

while True:
    schedule.run_pending()
    time.sleep(10)