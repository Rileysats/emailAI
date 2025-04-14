from pathlib import Path

def load_topics():
    topics = []
    current_folder = Path(__file__).parent
    topics_file = current_folder / "topics.txt"
    
    with Path(topics_file).open("r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("- "):
                topics.append(line[2:])
    return topics

if __name__ == "__main__":
    topics = load_topics("src/topics.txt")
    print(topics)