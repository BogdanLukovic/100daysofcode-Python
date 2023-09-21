from bs4 import BeautifulSoup
import requests
#
# response = requests.get(url="https://news.ycombinator.com/")
# contents = response.text
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_headlines = soup.select("span.titleline > a")
#
# all_upvotes = soup.select("span.score")
#
# titles = []
# links = []
# upvotes = []
#
# i = 0
# for _ in all_upvotes:
#
#     title = all_headlines[i].text
#     link = all_headlines[i].get("href")
#     upvote = all_upvotes[i].text
#
#     titles.append(title)
#     links.append(link)
#     upvotes.append(upvote)
#
#     i+=1
# upvotes_int = []
# for upvote in upvotes:
#     upvote = int(upvote.split()[0])
#     upvotes_int.append(upvote)
#     print(upvote)
#
#
# max_upvote = upvotes_int[0]
# max_upvote_position = 0
# position = 0
#
# for upvote in upvotes_int:
#     if upvote > max_upvote:
#         max_upvote_position = position
#         max_upvote = upvote
#     position += 1
#
#
# print(titles[max_upvote_position], links[max_upvote_position], upvotes[max_upvote_position])

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_titles = soup.findAll("h3", class_="listicleItem_listicle-item__title__hW_Kn")

all_movies_reversed = []

for title in all_titles:
    title = title.text

    all_movies_reversed.insert(0, title)

all_movies_list = "\n".join(all_movies_reversed)
with open("list-of-movies.txt", "w") as file:
    file.write(all_movies_list)
