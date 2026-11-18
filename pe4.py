import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor

topics = wikipedia.search("generative artificial intelligence")
print(topics)

start = time.perf_counter()

for topic in topics:
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    with open(title + ".txt", "w", encoding="utf-8") as file:
        for reference in references:
            file.write(reference + "\n")
    print(title)

end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds")

def wiki_dl_and_save(topic):
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    with open(title + ".txt", "w", encoding="utf-8") as file:
        for reference in references:
            file.write(reference + "\n")

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)

end = time.perf_counter()
print(f"Section B time taken: {end - start:.2f} seconds")