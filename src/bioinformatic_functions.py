import pandas as pd
import re

def get_locations(text):
    
    if pd.isna(text):
        return []
    
    text = text.replace("SUBCELLULAR LOCATION:", "")
    
    text = re.sub(r"\{ECO:[0-9]+\}", "", text)
    
    text = text.split("Note=", 1)[0]
    
    text = re.sub(r"\{[^{}]*\}", lambda match: match.group().replace(".", "<DOT>"), text)

    locations = []

    for part in text.split("."):

        part = part.split(";", 1)[0]
        part = part.replace("<DOT>", ".").strip()

        if not part:
            continue

        name = re.sub(r"\{[^{}]*\}", "", part).strip()

        if name:
            locations.append(name)

    return locations
    