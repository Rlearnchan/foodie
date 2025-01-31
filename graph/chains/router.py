from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class RouteQuery(BaseModel):
    """Route a user query to the appropriate chain."""

    needs: Literal["academic", "trivial"] = Field(
        ...,
        description="Given a user query, determine whether it is related to academic papers.",
    )


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


structured_llm_router = llm.with_structured_output(RouteQuery)


system = """
You are an expert at query classification.
The vectorstore contains academic papers related to 'Food Desert', 'Human Mobility', and 'Urban Planning'.
Classify questions related to these academic topics as 'academic'.
For all other general or casual questions, classify them as 'trivial'.
"""


route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)


question_router = route_prompt | structured_llm_router
