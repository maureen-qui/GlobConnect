document.addEventListener('DOMContentLoaded', function() {
    const leaveGroupLinks = document.querySelectorAll('.leave-group');

    leaveGroupLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const groupID = this.dataset.groupId;

            // Simulated API call to leave the group
            // Replace with actual API call or form submission
            console.log(`Leaving group with ID ${groupID}`);

            // Update UI to remove the group from the list
            this.parentNode.remove();
        });
    });
});
