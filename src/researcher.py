import os
import serpapi
from logger import ProjectLogger

logger = ProjectLogger(__name__).get_logger()

class Researcher():
    def __init__(self):
        pass

    def research_topic(self, topic):
        params = {
            "engine": "google",
            "q": topic,
            "api_key": os.getenv("SERPAI_API_KEY"),
            "tbs": "qdr:w"
        }
        logger.info(f"Researching topic: {topic}")

        search = serpapi.search(q=topic, engine="google", api_key=os.getenv("SERPAI_API_KEY"), hl="en", gl="au", tbs="qdr:w")

        # search = GoogleSearch(params)
        return search.get("organic_results", [])[:1]