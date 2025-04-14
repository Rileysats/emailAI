import torch
import requests
import trafilatura

from bs4 import BeautifulSoup
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
from newspaper import Article

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def extract_main_text(url):
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)

# USE THIS
def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def chunk_text_by_tokens(text, max_tokens=1024):
    tokens = tokenizer.encode(text, truncation=False)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        chunks.append(chunk_text)
    return chunks


    
def summarize(text):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=300, min_length=80, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize_articles(articles, model_name="facebook/bart-large-cnn"):
    summaries = []

    for article in articles:
        text = extract_article(article["link"])
        all_chunks = chunk_text_by_tokens(text)
        summaries = [summarize(chunk) for chunk in all_chunks]

        joined_summaries = " ".join(summaries)
        print(joined_summaries)
        final_summary = summarize(joined_summaries)

    return final_summary

        # summarizer = pipeline("summarization", model=model_name, device=0 if torch.cuda.is_available() else -1)

        # summary_parts = [summarize_text(chunk) for chunk in chunk_text(article)]

    #     text = fetch_full_article(article["link"])
        # text = extract_article(article["link"])
        # print(text)
        
        # if "Error" not in text:
        #     try:
        #         summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        #         print(summary)
        #         summary = summary[0]["summary_text"]
        #         summaries.append(summary)
        #     except Exception as e:
        #         summaries.append(f"Summary failed for {article['title']}: {str(e)}")
        # else:
        #     summaries.append(text)  # Error message
    # return " ".join(summaries)

if __name__ == "__main__":
    pass