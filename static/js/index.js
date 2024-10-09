document.addEventListener('DOMContentLoaded', () => {
    const symptomList = document.querySelector('.symptom-list');
    const container = document.querySelector('.symptom-container');
    const placeholder = document.getElementById('symptom-placeholder');
    const symptoms = document.getElementById('symptoms')
    const selectedSymptoms = new Set()

    const updateSymptoms = () => {
        symptoms.setAttribute('value', Array.from(selectedSymptoms).join(','));
    };

    symptomList.addEventListener('click', (e) => {
        if(e.target && e.target.classList.contains('dropdown-item')) {
            const symptom = e.target.getAttribute('value');

            if(container.childElementCount) {
                placeholder.setAttribute('hidden','');
            }

            const symptomBtn = createTag(e.target.textContent, (tag) => {
                tag.remove();
                if(container.childElementCount === 1) {
                    placeholder.removeAttribute('hidden');
                }
                selectedSymptoms.delete(symptom);
                updateSymptoms();
                e.target.removeAttribute('hidden');
            });
            
            container.appendChild(symptomBtn);
            selectedSymptoms.add(symptom);
            updateSymptoms();
            e.target.setAttribute('hidden', '');
        }
    })
});

function createTag(name, handleCloseEvent) {
    const tag = document.createElement('button');
    tag.classList.add('btn', 'btn-primary', 'me-1', 'mb-1');
    tag.style.borderRadius = '10px';
    tag.textContent = name;

    const closeBtn = document.createElement('span');
    closeBtn.innerHTML = '&Cross;';
    closeBtn.style.opacity = '0.8';
    closeBtn.style.marginLeft = '10px';
    closeBtn.style.cursor = 'pointer';

    closeBtn.addEventListener('click', () => handleCloseEvent(tag));
    tag.appendChild(closeBtn);
    return tag;
}