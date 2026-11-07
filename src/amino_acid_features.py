import pandas as pd

AMINO_LST = ["A", "D", "E", "F", "G", "I", "K",	"L", "M", "N", "P",	"Q", "R", "S", "T", "V", "W", "Y", "C", "H"]

def calc_sequence_freq(seq):
    
    length = len(seq)
    
    return pd.Series({f"count {am}": seq.count(am) for am in AMINO_LST, f"freq_{am}": seq.count(am) / length for am in AMINO_LST})

def calc_aminoacids_freq(df):
    
    label_seq = df.groupby(by="label")["Sequence"].sum().reset_index()
    
    freq_label_aa = label_seq["Sequence"].apply(calc_sequence_freq)
    
    result = pd.concat([label_seq[["label"]], freq_label_aa], axis=1)
    
    return result