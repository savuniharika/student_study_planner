from graph import graph

state = {
    "name": "Niharika",
    "subjects": ["Python", "DBMS", "Operating Systems"],
    "hours": 3,
    "exam_days": 5,
    "plan": ""
}

result = graph.invoke(state)

print("\n" + "=" * 50)
print(" AI GENERATED STUDY PLAN")
print("=" * 50)
print(result["plan"])
