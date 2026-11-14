import pandas as pd

AMINO_LST = ["A", "D", "E", "F", "G", "I", "K",	"L", "M", "N", "P",	"Q", "R", "S", "T", "V", "W", "Y", "C", "H"]

def calc_sequence_freq(seq):
    
    length = len(seq)
    
    return pd.Series({f"freq_{am}": seq.count(am) / length for am in AMINO_LST})

def calc_aminoacids_freq(df):
    
    label_seq = df.groupby(by="label")["Sequence"].sum().reset_index()
    
    freq_label_aa = label_seq["Sequence"].apply(calc_sequence_freq)
    
    result = pd.concat([label_seq[["label"]], freq_label_aa], axis=1)
    
    return result

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5,
    "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
    "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6,
    "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}

def gravy(seq):
    vals = [KD[aa] for aa in seq if aa in KD]

    return sum(vals) / len(vals) if vals else float("nan")