# Restaurant Management System API

### This project is a Django-based RESTful API for managing restaurants, menus, employees, orders, and user authentication. It provides various endpoints for owners and employees to perform operations related to restaurant management and order processing.

## Table of Contents
- [Getting Started](#getting-started)
- [Environment Setup](#environment-setup)
- [Running the Application](#running-the-application)
- [Docker Setup](#docker-setup)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Password Management](#password-management)
  - [Employee Management](#employee-management)
  - [Order Management](#order-management)
  - [Menu Management](#menu-management)
  - [Menu Item Management](#menu-item-management)
  - [Restaurant Management](#restaurant-management)
  - [Owner/User Management](#owneruser-management)


#### Getting Started
* To get started with the project, clone the repository using the following command:

```bash
git clone https://github.com/emoncse/Restaurant_Management_System_RMS.git
cd Restaurant_Management_System_RMS
```

#### Environment Setup
Create a `.env` file in the root directory of the project to store your environment variables. Example content for `.env`:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
STRIPE_SECRET_KEY=your_stripe_secret_key_here
```
Ensure you replace the placeholders with your actual configuration values.

#### Running the Application
Once you have your environment set up, you can proceed with the following steps:

**Install Dependencies:**

If you haven't done so already, create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

**Apply Migrations:**

Run the following commands to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Run the Server:**

Start the Django development server:

```bash
python manage.py runserver
```
The application should now be running on `http://127.0.0.1:8000/`.

#### Docker Setup
If you prefer to use Docker, follow these steps:

**Build and Start the Containers:**

```bash
docker-compose up --build -d
```
This command will build the Docker images and start the containers in detached mode.

**Access the Application:**

The application should be accessible at `http://localhost:8000/`.

## API Endpoints

### Authentication
- **Login**: `POST /authentication/v1/login/`
- **Logout**: `POST /authentication/v1/logout/`
- **Logout All Sessions**: `POST /authentication/v1/logout/all/`
- **Token Refresh**: `POST /authentication/v1/token/refresh/`
- **Token Verify**: `POST /authentication/v1/token/verify/`

### Password Management
- **Change Password**: `POST /password/v1/change/`

### Employee Management
- **List Employees**: `GET /restaurant/v1/employee/`
- **Create Employee**: `POST /restaurant/v1/employee/`
- **Retrieve Employee**: `GET /restaurant/v1/employee/{id}/`
- **Update Employee**: `PUT /restaurant/v1/employee/{id}/`
- **Partial Update Employee**: `PATCH /restaurant/v1/employee/{id}/`
- **Delete Employee**: `DELETE /restaurant/v1/employee/{id}/`

### Order Management
- **List Orders**: `GET /restaurant/v1/list/`
- **Update Order Status**: `PUT /restaurant/v1/order-status-update/{id}/`
- **Create Order**: `POST /restaurant/v1/order_create/`
- **Retrieve Order**: `GET /restaurant/v1/retrieve-order/{id}/`
- **Delete Order by Tracking ID**: `DELETE /restaurant/v1/track-order/{traking_id}/`

### Menu Management
- **List Menus**: `GET /restaurant/v1/menu/`
- **Create Menu**: `POST /restaurant/v1/menu/`
- **Retrieve Menu**: `GET /restaurant/v1/menu/{id}/`
- **Update Menu**: `PUT /restaurant/v1/menu/{id}/`
- **Partial Update Menu**: `PATCH /restaurant/v1/menu/{id}/`
- **Delete Menu**: `DELETE /restaurant/v1/menu/{id}/`

### Menu Item Management
- **List Menu Items**: `GET /restaurant/v1/menu_item/`
- **Create Menu Item**: `POST /restaurant/v1/menu_item/`
- **Retrieve Menu Item**: `GET /restaurant/v1/menu_item/{id}/`
- **Update Menu Item**: `PUT /restaurant/v1/menu_item/{id}/`
- **Partial Update Menu Item**: `PATCH /restaurant/v1/menu_item/{id}/`
- **Delete Menu Item**: `DELETE /restaurant/v1/menu_item/{id}/`

### Restaurant Management
- **List Restaurants**: `GET /restaurant/v1/restaurant/`
- **Create Restaurant**: `POST /restaurant/v1/restaurant/`
- **Retrieve Restaurant**: `GET /restaurant/v1/restaurant/{id}/`
- **Update Restaurant**: `PUT /restaurant/v1/restaurant/{id}/`
- **Partial Update Restaurant**: `PATCH /restaurant/v1/restaurant/{id}/`
- **Delete Restaurant**: `DELETE /restaurant/v1/restaurant/{id}/`

### Owner/User Management
- **Create User**: `POST /user/v1/create/`
- **Delete User**: `DELETE /user/v1/delete/{id}/`
- **List Users**: `GET /user/v1/list/`
- **Retrieve User**: `GET /user/v1/retrieve/{id}/`
- **Update User**: `PUT /user/v1/update/{id}/`
