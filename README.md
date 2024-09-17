# ExpenseEase
E-commerce is a user-friendly and secure website designed to provide customers with a seamless online shopping experience. With features like user account creation, product categorization, and a streamlined checkout process, E-commerce makes it easy for customers to browse, select, and purchase products from the comfort of their homes.

https://e-commerce-website-django-d6e595fc9613.herokuapp.com/

## Table of Contents
- [User Experience (UX)](#user-experience-ux)
  - [Project Goals](#project-goals)
  - [Development Strategy](#development-strategy)
  - [Epics](#epics)
  - [User Stories and Agile Methodology](#user-stories-and-agile-methodology)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Site Map](#site-map)
  - [Database Schema](#database-schema)
  - [The Surface Plane](#the-surface-plane)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Manual Testing](#manual-testing)
  - [Device Testing](#device-testing)
  - [W3C Validation](#w3c-css-validator)
  - [CI Python Linter](#ci-python-linter)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Known Bugs](#known-bugs)
- [Deployment](#deployment)
  - [How to Clone the Repository](#how-to-clone-the-repository)
  - [Create Application and Postgres DB on Heroku](#create-application-and-postgres-db-on-heroku)
- [Resources and Tutorials](#resources-and-tutorials)
- [Media](#media)
- [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Goals

The E-commerce Store project aims to create a user-friendly and secure online shopping experience. Our main objectives are:

- Provide a seamless platform for browsing and purchasing products
- Implement secure user authentication and order management
- Offer an intuitive interface for both customers and administrators
- Enhance the shopping experience with features like product categorization and search functionality

### Development Strategy

We employed the Agile methodology to plan and manage the development of our E-commerce Store:

- Used GitHub as the primary tool to demonstrate the Agile approach
- Created User Stories as GitHub Issues, linked to Epics
- Utilized custom issue templates for consistency and clarity
- Followed a specific format for each User Story, including title and description
- 
# User Stories and Agile Methodology

The development process was guided by user stories, managed through a Kanban board on GitHub Projects. Here's a breakdown of our key epics and user stories:

## Epics

1. User Account Management (E-commerce #14)
2. Product Browsing and Selection (E-commerce #15)
3. Shopping Cart Management (E-commerce #16)
4. Checkout and Order Management (E-commerce #17)
5. Inventory Management (E-commerce #18)
6. Order Processing (E-commerce #19)

## User Stories

1. Create an account so that I can manage my orders (E-commerce #1)
   * As a user, I want to create an account to manage my orders.
   * Priority: Must-Have
   * Acceptance Criteria:
      * User can access a registration page
      * User can enter necessary information
      * Account is created successfully
      * User can log in with new credentials

2. User Login (E-commerce #2)
   * As a user, I want to log in to access my account.
   * Priority: Must-Have
   * Acceptance Criteria:
      * Login page accessible
      * User can enter credentials
      * Successful login redirects to user dashboard
      * Error handling for incorrect credentials

3. View Product Catalog (E-commerce #3)
   * As a customer, I want to browse available products.
   * Priority: Must-Have
   * Acceptance Criteria:
      * Product catalog page accessible
      * Products displayed with basic information
      * Smooth navigation through catalog

4. Product Categories (E-commerce #4)
   * As a customer, I want to view products by category.
   * Priority: Should have
   * Acceptance Criteria:
      * Categories visible and selectable
      * Products filtered by selected category
      * Easy navigation between categories

5. Add to Cart (E-commerce #6)
   * As a customer, I want to add products to my shopping cart.
   * Priority: Must-Have
   * Acceptance Criteria:
      * "Add to Cart" button on product pages
      * Product successfully added to cart
      * Cart updates visibly

6. View and Edit Cart (E-commerce #7)
   * As a customer, I want to view and modify my shopping cart.
   * Priority: Must-Have
   * Acceptance Criteria:
      * Cart contents visible
      * Ability to change product quantities
      * Ability to remove items
      * Cart total updates accordingly

7. Checkout Process (E-commerce #8)
   * As a customer, I want to complete my purchase.
   * Priority: Must-Have
   * Acceptance Criteria:
      * Secure checkout process
      * Enter shipping and payment information
      * Order review before confirmation

8. Order Confirmation (E-commerce #9)
   * As a customer, I want to receive confirmation of my order.
   * Priority: Must-Have
   * Acceptance Criteria:
      * Order confirmation page displayed
      * Order details summarized
      * Confirmation email sent

9. View Order History (E-commerce #10)
   * As a customer, I want to view my past orders.
   * Priority: Should have
   * Acceptance Criteria:
      * Order history page accessible
      * List of past orders with basic details
      * Ability to view individual order details

10. Product Search (E-commerce #5)
    * As a customer, I want to search for specific products.
    * Priority: Should have
    * Acceptance Criteria:
      * Search bar accessible
      * Results display relevant products
      * Search works across product names and descriptions

11. Update Profile Information (E-commerce #11)
    * As a user, I want to update my account information.
    * Priority: Must-Have
    * Acceptance Criteria:
      * Profile edit page accessible
      * Fields for updating personal information
      * Changes save successfully

12. Manage Product Inventory (E-commerce #12)
    * As an admin, I want to manage the product inventory.
    * Priority: Must-Have
    * Acceptance Criteria:
      * Add new products
      * Edit existing product details
      * Update stock levels

13. Order Processing (E-commerce #13)
    * As an admin, I want to process customer orders.
    * Priority: Must-Have
    * Acceptance Criteria:
      * View list of new orders
      * Update order status
      * Add shipping information

### Agile Workflow

I managed our development process using a Kanban board on GitHub Projects:

![Kanban Board]) Image

Here is a link to my Kanban board: [ExpenseEase Project Board]([https://github.com/users/nathan-cool/projects/2/views/1](https://github.com/users/nathan-cool/projects/3))

My workflow consisted of three stages:
1. To Do
2. In Progress
3. Done

This Agile approach enabled me to:
- Prioritize features effectively
- Track progress consistently
- Ensure continuous delivery of value throughout development

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

<details>
  <summary><strong>Category Model</strong></summary>

Represents a product category in the e-commerce store.

**Fields**:
- `name`: CharField(max_length=255)
  - Stores the name of the category.

**Methods**:
- `__str__()`: Returns the name of the category.

**Meta**:
- `verbose_name_plural`: Changes the plural name of the model to 'categories'.

</details>

<details>
  <summary><strong>Customer Model</strong></summary>

Represents a customer in the e-commerce store.

**Fields**:
- `name`: CharField(max_length=255)
  - Stores the name of the customer.
- `email`: EmailField
  - Stores the email address of the customer.
- `phone`: CharField(max_length=255)
  - Stores the phone number of the customer.
- `password`: CharField(max_length=500)
  - Stores the customer's password (hashed).

**Methods**:
- `__str__()`: Returns the name of the customer.

</details>

<details>
  <summary><strong>Product Model</strong></summary>

Represents a product in the e-commerce store.

**Fields**:
- `name`: CharField(max_length=100)
  - Stores the name of the product.
- `price`: DecimalField(max_digits=10, decimal_places=2, default=0)
  - Stores the price of the product.
- `category`: ForeignKey(Category, on_delete=models.CASCADE, default=1)
  - Relates the product to a category.
- `product_title_description`: CharField(max_length=355, default='', null=True, blank=True)
  - Stores a short title or description of the product.
- `description`: CharField(max_length=2000, default='', null=True, blank=True)
  - Stores the detailed description of the product.
- `image`: ImageField(upload_to='uploads/products/')
  - Stores the product image.
- `is_sale`: BooleanField(default=False)
  - Indicates whether the product is on sale.
- `sale_price`: FloatField(default=0)
  - Stores the sale price of the product.
- `custom_badge`: CharField(max_length=6, default='', null=True, blank=True)
  - Stores a custom badge for the product, like "NEW" or "SALE".
- `qty`: IntegerField(default=0)
  - Stores the quantity of the product in stock.

**Methods**:
- `__str__()`: Returns the name of the product.

</details>

<details>
  <summary><strong>Order Model</strong></summary>

Represents an order placed by a customer.

**Fields**:
- `user`: ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  - Relates the order to a user.
- `quantity`: IntegerField(default=1)
  - Stores the quantity of the products ordered.
- `price`: DecimalField(max_digits=10, decimal_places=2)
  - Stores the total price of the order.
- `address`: CharField(max_length=255)
  - Stores the shipping address for the order.
- `phone`: CharField(max_length=255, blank=True, null=True)
  - Stores the customer's phone number.
- `date`: DateTimeField(default='django.utils.timezone.now')
  - Stores the date and time the order was placed.
- `status`: BooleanField(default=False)
  - Indicates the status of the order (e.g., completed or pending).

**Methods**:
- `__str__()`: Returns the name of the product in the order.

</details>

<details>
  <summary><strong>OrderItem Model</strong></summary>

Represents an individual item within an order.

**Fields**:
- `order`: ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  - Relates the order item to an order.
- `product`: ForeignKey(Product, on_delete=models.CASCADE)
  - Relates the order item to a product.
- `quantity`: PositiveIntegerField
  - Stores the quantity of the product in the order.
- `price`: DecimalField(max_digits=10, decimal_places=2)
  - Stores the price of the product.

**Methods**:
- `__str__()`: Returns a string in the format `quantity x product name`.

</details>

<details>
  <summary><strong>Profile Model</strong></summary>

Represents a user profile containing billing information.

**Fields**:
- `user`: OneToOneField(User, on_delete=models.CASCADE)
  - Relates the profile to a user.
- `billing_address_line1`: CharField(max_length=100)
  - Stores the first line of the billing address.
- `billing_address_line2`: CharField(max_length=100, blank=True, null=True)
  - Stores the second line of the billing address (optional).
- `city`: CharField(max_length=500)
  - Stores the city for the billing address.
- `county`: CharField(max_length=100)
  - Stores the county for the billing address.
- `eircode`: CharField(max_length=12)
  - Stores the postal code (Eircode).
- `country`: CharField(max_length=100, default='Ireland')
  - Stores the country for the billing address.

**Methods**:
- `__str__()`: Returns the username of the associated user.

</details>

<details>
  <summary><strong>Payment Model</strong></summary>

Represents a payment transaction.

**Fields**:
- `user`: ForeignKey(User, on_delete=models.CASCADE)
  - Relates the payment to a user.
- `order`: ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  - Relates the payment to an order.
- `profile`: ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  - Relates the payment to a user's profile.
- `amount`: DecimalField(max_digits=10, decimal_places=2)
  - Stores the amount of the payment.
- `stripe_payment_intent_id`: CharField(max_length=255)
  - Stores the Stripe payment intent ID.
- `status`: CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
  - Stores the status of the payment (e.g., pending, paid, failed).
- `timestamp`: DateTimeField(auto_now_add=True)
  - Stores the date and time when the payment was created.

**Methods**:
- `__str__()`: Returns a string showing the payment amount and user's username.

</details>





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
- **Python 3**: The core backend programming language used for the application.
- **HTML5**: Used for structuring the web pages of the application.
- **CSS3**: Used to style the HTML content.
- **JavaScript**: Employed for adding interactive behaviors to web pages.
- **Ajax**: Used for loading information without the need to reload the page

### Frameworks, Libraries & Programs Used
- **Django**: A high-level Python web framework used for developing the web application.
- **Python Standard Library**: Various modules such as `os`, `json`, and `re`.
- **dotenv**: Used for loading environment variables from a `.env` file.
- **Google OAuth**: Used for Google OAuth authentication.
- **JSON Web Tokens (JWT)**: Used for authentication and authorization.
- **Django Messages Framework**: Used to display success and error messages.
- **Django Authentication System**: For user registration, login, and logout functionality.
- **Django Email**: Used to send verification emails.

### Software & Web Applications Used
- **Git**: Used for version control.
- **GitHub**: For hosting Git repositories.
- **Visual Studio Code**: A code editor used for development.
- **Heroku**: Cloud platform used for deploying and hosting the web application.
- **PostgreSQL**: Used as the primary database.
- **Google Fonts**: Used for typography.
- **Balsamiq**: Used for creating mockups and prototypes.
- **Draw.io**: Used for creating visual representations of the application's architecture and user flows.

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
