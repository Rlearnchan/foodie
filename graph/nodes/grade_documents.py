import os
from typing import Any, Dict

from graph.chains.retrival_grader import retrival_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents
    """

    print("---GRADING RETRIEVED DOCUMENTS---")

    question = state["question"]
    documents = state["documents"]
    filtered_docs = []

    for doc in documents:
        score = retrival_grader.invoke(
            {"document": doc.page_content, "question": question}
        )
        grade = score.binary_score

        # Extract only filename (remove path)
        filename = os.path.basename(doc.metadata["source"])
        # Include page information
        page_info = f" (Page {doc.metadata['page']})" if "page" in doc.metadata else ""

        if grade == "yes":
            filtered_docs.append(doc)
            print(f"Document {filename}{page_info} is relevant")
        else:
            print(f"Document {filename}{page_info} is not relevant")

    return {"documents": filtered_docs, "question": question}
