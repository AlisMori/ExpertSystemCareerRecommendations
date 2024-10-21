import json
from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import fuzz

app = Flask(__name__)


# Load career data from JSON (could load from career_data.json)
def load_career_data():
    with open('static/career_data.json') as f:
        return json.load(f)


career_data = load_career_data()


def find_careers(skills, industries, work_style):
    career_scores = {}
    data = career_data["careers"]
    for i in data:
        career = i["name"]
        skills_list = i["skills"]
        industries_list = i["industries"]
        work_style_value = i["work_style"]
        skill_score = sum([skills_list.get(skill, 0) for skill in skills])
        work_style_score = 1 if work_style_value in work_style else 0
        industry_score = sum([1 for industry in industries if industry in industries_list])

        total_score = skill_score + work_style_score + industry_score
        career_scores[career] = total_score

    # Return sorted career paths with scores
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    recommendations = [
        {
            'career': career,
            'score': score,
            'description': career_data[career]['description'],
            'suggested_education': career_data[career]['education']
        }
        for career, score in sorted_careers
    ]
    return recommendations


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    skills = data.get('skills', [])
    industries = data.get('industries', [])
    work_style = data.get('work_style', '')

    recommendations = find_careers(skills, industries, work_style)
    return jsonify({'recommendations': recommendations})


if __name__ == '__main__':
    app.run(debug=True)
