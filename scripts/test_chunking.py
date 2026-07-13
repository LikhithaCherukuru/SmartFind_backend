from app.ai.chunking.chunker import TextChunker


text = """
Artificial intelligence allows computers to learn from data and make decisions.
Machine learning is a subset of artificial intelligence.
Deep learning uses neural networks to solve complex problems.
Computer vision enables machines to understand images and videos.
Natural language processing allows computers to understand human language.
Generative AI can create text, images, audio, and videos.
Large language models are trained on massive datasets.
Retrieval augmented generation combines search with language models.
Vector databases store numerical representations of text.
Embeddings capture the semantic meaning of information.
"""


chunker = TextChunker(
    chunk_size=20,
    overlap=5
)


chunks = chunker.split_text(text)


for index, chunk in enumerate(chunks):

    print("\nCHUNK", index)

    print(chunk)