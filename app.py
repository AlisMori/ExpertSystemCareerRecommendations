import json
from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import fuzz

app = Flask(__name__)


# Load career data from JSON (could load from career_data.json)
def load_career_data():
    with open('static/career_data.json') as f:
        return json.load(f)


career_data = load_career_data()


def find_careers(selected_skills, selected_industries, selected_work_style):
    career_scores = {}
    data = career_data["careers"]
    index = 0
    for career in data:
        skills_list = career["skills"]
        industries_list = career["industries"]
        work_styles = career["work_style"]
        skill_score = sum([skills_list.get(skill, 0) for skill in selected_skills])
        work_style_score = sum([1 for style in selected_work_style if style in work_styles])
        industry_score = sum([1 for industry in selected_industries if industry in industries_list])

        total_score = skill_score + work_style_score + industry_score
        career_scores[index] = total_score
        index += 1

    # Return sorted career paths with scores
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    recommendations = [
        {
            'career': data[indexx]["name"],
            'score': score,
            'description': data[indexx]['description'],
            'suggested_education': data[indexx]['education']
        }
        for indexx, score in sorted_careers
    ]
    return recommendations


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    print(f"Received data: {data}")
    skills = data.get('skills', [])
    industries = data.get('industries', [])
    work_style = data.get('work_style', '')

    recommendations = find_careers(skills, industries, work_style)

    return jsonify({'recommendations': recommendations})



if __name__ == '__main__':
    app.run(debug=True)
