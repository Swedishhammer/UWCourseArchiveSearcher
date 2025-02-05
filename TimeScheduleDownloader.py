import os
import requests
import time

"""
Downloads the website at the given url and stores/saves it within the 
    OUTPUT_DIR folder as fileName
"""
def downloadWebPage(url, fileName, OUTPUT_DIR):
    try:
        print(f"Downloading {url}")
        response = requests.get(url)
        response.raise_for_status()
        
        filePath = OUTPUT_DIR + "/" + fileName
        with open(filePath, 'w', encoding = 'utf-8') as file:
            file.write(response.text)

        print(f"Saved: {filePath}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
"""
Parameters:
    quarters: string list of quarters being searched
    years: int list of all years that should be downloaded
    depts: string list representing department codes
        Will be removed, building up to larger scope
**This method does NOT check if quarters or years are valid, that's up to you to get right**
"""
def downloadWebPages(quarters, years, depts, OUTPUT_DIR):
    urlbase = "https://washington.edu/students/timeschd/"
    for year in years:
        for quarter in quarters:
            for dept in depts:
                url = urlbase + quarter + str(year) + "/" + dept.lower() + ".html"
                fileName = dept.upper() + "_" + quarter + str(year) + ".html"
                if (os.path.exists("TimeSchedules/" + fileName)):
                    print("File already downloaded")
                else:
                    downloadWebPage(url, fileName, OUTPUT_DIR)
                    #Will slow down program but have to be careful to not violate download rate rules
                    time.sleep(1)

testQuarters = ["AUT", "WIN", "SPR"]
#years = ["2023","2020","2015"]
years = []
startYear = 2020
#+1 is due to range() having an exclusive end
endYear = 2025 + 1
for i in range(startYear, endYear):
    years.append(i)
depts = ["ENGL"]
OUTPUT_DIR = "TimeSchedules"

downloadWebPages(testQuarters, years, depts, OUTPUT_DIR)