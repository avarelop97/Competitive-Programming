def get_count(sentence: str) -> int:
    vowels = set("aeiou")
    return sum(ch in vowels for ch in sentence)