from amino_acid_features import gravy
from collections import Counter

def window_gravy(seq, window=20):
    values = []
    for i in range(0, max(1, len(seq) + window - 1)):
        values.append(gravy(seq[i:i + window]))
        
    return values
        
def max_window_gravy(seq, window=20):
    values = window_gravy(seq, window)
    
    return max(values) if values else 0


def count_hydrophobic_windows(seq, window=20, threshold=1.0):
    values = window_gravy(seq, window)
    
    cnt = 0
    for val in values:
        if val > threshold:
            cnt += 1
        
    return cnt

def max_hydrophobic_run(seq, hydrophobic="AVILMFWYC"):
    cnt_aa = 0
    lst_run = []
    
    for aa in seq:
        if aa in hydrophobic:
            cnt_aa += 1
        else:
            lst_run.append(cnt_aa)
            cnt_aa = 0
            
    lst_run.append(cnt_aa)
    
    return max(lst_run)

def group_fraction(seq, letters):
    if len(seq) == 0:
        return 0
    
    counts = Counter(seq)
    
    return sum(counts[a] for a in letters) / len(seq)

def segment_features(seq, prefix):
    hydrophobic = "AVILMFWYC"
    charged_pos = "KR"
    charged_neg = "DE"
    total = len(seq)
    counts = Counter(seq)

    return {
        f"{prefix}_gravy": gravy(seq),
        f"{prefix}_hydrophobic_frac": group_fraction(seq, hydrophobic),
        f"{prefix}_KR_frac": group_fraction(seq, charged_pos),
        f"{prefix}_DE_frac": group_fraction(seq, charged_neg),
        f"{prefix}_KR_minus_DE": (group_fraction(seq, charged_pos) -
                                   group_fraction(seq, charged_neg)),
        f"{prefix}_C_frac": counts.get("C", 0) / total,
        f"{prefix}_P_frac": counts.get("P", 0) / total,
        f"{prefix}_R_frac": counts.get("R", 0) / total,
        f"{prefix}_K_frac": counts.get("K", 0) / total,
    }