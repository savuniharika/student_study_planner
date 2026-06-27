from state import StudyState


def analyze_input(state: StudyState):

    print("\nAnalyzing student details...")

    print(f"Name: {state['name']}")
    print(f"Subjects: {', '.join(state['subjects'])}")
    print(f"Study Hours: {state['hours']}")
    print(f"Exam in: {state['exam_days']} days")

    return state

from llm import llm


def generate_plan(state: StudyState):

    prompt = f"""
    You are an expert study planner.

    Student Name: {state['name']}

    Subjects:
    {", ".join(state['subjects'])}

    Study Hours Per Day:
    {state['hours']}

    Exam in:
    {state['exam_days']} days

    Create a personalized study plan.
    """

    response = llm.invoke(prompt)

    state["plan"] = response.content

    return state
