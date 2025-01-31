from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from graph.chains.router import RouteQuery, question_router
from graph.nodes import generate, grade_documents, retrieve
from graph.state import GraphState

load_dotenv()


# constants
GENERATE = "generate"
RETRIEVE = "retrieve"
RETRIEVE_GRADE = "retrieve_grade"


# Adaptive RAG
def route_question(state: GraphState) -> str:

    print("---ROUTING QUESTION---")

    question = state["question"]
    needs: RouteQuery = question_router.invoke({"question": question})

    if needs.needs == "academic":
        return RETRIEVE
    else:
        return GENERATE


workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(RETRIEVE_GRADE, grade_documents)
workflow.add_node(GENERATE, generate)

workflow.set_conditional_entry_point(
    route_question,
    path_map={
        RETRIEVE: RETRIEVE,
        GENERATE: GENERATE,
    },
)

workflow.add_edge(RETRIEVE, RETRIEVE_GRADE)
workflow.add_edge(RETRIEVE_GRADE, GENERATE)
workflow.add_edge(GENERATE, END)


app = workflow.compile()


app.get_graph().draw_mermaid_png(output_file_path="workflow.png")
