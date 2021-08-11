import re

pattern = r"(?P<url>(?P<subdomain>www)\.(?P<domain_name>[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*)(?P<domain_extension>(?P<domain_block>\.[a-z]+)+))"

valid_urls = []
text = input()
while text:
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_urls.append(match.group("url"))
    text = input()

for url in valid_urls:
    print(url)
