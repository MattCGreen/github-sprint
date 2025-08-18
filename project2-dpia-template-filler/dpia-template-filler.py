from datetime import date

DPIA_TEMPLATE = """
# Data Protection Impact Assessment (DPIA)

**Project Name**: {project_name}  
**Date**: {date}  

## 1. Purpose
{purpose}

## 2. Data Types
{data_types}

## 3. Risks Identified
{risks}

## 4. Mitigation Measures
{mitigation}
"""

def create_dpia(project_name, purpose, data_types, risks, mitigation):
    today = date.today().strftime("%Y-%m-%d")
    return DPIA_TEMPLATE.format(
        project_name=project_name,
        date=today,
        purpose=purpose,
        data_types=data_types,
        risks=risks,
        mitigation=mitigation
    )

if __name__ == "__main__":
    dpia_doc = create_dpia(
        project_name="GDPR Chatbot",
        purpose="Provide GDPR guidance to users via AI",
        data_types="User queries, email addresses",
        risks="Data leakage, inaccurate guidance",
        mitigation="Encryption, human review of AI responses"
    )

    with open("dpia.md", "w", encoding="utf-8") as f:
        f.write(dpia_doc)
    print("DPIA document created: dpia.md")
