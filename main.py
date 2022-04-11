from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from jinja2 import Environment
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
global news
global html_content
driver = webdriver.Chrome(options=chrome_options)

news = []
content = dict(
    background_img_path=
    "https://beebom.com/wp-content/uploads/2022/04/Razer-headphone-save-life-feat.-fin..jpg?resize=250%2C155&quality=75&strip=all",
    description=
    "Razer Kraken Headphones Saved an 18-Year-Old Gamer’s Life from a Bullet",
)
html_content = """
<!DOCTYPE html>
<html>
    <head>
<meta name="imgkit-format" content="png">
<meta name="imgkit-orientation" content="Landscape">
<link rel="stylesheet" href="style.css">
<style type="text/css">

@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap');

<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap" rel="stylesheet">

.container {
  position: relative;
  text-align: center;
}

.image_pos {
    position: absolute;
    top: 136px;
    left: 8%;
    height: 673px;
    width: 84%;
    display: block;
    margin: 0 auto;
}

.news_pos {
    position: absolute;
    text-align:center;
    color: #000;
}

.para {
    position: absolute;
    font-family: 'DM Serif Display', serif;
    bottom: -82px;
    right: 110px;
    left: 98px;
    font-size: 50px;
}

img{
 display: block;
}
</style>
    </head>

<body>
   <div class=container>
       <img class="image" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQe6GOHM6KF6HgCPSz5n1EHUOm6iBoLx1orfdCSqwZDXNpsYFUc4aVPYHnS9HZAJHsRr5UExMe7vCL9u2TVlkBMeJ60icS7ljWge9gjqe4T6QzSjmOSrGA0OT5EUnIXwwUrYD4CeLZf4Np1GcFNDgZBNXzDURdbKwbaCD6Qciya3x38qrkPUuIdS27/s16000/blueprint.jpg" position="relative" style="width:100%" alt="NewsImageLayout">
    <div ><img class=image_pos src="{{background_img_path}}" alt="News Image"></div>
    </div class=news_pos>
        <div class="para">"{{description}}"</div>
   </div> 

</body>

</html>    
"""
rendered_output = Environment().from_string(html_content).render(**content)

with open("out.html", 'w', encoding='utf8') as f:
    f.write(rendered_output)

# def getnews(i):
# 	driver.get('https://beebom.com/category/news/')
# 	t = driver.find_element_by_xpath(f"/html/body/div/div/div/main/div/div[3]/div/div[1]/div/article[{i}]/div/h3/a")
# 	i = driver.find_element_by_xpath(f"/html/body/div/div/div/main/div/div[3]/div/div[1]/div/article[{1}]/figure/a/img")
# 	title=t.get_attribute('title')
# 	image=i.get_attribute('src')
# 	news.append(title)
# 	return title,image

# def createpost():
# 	if getnews(1)[0] in news:
# 		return False
# 	else:
# 		content = dict(
#         img_url = getnews(1)[1],
#         description = getnews(1)[0],
#     )

#     rendered_output = Environment().from_string(HTML).render(**content)

#     with open(html_location, 'w', encoding='utf8') as f:
#         f.write(rendered_output)
# 		driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))
driver.get("https://2.chetangupta5.repl.co/out.html")
time.sleep(5)
capture = driver.find_element_by_tag_name('body')
capture.screenshot("1.jpg")
# driver.get("https://replit.com/@ChetanGupta5/Selenium-GitHub#out.html")
