from topics import load_topics
from researcher import research_topic
from summariser import summarize_articles

if __name__ == "__main__":
    topics = load_topics()
    # print(topics)

    research_data = {topic: research_topic(topic) for topic in topics}
    # print(research_data)

    summaries = {}

    for topic, articles in research_data.items():
        # print(f"Topic: {topic}")
        # print(f"Article: {articles}")
        summaries[topic] = summarize_articles(articles)
        # summaries[topic] = articles

    print(summaries)