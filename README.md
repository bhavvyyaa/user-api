# REST API for User Management

## 🎯 Objective
This project implements a complete **RESTful API** using the **Flask** micro-framework to manage user data (CRUD operations: Create, Read, Update, Delete) using an in-memory Python list.

## 🛠️ Tools and Key Concepts
**Language/Framework:** Python, Flask.
**Testing Tools:** cURL or Postman.
**Key Concepts:** REST, HTTP Methods (GET, POST, PUT, DELETE), JSON.
*  **Storage:** Users are stored in an in-memory list/dictionary.

***

## ⚙️ Setup and Running the API

1.  **Install Flask:**
    ```bash
    pip install Flask
    ```

2.  **Run the Application:**
    Save the code above as `app.py` and execute:
    ```bash
    python app.py
    ```
    The API will start running at the base URL: `http://127.0.0.1:5000/`

***

## 🌐 API Endpoints and Usage

The API provides full management for the `/users` resource.

| CRUD Operation | HTTP Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- | :--- |
| **Read All** | `GET` | `/users` | Retrieves the list of all users. | `200 OK` |
| **Create** | `POST` | `/users` | Creates a new user (requires JSON body). | `201 Created` / `400 Bad Request` |
| **Read One** | `GET` | `/users/<id>` | Retrieves a single user by ID. | `200 OK` / `404 Not Found` [cite: 18] |
| **Update** | `PUT` | `/users/<id>` | Updates an existing user (requires JSON body). | `200 OK` / `404 Not Found` |
| **Delete** | `DELETE` | `/users/<id>` | Deletes a user by ID. | `204 No Content` / `404 Not Found` [cite: 18] |

***
