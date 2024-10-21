document.addEventListener("DOMContentLoaded", function () {
    let skillsList = [];
    let industriesList = [];

    // Fetch the career data from the JSON file
    fetch('/static/career_data.json')
        .then(response => response.json())
        .then(data => {
            skillsList = data.skills;
            industriesList = data.industries;

            initAutocomplete(document.getElementById('skills-input'), skillsList, 'skills-input-selected');
            initAutocomplete(document.getElementById('industries-input'), industriesList, 'industries-input-selected');
        })
        .catch(error => console.error('Error fetching career data:', error));

    // Function to initialize autocomplete
    function initAutocomplete(input, dataList, cloudContainerId) {
        input.addEventListener('input', function () {
            let inputValue = this.value;
            let suggestionBox = this.nextElementSibling;
            suggestionBox.innerHTML = '';

            if (!inputValue) return false;

            let matchingData = dataList.filter(item => item.toLowerCase().includes(inputValue.toLowerCase()));
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
    }

    // Function to add selected items as clouds
    function addSelectedItem(containerId, item) {
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
        let selectedWorkStyle = document.getElementById('work-style').value;

        let requestData = {
            skills: selectedSkills,
            industries: selectedIndustries,
            work_style: selectedWorkStyle
        };

        fetch('/get_recommendations', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            displayRecommendations(data);
        })
        .catch(error => console.error('Error:', error));
    });

    // Function to display recommendations
    function displayRecommendations(recommendations) {
        let recommendationsContainer = document.getElementById('recommendations');
        recommendationsContainer.innerHTML = '';

        if (recommendations.length === 0) {
            recommendationsContainer.innerHTML = '<p>No career recommendations found.</p>';
            return;
        }

        recommendations.forEach(function (career) {
            let careerDiv = document.createElement('div');
            careerDiv.classList.add('career-recommendation');
            careerDiv.innerHTML = `
                <h3>${career.name}</h3>
                <p><strong>Work Style:</strong> ${career.workStyle}</p>
                <p><strong>Description:</strong> ${career.description}</p>
                <p><strong>Suggested Training:</strong> ${career.training}</p>
            `;
            recommendationsContainer.appendChild(careerDiv);
        });
    }
});
