# from src.states.rag_state import RAGState
# import re

# class RAGNodes:
#     def __init__(self, retriever, llm):
#         self.retriever = retriever
#         self.llm = llm

#     def retrieve_docs(self, state: RAGState) -> RAGState:
#         """Retrieve relevant documents for the question."""
#         docs = self.retriever.invoke(state.question)

#         if not isinstance(docs, list):
#             docs = [docs]

#         return RAGState(
#             question=state.question,
#             retrieved_docs=docs
#         )

#     def generate_answer(self, state: RAGState) -> RAGState:
#         """Generate an answer strictly from the retrieved docs."""
#         context = "\n\n".join(
#             getattr(doc, "page_content", str(doc))
#             for doc in (state.retrieved_docs or [])
#         ).strip()

#         if not context:
#             answer_text = "I don't know from the provided documents."
#         else:
#             prompt = f"""Answer the question using ONLY the context below.
# If the answer is not present in the context, say:
# "I don't know from the provided documents."

# Context:
# {context}

# Question: {state.question}

# Answer:"""

#             response = self.llm.invoke(prompt)

#             # Normalize response to plain text
#             if isinstance(response, str):
#                 answer_text = response
#             else:
#                 answer_text = getattr(response, "content", str(response))

#             # ---------- GENERIC VALIDATION STEP ----------
#             context_lower = context.lower()

#             # 1) Extract capitalized name-like phrases from the answer
#             #    e.g., "KL Rahul", "Shubman Gill", "Hardik Pandya"
#             names = re.findall(
#                 r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b",
#                 answer_text
#             )

#             # Ignore some very generic non-name phrases if needed
#             ignore = set()

#             # Keep only names that are not in ignore
#             candidate_names = [
#                 n for n in names
#                 if n not in ignore
#             ]

#             hallucinated = False
#             if candidate_names:
#                 # If there are person-like names, require that at least
#                 # one of them appears in the context.
#                 if not any(name.lower() in context_lower for name in candidate_names):
#                     hallucinated = True
#             else:
#                 # If no names at all, require the full answer to be grounded
#                 # (rough heuristic).
#                 if answer_text.strip().lower() not in context_lower:
#                     hallucinated = True

#             if hallucinated:
#                 answer_text = "I don't know from the provided documents."

#         return RAGState(
#             question=state.question,
#             retrieved_docs=state.retrieved_docs,
#             answer=answer_text
#         )
