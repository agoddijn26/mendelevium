from difflib import SequenceMatcher


def num_same_words(s1, s2):
    list1 = list(filter(None, s1.upper().split(" ")))
    list2 = list(filter(None, s2.upper().split(" ")))
    set1 = set(list1)
    set2 = set(list2)
    intersect = set1.intersection(set2)
    return len(intersect)


def longest_substring(s1, s2):
    seqmatch = SequenceMatcher(None, s1.lower(), s2.lower())
    match = seqmatch.find_longest_match(0, len(s1), 0, len(s2))
    return match.size
