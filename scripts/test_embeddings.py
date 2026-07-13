from app.ai.embeddings.embedding_service import EmbeddingService


def main():
    service = EmbeddingService()

    text = """
    Artificial Intelligence enables computers to learn from data.
    Machine Learning is a subset of AI.
    """

    vector = service.create_embedding(text)

    print("\nEmbedding Generated Successfully!")

    print("\nVector Dimension:")
    print(len(vector))

    print("\nFirst 10 Values:")
    print(vector[:10])


if __name__ == "__main__":
    main()