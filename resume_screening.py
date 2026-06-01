import re

print("=" * 50)
print("      AI RESUME SCREENING SYSTEM")
print("=" * 50)

required_skills = input(
    "\nEnter required skills (comma separated): "
).lower().split(",")

print("\nPaste Resume Content Below")
print("(Type END on a new line when finished)\n")

resume_lines = []

while True:
    line = input()

    if line.upper() == "END":
        break

    resume_lines.append(line)

resume_text = " ".join(resume_lines).lower()

matched_skills = []

for skill in required_skills:

    skill = skill.strip()

    if skill in resume_text:
        matched_skills.append(skill)

total_required = len(required_skills)

matched_count = len(matched_skills)

score = (matched_count / total_required) * 100

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)

print(f"\nTotal Required Skills : {total_required}")
print(f"Matched Skills        : {matched_count}")

print("\nMatched Skill List:")

for skill in matched_skills:
    print("✓", skill.title())

print(f"\nMatch Score : {score:.2f}%")

if score >= 80:
    print("\nStatus : Highly Recommended")
elif score >= 60:
    print("\nStatus : Recommended")
else:
    print("\nStatus : Not Recommended")

print("\n" + "=" * 50)