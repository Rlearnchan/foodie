from typing import Annotated

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# schema for llm generation
class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: Annotated[
        str,
        Field(description="Documents are relevant to the question, 'yes' or 'no'"),
    ]


structured_llm_grader = llm.with_structured_output(GradeDocuments)


# prompt design
system = """
You are a grader assessing relevance of a retrieved document to a user question. \n
If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
If the document is purely a reference section or bibliography, grade it as not relevant regardless of content. \n
Give a binary score of 'yes' or 'no' score to indicate whether the document is relevant to the question.

Examples of reference sections to exclude:
- Lists of citations
- Bibliography sections
- Reference lists at the end of papers
- Citation information without substantive content
"""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: {document} \n User question: {question}"),
    ]
)


# LCEL style chain
retrival_grader = grade_prompt | structured_llm_grader
