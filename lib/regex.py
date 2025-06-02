import re

my_regex = re.compile(
    r"(It's such a lovely day today\.|"
    r"Rainy days make me feel gloomy\.|"
    r"The sky is clear and the sun is shining\.|"
    r"Some weather we're having today, huh\?|"
    r"Maybe today's just not my day\.)"
)

def find_all_matching_phrases(text):
    return my_regex.findall(text)
