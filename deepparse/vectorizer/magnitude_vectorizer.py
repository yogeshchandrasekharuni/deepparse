from typing import List

from numpy import ndarray

from .vectorizer import Vectorizer


class MagnitudeVectorizer(Vectorizer):
    """
    FastText Magnitude vectorizer to convert an address into fastText embeddings using magnitude mapping.
    """

    def __call__(self, addresses: List[str]) -> List:
        """
        Method to vectorizer addresses.

        Args:
            addresses (list[str]): The addresses to vectorize.

        Return:
            A list of embeddings corresponding to the addresses' elements.
        """
        return [self._vectorize_sequence(address) for address in addresses]

    def _vectorize_sequence(self, address: str) -> ndarray:
        """
        Method to vectorize the address.

        Args:
            address (str): Address to vectorize using fastText.

        Return:
            A list of word vector.
        """
        return self.embeddings_model(address)
