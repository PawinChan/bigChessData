from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
from dotenv import load_dotenv
from io import TextIOWrapper
from time import sleep
import pandas as pd
import seaborn as sb
import os, gc, json

load_dotenv()
sb.set_theme(font="Sarabun", font_scale=0.9)#, palette='tab10')

global db
if 'db' not in globals():
  uri = os.environ.get('mongoConnStr')
  if uri is None:
    uri = "mongodb://localhost:27017"
    print("Mongo Connection String is not set. Falling back to localhost!")
  #try to get explicitly defined connection string, otherwise fallback to localhost.
  
  # Create a new client and connect to the server
  print("Connecting to MongoDB...")
  db = MongoClient(uri, server_api=ServerApi('1'))
  
  # Send a ping to confirm a successful connection
  try:
    db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
    print(e)
else:
  print("Aren't you alreayd connected?")


def tm_formatter(x, pos):
  if x >= 1e6:
    return f"{round(x / 1e6)}M"
  elif x >= 1e3:
    return f"{round(x / 1e3)}K"
  else:
    return f"{round(x)}"