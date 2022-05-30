from sqlite3 import connect
from cloudant.client import Cloudant
client = Cloudant.iam("3eb5d4ae-f0a4-47e5-827d-fa621d8d6ce4-bluemix", "BCv3mSoW_qrApbYM8AyL460LVBYXtIXCgDPut6_r5Qii", connect = True)
my_database = client.create_database('my_database')