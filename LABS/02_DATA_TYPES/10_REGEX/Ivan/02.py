import re
sentence = input()

pattern = r"\b_([A-Za-z0-9]+)\b"


variables_names = re.findall(pattern,sentence)

print(",".join(variables_names))