# Career Path Expert System

This expert system helps users discover suitable career paths based on their selected skills, industries of interest,
work style preferences, and educational background. The application is built using Python (Flask), JavaScript, HTML,
CSS, and JSON for data storage.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Introduction

The Career Path Expert System aims to guide individuals in exploring career options aligned with their competencies,
interests, and preferences. Users input their skills, preferred industries, and work style, and the system provides a
tailored list of recommended careers along with relevant details and suggested educational paths.

## Features

- **Career Recommendations**: Generates a list of career suggestions based on user-selected skills, industries, and work
  style.
- **Customizable Career Database**: Easily updateable JSON database storing information about different career paths,
  including skills, industries, and work environments.
- **Evaluation Support**: Ability to test the system with synthetic profiles to assess recommendation accuracy and
  relevance.
- **Responsive Interface**: User-friendly web interface for interaction with the expert system.

## Technology Stack

- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON (for career data)
- **Algorithms**: Heuristic scoring based on matching user inputs to career attributes

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask (`pip install Flask`)

### Installation

1. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Flask app**:

    ```bash
    python app.py
    ```

3. **Access the application**:

   Open a web browser and go to `http://127.0.0.1:5000` to use the system.

---

### Usage

1. **Select Skills**: Choose relevant skills from a provided list.
2. **Choose Industries**: Select one or more industries of interest.
3. **Select Work Style**: Specify preferred work style (e.g., remote, on-site, or hybrid).
4. **Submit**: Click the submit button to receive personalized career recommendations.

---

### Evaluation

The system includes an evaluation setup using a series of synthetic profiles to test its accuracy and robustness. To run
an evaluation, add the synthetic profiles to the code, and test directly using the `find_careers` function to bypass the
web interface for faster processing.

The evaluation results can be analyzed with graphs and tables to measure how well the system aligns recommendations with
user inputs.

---

### Future Improvements

- **Advanced Machine Learning Integration**: Incorporate ML techniques to improve recommendation scoring.
- **User Feedback Loop**: Allow users to provide feedback on recommendations for continuous improvement.
- **Expanded Career Database**: Add more career paths and skills to increase the system’s versatility.
- **Dynamic Skills and Industry Lists**: Allow users to input custom skills and industries.

---

### License

This project is licensed under the MIT License. 