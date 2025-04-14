from topics import load_topics
from researcher import research_topic
from summariser import summarize_articles

if __name__ == "__main__":
    topics = load_topics()

    research_data = {topic: research_topic(topic) for topic in topics}

    summaries = {}

    for topic, articles in research_data.items():
        summaries[topic] = summarize_articles(articles)


    print(summaries)