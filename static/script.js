document.addEventListener("DOMContentLoaded", function () {
    let skillsList = [];
    let industriesList = [];
    let workStyleList = [];

    // Fetch the career data from the JSON file
    fetch('/static/career_data.json')
        .then(response => response.json())
        .then(data => {
            skillsList = data.skills;
            industriesList = data.industries;
            workStyleList = data.work_styles;

            initAutocomplete(document.getElementById('skills-input'), skillsList, 'skills-input-selected');
            initAutocomplete(document.getElementById('industries-input'), industriesList, 'industries-input-selected');
            initAutocomplete(document.getElementById('work-styles-input'), workStyleList, 'work-styles-input-selected');
        })
        .catch(error => console.error('Error fetching career data:', error));

    // Track selected items
    let selectedItems = new Set();

    // Function to initialize autocomplete
    function initAutocomplete(input, dataList, cloudContainerId) {
        input.addEventListener('input', function () {
            let inputValue = this.value;
            let suggestionBox = this.nextElementSibling;
            suggestionBox.innerHTML = '';

            if (!inputValue) return false;

            let matchingData = dataList.filter(item => item.toLowerCase().includes(inputValue.toLowerCase()) && !selectedItems.has(item));
            matchingData.forEach(function (item) {
                let suggestionItem = document.createElement('div');
                suggestionItem.classList.add('suggestion-item');
                suggestionItem.textContent = item;

                suggestionItem.addEventListener('click', function () {
                    input.value = '';
                    suggestionBox.innerHTML = '';
                    addSelectedItem(cloudContainerId, item);
                });

                suggestionBox.appendChild(suggestionItem);
            });
        });
        // Prevent 'Enter' key from triggering any unintended action
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault(); // Prevent form submission or any default action
            }
        });

    }

    // Function to add selected items as clouds
    function addSelectedItem(containerId, item) {

        // Check if item is already selected
        if (selectedItems.has(item)) return;
        // Add item to selectedItems set
        selectedItems.add(item);

        let selectedContainer = document.getElementById(containerId);
        let cloud = document.createElement('span');
        cloud.classList.add('cloud');
        cloud.innerHTML = item + ' <span class="remove-cloud">&times;</span>';

        cloud.querySelector('.remove-cloud').addEventListener('click', function () {
            selectedContainer.removeChild(cloud);
        });

        selectedContainer.appendChild(cloud);
    }

    // Handle form submission
    document.getElementById('career-form').addEventListener('submit', function (event) {
        event.preventDefault();

        let selectedSkills = Array.from(document.querySelectorAll('#skills-input-selected .cloud')).map(cloud => cloud.textContent.replace('×', '').trim());
        let selectedIndustries = Array.from(document.querySelectorAll('#industries-input-selected .cloud')).map(cloud => cloud.textContent.replace('×', '').trim());
        let selectedWorkStyle = Array.from(document.querySelectorAll('#work-styles-input-selected .cloud')).map(cloud => cloud.textContent.replace('×', '').trim());

        let requestData = {
            skills: selectedSkills,
            industries: selectedIndustries,
            work_style: selectedWorkStyle
        };

        // console.log("Request Data:", requestData);
        fetch('/get_recommendations', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(requestData)
        })
            .then(response => response.json())
            .then(data => {
                // console.log("Response Data:", data);
                displayRecommendations(data.recommendations);
            })
            .catch(error => console.error('Error:', error));
    });

    // Function to display recommendations
    function displayRecommendations(recommendations) {
        const recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = '';  // Clear previous results

        if (Array.isArray(recommendations) && recommendations.length > 0) {
            recommendations.forEach(recommendation => {
                // Create a new div for each recommendation
                const recommendationDiv = document.createElement('div');
                recommendationDiv.classList.add('recommendation');

                // Create elements for career, score, description, and suggested education
                const careerName = document.createElement('h3');
                careerName.textContent = recommendation.career;

                const score = document.createElement('p');
                score.textContent = `Match score: ${recommendation.score.toFixed(1)}`;

                const description = document.createElement('p');
                description.textContent = `Description: ${recommendation.description}`;

                const education = document.createElement('p');
                education.textContent = 'You should consider education in following areas:'

                const educationList = document.createElement('ul');
                recommendation.suggested_education.forEach(education => {
                    const listItem = document.createElement('li');
                    listItem.textContent = education;
                    educationList.appendChild(listItem);
                });

                // Append the elements to the recommendationDiv
                recommendationDiv.appendChild(careerName);
                recommendationDiv.appendChild(score);
                recommendationDiv.appendChild(description);
                recommendationDiv.appendChild(education);
                recommendationDiv.appendChild(educationList);

                // Append the recommendationDiv to the recommendationsDiv
                recommendationsDiv.appendChild(recommendationDiv);
            });
        } else {
            recommendationsDiv.textContent = 'No recommendations available.';
        }
    }
});
