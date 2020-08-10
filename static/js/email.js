// Sends Form
function sendMail(contactForm) {
    emailjs.send("gmail", "rosie", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "project_request": contactForm.project.value
    })
    .then(
        function(response) {
            console.log('success', response);
            alert('Message Sent! We Aim To Get a Response Back To You Within The Next 24 Hours');
        },
        function(error) {
            console.log('failed', error);
        }
    );
    return false;
};

// Clears Form
const nameClear = document.getElementById('name');
const emailClear = document.getElementById('email');
const textareaClear = document.querySelector('textarea');
const submitButton = document.getElementById('submit-btn');

submitButton.addEventListener('click', resetForm);

function resetForm() {
    // Reset Textarea
    setTimeout(() => {
        nameClear.value = '';
        emailClear.value = '';
        textareaClear.value = '';
    }, 100);
};