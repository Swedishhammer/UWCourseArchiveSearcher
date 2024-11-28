from bs4 import BeautifulSoup
import json
import os

HTML_SOURCE_DIR = "UWCourseArchiveSearcher/TimeSchedules"
OUTPUT_FILE = "CourseData.json"

def parseHTMLFile(filePath):
    print(f"Parsing: {filePath}")
    with open(filePath, 'r', encoding='utf-8') as file:
        dataSoup = BeautifulSoup(file, 'lxml')
    
    titles = [h1.text.strip() for h1 in dataSoup.find_all('h1')]
    paragraphs = [p.text.strip() for p in dataSoup.find_all('p')]

    return {"titles": titles, "paragraphs": paragraphs}
    

def saveToJSON(data):
    with open(OUTPUT_FILE, 'w', econding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data saved to {OUTPUT_FILE}")


filePath = HTML_SOURCE_DIR + "/CSE_24AU.html"
parsedData = parseHTMLFile(filePath)
saveToJSON(parsedData)
