def DNA_strand(dna: str) -> str:
    # Fast C-level translation
    return dna.translate(str.maketrans("ATCG", "TAGC"))