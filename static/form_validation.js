document.addEventListener('DOMContentLoaded', function() {
    const createGroupForm = document.getElementById('createGroupForm');
    const groupNameInput = document.getElementById('groupName');
    const groupDescriptionInput = document.getElementById('groupDescription');

    createGroupForm.addEventListener('submit', function(event) {
        if (groupNameInput.value.trim() === '' || groupDescriptionInput.value.trim() === '') {
            event.preventDefault();
            alert('Please fill in all fields.');
        }
    });
});
