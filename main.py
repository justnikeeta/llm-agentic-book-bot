from scraper import scrape_chapter
from llm_agents import ai_writer, ai_reviewer

# URL to fetch from
url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

# 1. Scrape content + take screenshot
chapter, screenshot_path = scrape_chapter(url)

# 2. AI Writes the content
spun = ai_writer(chapter)

# 3. AI Reviews it
reviewed = ai_reviewer(spun)

# 4. Save to final output file
with open("final_chapter.txt", "w") as f:
    f.write(reviewed)

print("✅ Final version saved to final_chapter.txt")
