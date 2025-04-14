import os

# from serpapi import GoogleSearch
import serpapi
from dotenv import load_dotenv

load_dotenv()

def research_topic(topic):
    params = {
        "engine": "google",
        "q": topic,
        "api_key": os.getenv("SERPAI_API_KEY")
    }

    search = serpapi.search(q=topic, engine="google", location="Melbourne, Australia", hl="en", gl="us")

    # search = GoogleSearch(params)
    return search.get("organic_results", [])[:1]