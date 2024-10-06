document.addEventListener("DOMContentLoaded", function() {
})

document.addEventListener('DOMContentLoaded', () => {
    const symptomSelect = document.getElementById('symptoms');
    const dropdownContainer = document.createElement('div');
    const selectedSymptomsContainer = document.createElement('div');
    const dropdownMenu = document.createElement('div');

    dropdownContainer.classList.add('dropdown-container');
    selectedSymptomsContainer.classList.add('selected-symptoms-container');
    dropdownMenu.classList.add('dropdown-menu');

    dropdownContainer.append(selectedSymptomsContainer, dropdownMenu);
    symptomSelect.parentElement.insertBefore(dropdownContainer, symptomSelect);
    symptomSelect.style.display = 'none';

    const createTag = (option) => {
        const tag = document.createElement('span');
        tag.className = 'tag';
        tag.dataset.value = option.value;
        tag.textContent = option.textContent + ' ';
        const removeX = document.createElement('span');
        removeX.className = 'remove-x';
        removeX.textContent = 'x';
        removeX.onclick = () => removeTag(tag, option);
        tag.onclick = () => removeTag(tag, option);
        tag.appendChild(removeX);
        return tag;
    };

    const removeTag = (tag, option) => {
        selectedSymptomsContainer.removeChild(tag);
        option.disabled = false;
    };

    Array.from(symptomSelect.options)
        .filter(option => option.value !== "Add symptoms...")
        .forEach(option => {
            const optionItem = document.createElement('div');
            optionItem.className = 'dropdown-option';
            optionItem.textContent = option.textContent;
            optionItem.onclick = () => {
                if (![...selectedSymptomsContainer.children].some(tag => tag.dataset.value === option.value)) {
                    selectedSymptomsContainer.appendChild(createTag(option));
                    option.disabled = true;
                }
            };
            dropdownMenu.appendChild(optionItem);
        });

    dropdownContainer.onclick = () => dropdownMenu.classList.toggle('show');
    document.addEventListener('click', event => {
        if (!dropdownContainer.contains(event.target)) dropdownMenu.classList.remove('show');
    });
});
