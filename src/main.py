from helpers import load_topics
from summariser import Summariser
from researcher import Researcher
from dotenv import load_dotenv
from logger import ProjectLogger

logger = ProjectLogger(__name__).get_logger()

load_dotenv()

if __name__ == "__main__":

    topics = load_topics()

    researcher = Researcher()
    research_data = {topic: researcher.research_topic(topic) for topic in topics}

    summaries = {}
    summariser = Summariser()

    for topic, articles in research_data.items():
        summaries[topic] = summariser.summarize_articles(articles)

    print(summaries)