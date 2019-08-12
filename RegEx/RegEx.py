import re

def Main():
    line = "I think I understand regular expressions"

    matchResult = re.match('think', line, re.M|re.I)
    if matchResult:
        print("Match found: " + matchResult.group())
    else:
        print("Not match found !")
    
    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print("Search found: " + searchResult.group())
    else:
        print("Not search found !")

if __name__ == "__main__":
    Main()