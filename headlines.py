# headlines.py
# docker run --rm -v /home/realpython/code:/app rp python /app/headlines.py
# docker run --rm -v /home/brent/srcnode/App13320:/app rp python /app/headlines.py
import parse
from reader import feed

print('Hello world')
# tutorial = feed.get_article(0)
# headlines = [
#     r.named["header"]
#     for r in parse.findall("\n## {header}\n", tutorial)
# ]
# print("\n".join(headlines))
