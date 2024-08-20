## User Experience (UX)
### Project Goals
### Development Strategy
### Epics
### User Stories and Agile Methodology
### Agile Workflow

## Features
### Existing Features
#### Base Template and Layout
#### Authentication System and Security
#### Expense Management
#### Error Handling
#### User Preferences
### Future Features

## Design
### Wireframes
### Site map
### Database Schema

## The Surface Plane
### Design
#### Colour Scheme
#### Typography
#### Layout and Elements
#### Special Elements
#### Imagery

## Planning

## Technologies Used
### Languages Used
### Frameworks, Libraries & Programs Used
### Software & Web Applications Used

## Testing
### Browser Compatibility
### Manual Testing
#### Search and Pagination Functionality
<h3>User Authentication</h3>

<details>
<summary>Social Authentication</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Procedure</th>
      <th>Expected Result</th>
      <th>Actual Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Successful Google OAuth authentication and user creation</td>
      <td>
        1. Click "Sign in with Google"<br>
        2. Select a Google account<br>
        3. Grant permissions
      </td>
      <td>New user account created and logged in</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Successful Google OAuth authentication with existing user</td>
      <td>
        1. Click "Sign in with Google"<br>
        2. Select a previously used Google account
      </td>
      <td>Existing user logged in successfully</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Failed Google OAuth authentication</td>
      <td>
        1. Click "Sign in with Google"<br>
        2. Cancel the Google authentication process
      </td>
      <td>User remains on login page with error message</td>
      <td>✅ Pass</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>User Registration</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Procedure</th>
      <th>Expected Result</th>
      <th>Actual Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Successful user registration with valid data</td>
      <td>Enter valid name, email, and password</td>
      <td>Account created, verification email sent</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Registration with invalid password</td>
      <td>Enter valid name and email, but a password that doesn't meet requirements</td>
      <td>Error message displayed, registration prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Registration with invalid name</td>
      <td>Enter invalid name (e.g., numbers or special characters)</td>
      <td>Error message displayed, registration prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Registration with invalid email</td>
      <td>Enter an incorrectly formatted email address</td>
      <td>Error message displayed, registration prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Registration with existing email</td>
      <td>Attempt to register with an email already in use</td>
      <td>Error message displayed, registration prevented</td>
      <td>✅ Pass</td>
    </tr>
  </tbody>
</table>

</details>

<h3>Input Validation</h3>

<details>
<summary>Email Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Procedure</th>
      <th>Expected Result</th>
      <th>Actual Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Email validation with empty email</td>
      <td>Submit registration form with empty email field</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Email validation with existing email</td>
      <td>Enter an email address already registered</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Email validation with invalid email format</td>
      <td>Enter an incorrectly formatted email (e.g., missing @ symbol)</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Email validation with valid email</td>
      <td>Enter a correctly formatted, unused email address</td>
      <td>No error message, form submission allowed</td>
      <td>✅ Pass</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Name Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Procedure</th>
      <th>Expected Result</th>
      <th>Actual Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Name validation with empty name</td>
      <td>Submit registration form with empty name field</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Name validation with invalid characters</td>
      <td>Enter a name with numbers or special characters</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Name validation with valid name</td>
      <td>Enter a name with only letters and spaces</td>
      <td>No error message, form submission allowed</td>
      <td>✅ Pass</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Password Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Procedure</th>
      <th>Expected Result</th>
      <th>Actual Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Password validation with short password</td>
      <td>Enter a password shorter than the minimum required length</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Password validation with missing required characters</td>
      <td>Enter a password without required elements (e.g., uppercase, lowercase, number)</td>
      <td>Error message displayed, form submission prevented</td>
      <td>✅ Pass</td>
    </tr>
    <tr>
      <td>Password validation with valid password</td>
      <td>Enter a password meeting all requirements</td>
      <td>No error message, form submission allowed</td>
      <td>✅ Pass</td>
    </tr>
  </tbody>
</table>

</details>
#### User Verification
#### User Login and Logout
#### Expense Operations
### Device Testing
### W3C CSS Validator
### W3C HTML Validator
### CI Python Linter
### Lighthouse Testing
### JSHint
### Known Issues

## Deployment

### How to Clone the Repository
<details>
<summary>Click to expand</summary>
To clone this repository and run the E-commerce app locally, follow these steps:
1. **Open Terminal**: Open your terminal if you are on macOS or Linux, or open CMD or PowerShell if you are on Windows.
2. **Install Git**: Ensure you have Git installed on your system. You can download and install it from [Git's official site](https://git-scm.com/downloads).
3. **Clone the Repository**:
    ```bash
    git clone https://github.com/nathan-cool/E-commerce.git
    ```
4. **Navigate to the Project Directory**:
    ```bash
    cd E-commerce
    ```
5. **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
6. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
7. **Set Environment Variables**: Create a `.env` file in the root directory of the project and add the necessary environment variables like `DJANGO_SECRET_KEY`, `DATABASE_URL`, and any other required API keys.
8. **Migrate Database**:
    ```bash
    python manage.py migrate
    ```
9. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Once the server is running, you can access the E-commerce app at `http://127.0.0.1:8000` in your web browser.
10. **Access the Application**: Open a browser and go to `http://127.0.0.1:8000` to start using the E-commerce app.
</details>

### Create Application and Postgres DB on Heroku
<details>
<summary>Click to expand</summary>
1. **Sign Up or Log In to Heroku**:
    - Sign up at [Heroku's website](https://signup.heroku.com/) or log in if you already have an account.
2. **Create a New Application**:
    - Navigate to your Heroku dashboard.
    - Click on the "New" button and select "Create new app."
    - Enter a name for your application and select the region closest to your users.
    - Click on "Create app."
3. **Add a PostgreSQL Database**:
    - Go to the "Resources" tab in your Heroku dashboard.
    - In the "Add-ons" section, start typing "Heroku Postgres" and select it.
    - Choose the free "Hobby Dev" plan for development purposes.
    - Click "Submit Order Form" to add the PostgreSQL add-on to your application.
4. **Configure Environment Variables**:
    - Go to the "Settings" tab in your Heroku dashboard.
    - Under the "Config Vars" section, click on "Reveal Config Vars."
    - Add the necessary configuration variables such as `DJANGO_SECRET_KEY`, `DEBUG`, etc.
5. **Deploy Your Application**:
    - Connect your GitHub account under the "Deploy" tab by selecting "GitHub" as the deployment method.
    - Search for your repository and connect to it.
    - Enable Automatic Deploys or use the "Manual Deploy" section to deploy a specific branch.
6. **Run Migrations**:
    - After deploying, run your database migrations.
    - In the "More" dropdown menu, select "Run console."
    - Type `python manage.py migrate` and click "Run."
7. **Open Your App**: Click on the "Open app" button in the top right corner of the dashboard.
</details>


## Resources and Tutorials

- [Django Tutorial and Documentation:](https://docs.djangoproject.com/en/5.0/) Official Django documentation, tutorials, and guides covering all aspects of Django development.

- [Google Sign-In for server-side apps:](https://developers.google.com/identity/sign-in/web/backend-auth) Official Google documentation for implementing Google Sign-In.

- [Stack Overflow:](https://stackoverflow.com) For troubleshooting and finding solutions to specific programming problems.

- [W3Schools:](https://www.w3schools.com) Online Web Tutorials for various programming languages and web technologies.

- [MDN Web Docs:](https://developer.mozilla.org/en-US/) Resources for developers, by developers.

- [Django Search Tutorial:](https://learndjango.com/tutorials/django-search-tutorial) Tutorial for implementing search functionality in Django.

- [Django Pagination Tutorial:](https://simpleisbettercomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) Guide for implementing pagination in Django views.

- [OpenAI GPT-3.5:](https://openai.com/) AI model used for generating tutorial-like explanations.

- [GitHub Docs:](https://docs.github.com/en) Learn about GitHub features, from repositories to pull requests.

- [Heroku Dev Center:](https://devcenter.heroku.com/) Documentation and guides for deploying and managing applications on Heroku.

- [Bootstrap Documentation:](https://getbootstrap.com/docs/) Comprehensive guide for the Bootstrap framework.

- [Google Fonts:](https://fonts.google.com/) Free and easy-to-use web fonts.

- [Django Custom User Model Tutorial:](https://www.youtube.com/watch?v=tYPx-fcICts&list=PLx-q4INfd95G-wrEjKDAcTB1K-8n1sIiz&index=2) YouTube tutorial for implementing a custom user model in Django.

- Grammarly: AI-powered writing assistant for grammar checking, spell checking, and improving writing style and clarity.

- [REM Converter:](https://nekocalc.com/px-to-rem-converter) Used to convert PX to REM 

### Media 



### Acknowledgments

I would like to express my gratitude to the Slack Community for their invaluable assistance. Stephen Seagrave for helping me throughout my coding. My mentor Brian Macharia.
