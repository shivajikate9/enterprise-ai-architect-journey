# current_skills = [
#     "azure",
#     "vmware",
#     "oci",
#     "k8s",
#     "terraform",
#     "python"
# ]

# target_skills = [
#     "python",
#     "LLMs"
#     "RAG",
#     "Agentic AI",
#     "Vector databases",
#     "AI Security",
#     "LLMOps",
#     "AI Architecture"
# ]

import json 

with open("skills.json","r") as file:
    data = json.load(file)

current_skills = data["current_skills"]
target_skills = data["target_skills"]

def skill_gap(current,target):
    missing = []

    for skill in target:
        if skill not in current:
            missing.append(skill)

    return missing


missing_skills = skill_gap(current_skills,target_skills)

print("missing ai skills")

for skill in missing_skills:
    print(f"- {skill}")

def calculate_progress(current,target):
    completed = 0

    for skill in target:
        if skill in current:
            completed += 1


    return (completed / len(target)) * 100

progress = calculate_progress(current_skills,target_skills)

print(f"\nAI Skill progress: {progress:.1f}%")

