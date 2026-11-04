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

def get_class(location):
    main_location = location.split(",", 1)[0].strip()

    return location_classes.get(main_location)

location_classes = {
    "Nucleus": "nucleus",
    "Cytoplasm": "cytoplasm",
    "Cytosol": "cytoplasm",
    "Cell membrane": "cell_membrane",

    "Mitochondrion": "mitochondrion",
    "Mitochondrion matrix": "mitochondrion",
    "Mitochondrion inner membrane": "mitochondrion",
    "Mitochondrion outer membrane": "mitochondrion",
    "Mitochondrion intermembrane space": "mitochondrion",

    "Secreted": "secreted",

    "Endoplasmic reticulum": "endoplasmic_reticulum",
    "Endoplasmic reticulum membrane": "endoplasmic_reticulum",
    "Endoplasmic reticulum lumen": "endoplasmic_reticulum"
}

def get_label(locations):
    if not locations:
        return None

    classes = []
    experimental_classes = []

    for location in locations:
        label = get_class(location)

        if label is None:
            return None

        classes.append(label)

    classes = set(classes)

    if len(classes) != 1:
        return None

    label = next(iter(classes))

    if label not in experimental_classes:
        return None

    return label