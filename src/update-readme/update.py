"""Used to automatically update README to reflect stars earned"""

from typing import Optional
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd

from helper.aoc_requests import get_aoc_page


def get_aoc_stars() -> str:
    """Scrapes the AOC Page retrives star information to display in README"""

    # Send the URL Request with Cookie to get HTML
    response = get_aoc_page(f"https://adventofcode.com/{date.today().year-1}/events")
    soup = BeautifulSoup(response.text, "html.parser")
    # Total Stars
    total_stars = soup.find(string="Total stars: ")
    total = total_stars.find_parent("p").find("span").text.replace("*", "")

    # Find all the events star counts
    all_events = soup.find_all("div", attrs={"class": "eventlist-event"})
    year_stars = {
        x.find("a").text: (
            x.find("span").text.replace("*", "") if x.find("span") is not None else None
        )
        for x in all_events
    }
    # Create a markdown table of all stars
    df = pd.DataFrame.from_dict(year_stars.values())
    df["Year"] = year_stars.keys()
    df = df[["Year", 0]]
    df.columns = ["Year", "Stars"]
    df["Completion %"] = (df["Stars"].fillna(0).astype(int) / 50) * 100
    all_possible = df.shape[0] * 50
    df = df.append(
        pd.DataFrame(
            [["TOTAL", total, (int(total) / all_possible) * 100]], columns=df.columns
        )
    )
    df["Completion %"] = round(df["Completion %"], 2)
    # return the Markdown table for use
    return df.to_markdown(index=False, tablefmt="github")


def update_readme(new_table: Optional[str] = None) -> None:
    """
    Updates the README.md file with your current status in the AOC
    Accepts a markdown style table from aoc_stars()
    """
    # if no table passed in, will create one from aoc_stars()
    if new_table is None:
        new_table = get_aoc_stars()
    # GET current README file
    with open("README.md", "r") as f:
        md = f.read()
    # remove current table (Only Element under AOC Star Summary)
    new = md.split("#")
    summary_idx = [idx for idx, x in enumerate(new) if "AOC Star Summary" in x][0]
    # add the updated table in, replacing the old
    new[summary_idx] = f" AOC Star Summary\n{new_table}\n\n"

    # write back the new README with updated table
    with open("README.md", "w") as f:
        f.write("#".join(new))

    print("README.md Updated")


if __name__ == "__main__":
    update_readme()
