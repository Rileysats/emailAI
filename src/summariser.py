from transformers import pipeline
import torch

def summarize_articles(articles, model_name="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model_name, device=0 if torch.cuda.is_available() else -1)
    summaries = []
    for article in articles:
        # Fetch article content (simplified; use full text in practice)
        text = f"{article['title']} {article.get('snippet', '')}"
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
        summaries.append(summary)
    return " ".join(summaries)