import requests
import pandas as pd
import time

while True:
    current_df = pd.read_csv("database.csv")

    url = "https://api.nobitex.ir/v2/trades/BTCIRT"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()

    df = pd.DataFrame(response_json["trades"])
    df["time"] = pd.to_datetime(df["time"], unit='ms')
    df["time"] = df["time"].dt.tz_localize("UTC").dt.tz_convert("Asia/Tehran")
    df.drop_duplicates(inplace=True)
    df.to_csv("database.csv", mode= "a", header= False, index= False)

    # To create the CSV file:
    # df.to_csv("database.csv", index = False)

    print("DONE")
    time.sleep(60)