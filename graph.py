from langgraph.graph import StateGraph, START, END

from state import StudyState
from nodes import analyze_input, generate_plan

# Create Graph
builder = StateGraph(StudyState)

# Add Nodes
builder.add_node("analyze", analyze_input)
builder.add_node("generate_plan", generate_plan)

# Connect Nodes
builder.add_edge(START, "analyze")
builder.add_edge("analyze", "generate_plan")
builder.add_edge("generate_plan", END)

# Compile Graph
graph = builder.compile()
