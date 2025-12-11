from langgraph.graph import StateGraph, END
from src.states.rag_state import RAGState
from src.nodes.reactnode import RAGNodes

class GraphBuilder:

    def __init__(self, retriever, llm):
        
        try:
            self.nodes = RAGNodes(retriever, llm)
        except TypeError:
            try:
                self.nodes = RAGNodes(retriever)
            except TypeError:
                self.nodes = RAGNodes()

        self.retriever = retriever
        self.llm = llm
        self.graph = None

    def build(self):
        builder = StateGraph(RAGState)

        # add_node expects a callable that accepts a single `state` arg (bound method)
        builder.add_node("retriever", self.nodes.retrieve_docs)
        builder.add_node("responder", self.nodes.generate_answer)

        # correct entry point and edge names
        builder.set_entry_point("retriever")

        builder.add_edge("retriever", "responder")
        builder.add_edge("responder", END)

        self.graph = builder.compile()
        return self.graph

    def run(self, question: str) -> dict:
        if self.graph is None:
            self.build()

        initial_state = RAGState(question=question)
        return self.graph.invoke(initial_state)
