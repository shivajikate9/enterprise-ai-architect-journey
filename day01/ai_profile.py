profile = {
    "name" : "your name",
    "current_role" : "cloud architect",
    "cloud_skills" : ["azure","OCI"],
    "ai_skills" : [""],
    "target_role" : "enterprise AI aarchitect"
}

print("-------AI Career Path-------")

print(f"current role: {profile['current_role']}")
print(f"target role: {profile['target_role']}")

print("\nCloud Skills")
for skill in profile["cloud_skills"]:
    print(f"- {skill}")

print("\nAI skills:")
if len(profile["ai_skills"]) == 0:
    print("AI transitiona starting today.")
else:
    for skill in profile["ai_skills"]:
        print(f"- {skill}")