import pandas as pd

AMINO_LST = ["A", "D", "E", "F", "G", "I", "K",	"L", "M", "N", "P",	"Q", "R", "S", "T", "V", "W", "Y", "C", "H"]
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5,
    "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
    "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6,
    "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}

def calc_sequence_freq(seq):
    
    if not isinstance(seq, str) or not seq:
        raise ValueError("Последовательность должна быть непустой строкой.")

    if not set(seq).issubset(AMINO_LST):
        raise ValueError("В последовательности есть неподдерживаемые символы.")
    
    return pd.Series({f"freq_{am}": seq.count(am) / len(seq) for am in AMINO_LST})

def calc_aminoacids_freq(df):
    freqs = df["Sequence"].apply(calc_sequence_freq)

    freqs["label"] = df["label"]

    result = (freqs.groupby("label").mean().reset_index())

    return result

def gravy(seq):
    if not isinstance(seq, str) or not seq:
        raise ValueError("Последовательность должна быть непустой строкой.")

    if not set(seq).issubset(KD):
        raise ValueError("В последовательности есть неподдерживаемые символы.")

    return sum(KD[aa] for aa in seq) / len(seq)