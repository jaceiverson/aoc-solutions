"""Helper functions to automate AOC"""
import os
from typing import Optional

import requests as r
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pandas as pd


load_dotenv()

def read(path:str) -> str:
    """General Purpose Read a Text file and Return"""
    with open(path) as f:
        rules = f.read()
    return rules

def aoc_stars() -> str:
    """Scrapes the AOC Page retrives star information to display in README"""

    # Send the URL Request with Cookie to get HTML
    url = "https://adventofcode.com/2021/events"
    response = r.get(
        url,
        cookies={"session": os.environ["COOKIE_SESSION"]},
    )
    soup = BeautifulSoup(response.text,'html.parser')
    # Total Stars
    total_stars = soup.find(string="Total stars: ")
    total = total_stars.find_parent('p').find('span').text.replace('*',"")

    # Find all the events star counts
    all_events = soup.find_all('div',attrs={'class':'eventlist-event'})
    year_stars = {x.find('a').text:(x.find('span').text.replace('*','') if x.find('span') is not None else None) for x in all_events}
    # Create a markdown table of all stars 
    df = pd.DataFrame.from_dict(year_stars.values())
    df["Year"] = year_stars.keys()
    df = df[["Year",0]]
    df.columns = ["Year","Stars"]
    df['Completion %'] = (df['Stars'].fillna(0).astype(int) / 50) * 100
    all_possible = df.shape[0]*50
    df = df.append(pd.DataFrame([["TOTAL",total,(int(total)/all_possible)*100]],columns = df.columns))
    df['Completion %'] = round(df['Completion %'],2)
    # return the Markdown table for use
    return df.to_markdown(index=False,tablefmt="github")

def update_md(new_table:Optional[str] = None) -> None:
    """
    Updates the README.md file with your current status in the AOC
    Accepts a markdown style table from aoc_stars()
    """
    if new_table is None:
        new_table = aoc_stars()
    # GET MD file
    with open("README.md","r") as f:
        md = f.read()
    # remove current table 
    # between Summary and Requests
    new = md.split("##")
    summary_idx = [idx for idx,x in enumerate(new) if "AOC Star Summary" in x][0]
    new[1] = f" AOC Star Summary\n{new_table}\n\n"

    with open("README.md","w") as f:
        f.write("##".join(new))
