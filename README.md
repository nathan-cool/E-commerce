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

# Features

## Existing Features

### Base Template and Layout

- **Responsive Design:** Built with Bootstrap 5.3.3 to ensure the site looks great on all devices. Custom CSS adds unique styling to make the design stand out.
  
- **Navigation:** 
  - A sticky top navbar with a dark theme makes navigation easy and accessible.
  - A collapsible sidebar menu adapts seamlessly to mobile devices, enhancing user experience on smaller screens.
  - The header displays the user's name and email
  - A convenient sign-out button is always available in the header for quick access.

- **Footer:** 
  - Includes a news letter signup
  - Provides a link to the GitHub repository for easy access to the source code.
  - Credits the creator, acknowledging their hard work and contributions.

### Authentication System and Security

#### Registration System

- **User Account Creation:** Users can easily create a new account by entering their name, email, and password. The system automatically splits the name into first and last names for better organization.

- **Form Validation:** 
  - Ensures that email addresses are in the correct format.
  - Requires strong passwords to enhance security.
  - Provides real-time error messages to help users fix any input mistakes.

- **Security Measures:** 
  - Implements CSRF protection to guard against cross-site request forgery attacks.
  - Uses Django's secure authentication mechanisms to handle user credentials safely.

- **Google Sign-In Integration:** Users have the option to sign up using their Google accounts, making the registration process quicker and more secure through Google's Identity Services.

#### Login System

- **User Authentication:** Allows users to log in using their registered email and password with robust form validation to ensure security.

- **Password Management:** Includes a password visibility toggle, so users can easily show or hide their passwords for convenience.

- **Security Measures:** 
  - Protects against CSRF attacks with built-in tokens.
  - Utilizes Django's secure protocols to manage user sessions safely.

- **Google Sign-In Integration:** Users can also log in using their Google accounts

### Messaging System

- **Dynamic Messages Display:** Uses Django's messaging framework to show success, error, and informational messages. These messages are styled with Bootstrap alerts for clear and attractive feedback.

### Security Enhancements

- **CSRF Protection:** All forms include CSRF tokens to protect against cross-site request forgery attacks.

- **Input Validation:** Validates and sanitizes all user inputs to prevent malicious data entry and enhance overall security.

- **Secure Authentication:** Relies on Django's built-in authentication system to manage user credentials and sessions securely.

### 1. Product Catalog

#### Product Listing:
- Displays all available products with **images**, **names**, **prices**, and **brief descriptions**.

#### Product Categories:
- Products are organized into **categories**.
- Users can **filter products** by selecting a category from the navigation menu.

### 3. Product Detail Page

#### Detailed View:
- Each product has a dedicated page showing **detailed information**.
- Includes **images**, **full descriptions**, **price**, and **stock availability**.
- Users can select the **quantity** and **add the product to their cart**.

### 4. Shopping Cart

#### Add to Cart:
- Users can **add products to their cart** from the product detail page.
- A **confirmation ** the cart icon updates with the amount 

#### View Cart:
- The cart displays all selected items with **quantities**, **individual prices**, and **total cost**.
- Users can **update quantities** or **remove items** directly from the cart.

### 5. Checkout Process

#### Secure Checkout:
- Users can **proceed to checkout** from their cart.
- Securely enter **billing details**.
- Integration with **Stripe** for payment processing.

#### Order Review:
- Users can **review their order** before final confirmation.
- Displays all items, shipping information, and total cost via stripe

### 8. Responsive Design

- The website is **fully responsive**, providing an optimal experience on **desktops**, **tablets**, and **mobile devices**.

### 9. Admin Panel

#### Product Management:
- Admins can **add new products** with details like **name**, **description**, **price**, **category**, and **images**.
- **Edit or delete existing products** via the home page.

#### Category Management:
- Admins can **create**, **edit**, or **delete product categories**.

#### Order Management:
- **View all orders** placed by customers.

### Future Features

## Design
### Wireframes

### Site map

![image](https://github.com/user-attachments/assets/22fa47b4-11d5-4051-9d48-6a0f3b4e9b43)

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

<details>
<summary>Browser Compatibility Table</summary>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Test Case</th>
      <th>Chrome</th>
      <th>Firefox</th>
      <th>Safari</th>
      <th>Edge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Registration System</td>
      <td>User can register a new account</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Login System</td>
      <td>User can log in with correct credentials</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Logout System</td>
      <td>Logged-in user can log out</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Google OAuth Integration</td>
      <td>User can authenticate using Google</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>View Expenses</td>
      <td>User can view all expenses</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Add Expenses</td>
      <td>User can add a new expense</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Edit Expenses</td>
      <td>User can edit an expense</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

### Manual Testing

#### User Authentication

##### Social Authentication

<details>
<summary>Test Cases for Social Authentication</summary>

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
      <td>Successful Google OAuth Authentication</td>
      <td>
        1. Click on "Sign in with Google" button.<br>
        2. Select a Google account.<br>
        3. Grant permissions when prompted.
      </td>
      <td>User is authenticated and redirected to the dashboard.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Cancel Google OAuth Authentication</td>
      <td>
        1. Click on "Sign in with Google" button.<br>
        2. Cancel or close the authentication window.
      </td>
      <td>User remains on the login page with an appropriate error message.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Google OAuth with Invalid Credentials</td>
      <td>
        1. Click on "Sign in with Google" button.<br>
        2. Enter invalid Google account credentials.
      </td>
      <td>User is not authenticated; an error message is displayed.</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### User Registration

<details>
<summary>Test Cases for User Registration</summary>

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
      <td>Register with Valid Details</td>
      <td>
        1. Navigate to the registration page.<br>
        2. Enter a valid name, email, and password.<br>
        3. Submit the form.
      </td>
      <td>User account is created; user is redirected to the dashboard.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Register with Existing Email</td>
      <td>
        1. Navigate to the registration page.<br>
        2. Enter an email that is already registered.<br>
        3. Submit the form.
      </td>
      <td>Error message displayed: "Email is already in use."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Register with Invalid Email Format</td>
      <td>
        1. Navigate to the registration page.<br>
        2. Enter an invalid email (e.g., "user@@example").<br>
        3. Submit the form.
      </td>
      <td>Error message displayed: "Enter a valid email address."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Register with Weak Password</td>
      <td>
        1. Navigate to the registration page.<br>
        2. Enter a password that is too short or lacks complexity.<br>
        3. Submit the form.
      </td>
      <td>Error message displayed: "Password must be at least 8 characters and include letters and numbers."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### User Login and Logout

<details>
<summary>Test Cases for User Login and Logout</summary>

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
      <td>Login with Correct Credentials</td>
      <td>
        1. Navigate to the login page.<br>
        2. Enter valid email and password.<br>
        3. Click "Login".
      </td>
      <td>User is logged in and redirected to the dashboard.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Login with Incorrect Password</td>
      <td>
        1. Navigate to the login page.<br>
        2. Enter valid email but incorrect password.<br>
        3. Click "Login".
      </td>
      <td>Error message displayed: "Invalid email or password."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Logout</td>
      <td>
        1. While logged in, click on the "Sign Out" button.
      </td>
      <td>User is logged out and redirected to the homepage.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Access Restricted Page After Logout</td>
      <td>
        1. Log out of the account.<br>
        2. Attempt to access the dashboard URL directly.
      </td>
      <td>User is redirected to the login page.</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

#### Input Validation

##### Email Validation

<details>
<summary>Test Cases for Email Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Input</th>
      <th>Expected Output</th>
      <th>Actual Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valid Email</td>
      <td>user@example.com</td>
      <td>Accepted; no error message.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Invalid Email (No @ Symbol)</td>
      <td>userexample.com</td>
      <td>Error message: "Enter a valid email address."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Invalid Email (Multiple @ Symbols)</td>
      <td>user@@example.com</td>
      <td>Error message: "Enter a valid email address."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Empty Email Field</td>
      <td>[Blank]</td>
      <td>Error message: "This field is required."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### Name Validation

<details>
<summary>Test Cases for Name Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Input</th>
      <th>Expected Output</th>
      <th>Actual Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valid Name</td>
      <td>John Doe</td>
      <td>Accepted; no error message.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Name with Numbers</td>
      <td>John123</td>
      <td>Error message: "Name cannot contain numbers."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Name with Special Characters</td>
      <td>John@Doe!</td>
      <td>Error message: "Name cannot contain special characters."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Empty Name Field</td>
      <td>[Blank]</td>
      <td>Error message: "This field is required."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### Password Validation

<details>
<summary>Test Cases for Password Validation</summary>

<table>
  <thead>
    <tr>
      <th>Test Case</th>
      <th>Input</th>
      <th>Expected Output</th>
      <th>Actual Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valid Password</td>
      <td>Passw0rd!</td>
      <td>Accepted; no error message.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Password Too Short</td>
      <td>Pass1</td>
      <td>Error message: "Password must be at least 8 characters."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Password Without Number</td>
      <td>Password!</td>
      <td>Error message: "Password must contain at least one number."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Password Without Special Character</td>
      <td>Passw0rd</td>
      <td>Error message: "Password must contain at least one special character."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Empty Password Field</td>
      <td>[Blank]</td>
      <td>Error message: "This field is required."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

#### Shopping Cart Functionality

##### Adding Items to Cart

<details>
<summary>Test Cases for Adding Items to Cart</summary>

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
      <td>Add Item from Product Page</td>
      <td>
        1. Navigate to a product page.<br>
        2. Select quantity.<br>
        3. Click "Add to Cart".
      </td>
      <td>Item is added to cart; cart icon updates with item count.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Add Item with Zero Quantity</td>
      <td>
        1. Navigate to a product page.<br>
        2. Set quantity to zero.<br>
        3. Click "Add to Cart".
      </td>
      <td>Error message: "Quantity must be at least 1."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Add Out-of-Stock Item</td>
      <td>
        1. Navigate to an out-of-stock product page.<br>
        2. Click "Add to Cart".
      </td>
      <td>Error message: "This item is currently out of stock."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### Updating Cart Items

<details>
<summary>Test Cases for Updating Cart Items</summary>

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
      <td>Increase Item Quantity</td>
      <td>
        1. Go to the cart page.<br>
        2. Increase the quantity of an item.<br>
        3. Click "Update Cart".
      </td>
      <td>Cart updates with new quantity and recalculated total.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Decrease Item Quantity</td>
      <td>
        1. Go to the cart page.<br>
        2. Decrease the quantity of an item.<br>
        3. Click "Update Cart".
      </td>
      <td>Cart updates with new quantity and recalculated total.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Set Quantity to Zero</td>
      <td>
        1. Go to the cart page.<br>
        2. Set item quantity to zero.<br>
        3. Click "Update Cart".
      </td>
      <td>Item is removed from the cart.</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

##### Removing Items from Cart

<details>
<summary>Test Cases for Removing Items from Cart</summary>

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
      <td>Remove Single Item</td>
      <td>
        1. Go to the cart page.<br>
        2. Click the "Remove" button next to an item.
      </td>
      <td>Item is removed from the cart; cart total updates.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Remove All Items</td>
      <td>
        1. Go to the cart page.<br>
        2. Remove all items individually.
      </td>
      <td>Cart is empty; message displayed: "Your cart is empty."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

#### Checkout Process

##### Payment Processing

<details>
<summary>Test Cases for Payment Processing</summary>

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
      <td>Successful Payment with Valid Card</td>
      <td>
        1. Proceed to checkout.<br>
        2. Enter valid billing and card details.<br>
        3. Confirm payment.
      </td>
      <td>Payment is processed; user receives confirmation.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Payment with Invalid Card Number</td>
      <td>
        1. Proceed to checkout.<br>
        2. Enter invalid card number.<br>
        3. Confirm payment.
      </td>
      <td>Error message: "Invalid card number."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Payment with Insufficient Funds</td>
      <td>
        1. Use a test card that simulates insufficient funds.<br>
        2. Confirm payment.
      </td>
      <td>Error message: "Payment declined due to insufficient funds."</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Payment with Expired Card</td>
      <td>
        1. Enter card details with past expiration date.<br>
        2. Confirm payment.
      </td>
      <td>Error message: "Card has expired."</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>


#### Admin Functions

##### Product Management

<details>
<summary>Test Cases for Product Management</summary>

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
      <td>Add New Product</td>
      <td>
        1. Log in as admin.<br>
        2. Navigate to "Add Product" page.<br>
        3. Fill in product details.<br>
        4. Submit the form.
      </td>
      <td>Product is added to the catalog; visible to customers.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Edit Existing Product</td>
      <td>
        1. Log in as admin.<br>
        2. Navigate to "Products" list.<br>
        3. Click "Edit" on a product.<br>
        4. Modify details.<br>
        5. Save changes.
      </td>
      <td>Product details are updated in the catalog.</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Delete Product</td>
      <td>
        1. Log in as admin.<br>
        2. Navigate to "Products" list.<br>
        3. Click "Delete" on a product.<br>
        4. Confirm deletion.
      </td>
      <td>Product is removed from the catalog.</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

### Device Testing

<details>
<summary>Device Compatibility Table</summary>

<table>
  <thead>
    <tr>
      <th>Device</th>
      <th>Browser</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Windows 10 PC</td>
      <td>Chrome</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>macOS Monterey</td>
      <td>Safari</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>iPad Pro</td>
      <td>Safari</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Samsung Galaxy Tab S6</td>
      <td>Chrome</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>iPhone 13</td>
      <td>Safari</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Google Pixel 6</td>
      <td>Chrome</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>Samsung Galaxy S21</td>
      <td>Samsung Internet</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

</details>

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
