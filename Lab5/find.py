strr = "This_is_a_test_string. It has multiple Sentences, Words, and Letters. It also hasb some CamelCaseWords and some snake_case_words. The string also contains an 'a' followed by 'b' as in 'ab' and an 'a' not followed by 'b' as in 'ac'. There are also sequences of ajkdfb lowercabbse letters joined with abbbbn underscore like 'this_is_a_sequenceb'."


import re

print(re.findall("ab*", strr))
print(re.findall("ab{2,3}", strr))
print(re.findall("[a-z]+_[a-z]+", strr))
print(re.findall("[A-Z][a-z]+", strr))
print(re.findall("a.*?b", strr))

ptr = re.compile("[ ,.]")

def to_col(m):
    return ":"

new = ptr.sub(to_col, strr)

print(new)

ptrr = re.compile("_.")

def camel(m):
    wrd = str(m.group())
    return wrd[1].upper()

cam = ptrr.sub(camel, strr)
print(cam)

print(re.findall("[A-Z][^A-Z]*", strr))

print(re.sub(r"(\w)([A-Z])", r"\1 \2", strr))

verblud = "GovoryatMiBiakiBukiKakJeNositNasZemlia"
print(re.sub(r"(\w)([A-Z])", r"\1_\2", verblud))
    