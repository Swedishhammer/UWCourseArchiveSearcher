from bs4 import BeautifulSoup
import json
import os

HTML_SOURCE_DIR = "TimeSchedules"
OUTPUT_FILE = "CourseDataTest.json"

def courseNameTrim(text):
    parenIndex = text.find("(")
    if (parenIndex != -1):
        text = text[0 : parenIndex]
    
    prereqIndex = text.find("Prerequisites")
    if (prereqIndex != -1):
        text = text[0 : prereqIndex]
    return text
def parseHTMLFile(filePath):
    print(f"Parsing: {filePath}")
    with open(filePath, 'r', encoding='utf-8') as file:
        dataSoup = BeautifulSoup(file, 'lxml')
    #This deptCode fails for a couple cases ie. Mechanical Engineering where url uses logical meche
    #    but the course code listed in the Time Schedule tables is "M E"
    fileName = filePath[(filePath.rindex('/') + 1) : len(filePath)]
    deptCode = fileName[0 : fileName.index("_")]
    print(f"deptCode is {deptCode}")
    titles = [h1.text.strip() for h1 in dataSoup.find_all('h1')]
    tables = []
    for table in dataSoup.find_all('table'):
        text = table.text.strip()
        if text.startswith(deptCode):
            text = courseNameTrim(text)
            tables.append(text)

    return {"titles": titles, "tables": tables}
    

def saveToJSON(data):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data saved to {OUTPUT_FILE}")

def parseAllHTMLFiles():
    parsedData = []

    for fileName in os.listdir(HTML_SOURCE_DIR):
        if fileName.endswith('.html'):
            filePath = HTML_SOURCE_DIR + "/" + fileName
            parsedData.append(parseHTMLFile(filePath))
    return parsedData
#filePath = HTML_SOURCE_DIR + "/CSE_24AU.html"
#filePath = HTML_SOURCE_DIR + "/Latin Sucess"
parsedData = parseAllHTMLFiles()
print(f"data: {parsedData}")
saveToJSON(parsedData)
