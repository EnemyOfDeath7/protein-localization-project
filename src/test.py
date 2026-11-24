def max_hydrophobic_run(seq, hydrophobic="AVILMFWYC"):
    max_run = 0
    current = 0
    for aa in seq:
        if aa in hydrophobic:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 0
    return max_run

print(max_hydrophobic_run("AAAKKKAAAVVV", hydrophobic="AVILMFWYC"))