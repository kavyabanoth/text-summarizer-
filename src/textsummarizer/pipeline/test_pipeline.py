from transformers import pipeline

# Load pretrained summarizer
summarizer = pipeline(
    "summarization",
    model="google/pegasus-cnn_dailymail"
)

# Sample input
text = """
Artificial intelligence is transforming industries by enabling machines to learn from data.
It is widely used in healthcare, finance, and automation.
However, challenges such as data privacy and ethical concerns remain important.
"""

# Generate summary
result = summarizer(text, max_length=60, min_length=20, do_sample=False)

print(result[0]['summary_text'])