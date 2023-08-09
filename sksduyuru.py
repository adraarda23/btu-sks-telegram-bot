import requests
from bs4 import BeautifulSoup

class DUYURU:
    class Announcement:
        def __init__(self, link, title, publish_date):
            self.link = link
            self.title = title
            self.publish_date = publish_date

    def __init__(self, url="https://sks.btu.edu.tr/tr/duyuru/birim/108"):
        self.url = url

    def get_first_announcement_link(self):
        response = requests.get(self.url)
        page = BeautifulSoup(response.content, "html.parser")

        content = page.find("div", class_="ann-list")
        announcements = content.find_all("li")
        
        first_announcement_link = announcements[0].find("a")["href"]
        
        with open("first_announcement_link.txt", "w"  , encoding = "utf-8") as f:
            f.write(first_announcement_link)
        


    def check_for_new_content(self):
        new_content = []

        response = requests.get(self.url)
        page = BeautifulSoup(response.content, "html.parser")
        content = page.find("div", class_="ann-list")
        announcements = content.find_all("li")
        
        for ann in announcements:
            link = ann.find("a")["href"]
            title = ann.find("strong").text
            publish_date = ann.find("span").text

            first_announcement_link = open("first_announcement_link.txt", "r", encoding = "utf-8")
            if link == first_announcement_link.read():
                 break

            new_content.append(self.Announcement(link, title, publish_date))
        
        return new_content

    """def print_new_content(self, new_content):
        for ann in new_content:
            print("DUYURU", end="\n\n")
            print(ann.title.upper())
            print(ann.publish_date, end="\n\n")
            print("Daha fazla bilgi için: " + ann.link)
            print("\n----------------\n")"""

""""
if __name__ == "__main__":
    duyuru_instance = DUYURU()
    first_announcement_link = duyuru_instance.get_first_announcement_link()
    new_content = duyuru_instance.check_for_new_content(first_announcement_link)
    duyuru_instance.print_new_content(new_content)"""