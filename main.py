import requests
from bs4 import BeautifulSoup

url = "https://giiss1.blogspot.com/2023/02/blog-post_36.html" # استبدل "https://example.com/page" برابط الصفحة التي تريد البحث فيها.
keyword = "الزكاة"  "#السؤال# " 

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("a", href=True) # العثور على جميع الروابط الموجودة على الصفحة.

count = 0
for tag in tags:
    if keyword in tag["href"]:
        count += 1

print("تم العثور على {} حالة للهاشتاغ '{}' على الصفحة '{}'".format(count, keyword, url))