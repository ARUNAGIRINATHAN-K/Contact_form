document.getElementById('contactForm').addEventListener('submit', function(event) {
    let valid = true;

    // Check if all fields are filled
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !message) {
        valid = false;
        alert('All fields are required.');
    }

    // Check email format
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (email && !emailPattern.test(email)) {
        valid = false;
        alert('Please enter a valid email address.');
    }

    // Check message length
    if (message.length > 500) {
        valid = false;
        alert('Message should be less than 500 characters.');
    }

    // If not valid, prevent form submission
    if (!valid) {
        event.preventDefault();
    }
});
