import requests
from bs4 import BeautifulSoup


class HackerNews:
    """
    Create an instance of `HackerNews` class.
    ```py
    articles = HackerNews()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.articles_list()` | Returns the latest articles along with their score, author, author url, time, comment count and link in JSON format. |
    """

    def articles_list(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.articles_list()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None