document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    var userName = document.getElementById('users-name'); // User name input field
    var email = document.getElementById('email'); // Email input field
    var userPassword = document.getElementById('password'); // Password input field
    var feedbackElements = document.getElementsByClassName('invalid-feedback'); // Invalid feedback elements
    var showPasswordToggle = document.getElementById('show-password-toggle'); // Show/hide password toggle button
    var registerButton = document.getElementById('register'); // Register button
    var add_cart = document.getElementById('add_cart');

    console.log('DOM elements loaded:', { userName: userName, email: email, userPassword: userPassword, showPasswordToggle: showPasswordToggle, registerButton: registerButton });

    // Call the validation functions for each input field
    if (userName) validateName(userName);
    if (email) validateEmail(email);
    if (userPassword) validatePassword(userPassword);

    // Password toggle functionality
    if (showPasswordToggle && userPassword) {
        showPasswordToggle.addEventListener('click', function() {
            if (userPassword.type === 'password') {
                userPassword.type = 'text';
                showPasswordToggle.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                userPassword.type = 'password';
                showPasswordToggle.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    }

    // Event listener for user name input
    function validateName(userName) {
        userName.addEventListener('keyup', function(e) {
            var userNameValue = e.target.value;

            if (userNameValue.length > 0) {
                fetch('/authentication/validate-name', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ users_name: userNameValue })
                })
                    .then(function(res) { return res.json(); })
                    .then(function(data) {
                        if (data.users_name_valid) {
                            userName.classList.add('is-valid');
                            userName.classList.remove('is-invalid');
                            feedbackElements[0].style.display = 'none'; // Hide invalid feedback
                            registerButton.disabled = false; // Enable register button
                        } else {
                            userName.classList.remove('is-valid');
                            userName.classList.add('is-invalid');
                            feedbackElements[0].style.display = 'block'; // Show invalid feedback
                            feedbackElements[0].innerHTML = '<p>' + data.users_name_error + '</p>'; // Display error message
                            registerButton.disabled = true; // Disable register button
                        }
                    })
                    .catch(function(error) {
                        console.error('Error:', error);
                    });
            } else {
                userName.classList.remove('is-valid');
                userName.classList.remove('is-invalid');
                feedbackElements[0].style.display = 'none'; // Hide invalid feedback
            }
        });
    }

    // Event listener for email input
    function validateEmail(email) {
        email.addEventListener('keyup', function(e) {
            var emailValue = e.target.value;

            if (emailValue.length > 0) {
                fetch('/authentication/validate-email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email: emailValue })
                })
                    .then(function(res) { return res.json(); })
                    .then(function(data) {
                        if (data.email_valid) {
                            email.classList.add('is-valid');
                            email.classList.remove('is-invalid');
                            feedbackElements[1].style.display = 'none'; // Hide invalid feedback
                            registerButton.disabled = false; // Enable register button
                        } else {
                            email.classList.remove('is-valid');
                            email.classList.add('is-invalid');
                            feedbackElements[1].style.display = 'block'; // Show invalid feedback
                            feedbackElements[1].innerHTML = '<p>' + data.email_error + '</p>'; // Display error message
                            registerButton.disabled = true; // Disable register button
                        }
                    })
                    .catch(function(error) {
                        console.error('Error:', error);
                    });
            } else {
                email.classList.remove('is-valid');
                email.classList.remove('is-invalid');
                feedbackElements[1].style.display = 'none'; // Hide invalid feedback
            }
        });
    }

    // Event listener for password input
    function validatePassword(userPassword) {
        userPassword.addEventListener('keyup', function(e) {
            var userPasswordValue = e.target.value;

            if (userPasswordValue.length > 0) {
                showPasswordToggle.style.color = 'black';
                fetch('/authentication/validate-password', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ password: userPasswordValue })
                })
                    .then(function(res) { return res.json(); })
                    .then(function(data) {
                        if (data.password_valid) {
                            userPassword.classList.add('is-valid');
                            userPassword.classList.remove('is-invalid');
                            feedbackElements[2].style.display = 'none'; // Hide invalid feedback
                            registerButton.disabled = false; // Enable register button
                        } else {
                            userPassword.classList.remove('is-valid');
                            userPassword.classList.add('is-invalid');
                            feedbackElements[2].style.display = 'block'; // Show invalid feedback
                            feedbackElements[2].innerHTML = '<p>' + data.password_error + '</p>'; // Display error message
                            registerButton.disabled = true; // Disable register button
                        }
                    })
                    .catch(function(error) {
                        console.error('Error:', error);
                    });
            } else {
                userPassword.classList.remove('is-valid');
                userPassword.classList.remove('is-invalid');
                feedbackElements[2].style.display = 'none'; // Hide invalid feedback
                showPasswordToggle.style.color = 'gray';
                showPasswordToggle.style.cursor = 'default';
                showPasswordToggle.disabled = true;
                userPassword.setAttribute('type', 'password');
            }
        });
    }

    function admin_check() {
        var admin = document.getElementById('admin');
        if (admin) {
            if (admin.checked) {
                admin.value = '1';
            } else {
                admin.value = '0';
            }
        }
    }
});


    