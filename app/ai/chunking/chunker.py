class TextChunker:


    def __init__(
        self,
        chunk_size=100,
        overlap=20
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def split_text(self, text):

        words = text.split()

        chunks = []

        start = 0


        while start < len(words):

            end = start + self.chunk_size


            chunk_words = words[start:end]


            chunk = " ".join(chunk_words)


            chunks.append(chunk)


            start = end - self.overlap


        return chunks