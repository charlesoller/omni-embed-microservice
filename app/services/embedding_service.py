from typing import List
import logging
from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model, logger=None):
        self.model = SentenceTransformer(model)
        self.logger = logger or logging.getLogger(__name__)

    def create_embedding(self, text: str) -> List[float]:
        """
        Create an embedding for the given text.

        Args:
            text (str): The input text to embed.

        Returns:
            List[float]: The embedding vector.

        Raises:
            ValueError: If the input text is invalid.
            RuntimeError: If there is an error during embedding creation.
        """
        try:
          if not isinstance(text, str) or not text.strip():
              raise ValueError("Input text must be a non-empty string.")

          self.logger.debug(f"Creating embedding for text: {text[:50]}...")

          embedding = self.model.encode([text])

          if embedding is None or len(embedding) == 0:
              raise RuntimeError("Failed to create a valid embedding.")

          return embedding[0].tolist() 

        except ValueError as ve:
            self.logger.error(f"ValueError: {ve}")
            raise

        except Exception as e:
            self.logger.error(f"Error creating embedding: {e}")
            raise RuntimeError(f"An error occurred while creating the embedding: {e}")
