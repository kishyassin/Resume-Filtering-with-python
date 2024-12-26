def filter_by_tags(data, tags):
    tags = [tag.lower() for tag in tags]
    filtered_data = []
    for person in data:
        if isinstance(person, dict):
            skills = person.get("skills", [])
            if isinstance(skills, list):
                flat_skills = []
                for skill in skills:
                    if isinstance(skill, dict):
                        for key in skill:
                            flat_skills.extend(skill[key])
                    elif isinstance(skill, str):
                        flat_skills.append(skill)
                skills = [skill.lower() for skill in flat_skills]
                if any(tag in skills for tag in tags):
                    filtered_data.append(person)
    return filtered_data
