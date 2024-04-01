from googlesearch import search
a="download "
query = "The Two Towers (The Lord of the Rings, Part 2)"
b=query+a
for j in search(b, tld="co.in", num=1, stop=1, pause=1):
    print(j)