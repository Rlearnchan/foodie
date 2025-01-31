from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of the graph.
    Attributes:
        question: The question that the user asked
        generation: LLM generation
        documents: List of documents
    """

    question: str
    generation: str
    documents: List[str]
