document.addEventListener("DOMContentLoaded", function() {
    const sympList = [
        'Back pain', 'Constipation', 'Abdominal pain', 'Diarrhoea', 'Mild fever', 'Yellow urine',
        'Yellowing of eyes', 'Acute liver failure', 'Fluid overload', 'Swelling of stomach',
        'Swelled lymph nodes', 'Malaise', 'Blurred and distorted vision', 'Phlegm', 'Throat irritation',
        'Redness of eyes', 'Sinus pressure', 'Runny nose', 'Congestion', 'Chest pain', 'Weakness in limbs',
        'Fast heart rate', 'Pain during bowel movements', 'Pain in anal region', 'Bloody stool',
        'Irritation in anus', 'Neck pain', 'Dizziness', 'Cramps', 'Bruising', 'Obesity', 'Swollen legs',
        'Swollen blood vessels', 'Puffy face and eyes', 'Enlarged thyroid', 'Brittle nails',
        'Swollen extremities', 'Excessive hunger', 'Extra marital contacts', 'Drying and tingling lips',
        'Slurred speech', 'Knee pain', 'Hip joint pain', 'Muscle weakness', 'Stiff neck', 'Swelling joints',
        'Movement stiffness', 'Spinning movements', 'Loss of balance', 'Unsteadiness',
        'Weakness of one body side', 'Loss of smell', 'Bladder discomfort', 'Foul smell of urine',
        'Continuous feel of urine', 'Passage of gases', 'Internal itching', 'Toxic look (typhos)',
        'Depression', 'Irritability', 'Muscle pain', 'Altered sensorium', 'Red spots over body', 'Belly pain',
        'Abnormal menstruation', 'Dischromic patches', 'Watering from eyes', 'Increased appetite', 'Polyuria', 'Family history', 'Mucoid sputum',
        'Rusty sputum', 'Lack of concentration', 'Visual disturbances', 'Receiving blood transfusion',
        'Receiving unsterile injections', 'Coma', 'Stomach bleeding', 'Distention of abdomen',
        'History of alcohol consumption', 'Fluid overload', 'Blood in sputum', 'Prominent veins on calf',
        'Palpitations', 'Painful walking', 'Pus filled pimples', 'Blackheads', 'Scurring', 'Skin peeling',
        'Silver like dusting', 'Small dents in nails', 'Inflammatory nails', 'Blister', 'Red sore around nose',
        'Yellow crust ooze'
    ];    

    // Load existing symptoms from local storage when the page is loaded
    loadSymptoms();
    const listOfSymp = document.getElementById("symp-select");
    // Populate the symptom dropdown
    sympList.forEach(symp => {
        const option = document.createElement("option");
        option.value = symp;
        option.textContent = symp;
        listOfSymp.appendChild(option);
    });

    // Function to remove a tag
    window.removeTag = function(element) {
        const symptomTag = element.parentElement; // Get the parent <span> element of the tag
        symptomTag.style.animation = 'whoops 0.5s forwards'; // Add animation class

        // Remove the tag from the DOM after the animation duration
        setTimeout(() => {
            symptomTag.remove();
            saveSymptoms(); // Save updated symptoms to local storage after removal
        }, 500); // Match this duration with the animation duration
    }

    // Event listener for adding new symptoms
    document.getElementById("symp-select").addEventListener("change", function() {
        const selectedSymptom = this.value; // Get the selected symptom
        if (selectedSymptom !== "Add a symptom...") { // Check if it's a valid selection
            addSymptom(selectedSymptom); // Add the selected symptom
            this.value = "Add a symptom..."; // Reset the select back to the default
            saveSymptoms(); // Save updated symptoms to local storage after addition
        }
    });

    // Function to add a new symptom
    function addSymptom(symptomName) {
        // Check if the symptom already exists in the tags
        const existingTags = document.querySelectorAll("#symp-tags .tag");
        for (let tag of existingTags) {
            if (tag.textContent.slice(0, -1).trim() === symptomName) { // Compare without the button
                return; // Exit the function if the symptom already exists
            }
        }
    
        const newTag = document.createElement("span"); // Create a new <span> element
        newTag.className = 'tag'; // Set the class
        newTag.innerHTML = `${symptomName} <button class='close-btn' onclick='removeTag(this)'>×</button>`; // Set the inner HTML
        document.getElementById("symp-tags").appendChild(newTag); // Append the new tag to the container
    }

    // Function to save symptoms to local storage
    function saveSymptoms() {
        const symptoms = Array.from(document.querySelectorAll("#symp-tags .tag")).map(tag => tag.textContent.slice(0, -1).trim());
        localStorage.setItem("symptoms", JSON.stringify(symptoms));
    }

    // Function to load symptoms from local storage
    function loadSymptoms() {
        const savedSymptoms = JSON.parse(localStorage.getItem("symptoms"));
        if (savedSymptoms) {
            savedSymptoms.forEach(symptom => {
                addSymptom(symptom);
            });
        }
    }
});
