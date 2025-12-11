
from src.states.rag_state import RAGState


class RAGNodes:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def retrieve_docs(self, state: RAGState) -> RAGState:
        """Retrieve relevant documents for the question."""
        docs = self.retriever.invoke(state.question)

        # Ensure docs is always a list
        if not isinstance(docs, list):
            docs = [docs]

        return RAGState(
            question=state.question,
            retrieved_docs=docs
        )

    def generate_answer(self, state: RAGState) -> RAGState:
        """Generate an answer strictly from the retrieved documents."""
        # Build context from retrieved docs
        context = "\n\n".join(
            getattr(doc, "page_content", str(doc))
            for doc in (state.retrieved_docs or [])
        ).strip()

        if not context:
            answer_text = "I don't know from the provided documents."
        else:
            prompt = f"""Answer the question using ONLY the context below.
If the answer is not present in the context, say:
"I don't know from the provided documents."

Context:
{context}

Question: {state.question}

Answer:"""

            response = self.llm.invoke(prompt)

            # normalize response to plain text
            if isinstance(response, str):
                answer_text = response
            else:
                answer_text = getattr(response, "content", str(response))

        return RAGState(
            question=state.question,
            retrieved_docs=state.retrieved_docs,
            answer=answer_text
        )
