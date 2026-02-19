from solution import DNA_strand

def test_basic_cases():
    assert DNA_strand("AAAA") == "TTTT"
    assert DNA_strand("ATTGC") == "TAACG"
    assert DNA_strand("GTAT") == "CATA"