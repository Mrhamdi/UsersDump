
# UsersDump

**UsersDump** is a FastAPI project designed for front-end developers to test and integrate user management functionalities. This project provides a simple and effective way to simulate common user operations, including adding, logging in, searching, deleting, and updating users.

---

## Features
- **Add Users**: Create new user entries.
- **Login**: Simulate user authentication.
- **Search Users**: Retrieve user information based on specific criteria.
- **Delete Users**: Remove user records.
- **Update Users**: Modify existing user details.

---

## User Fields
- **ID**: Unique identifier for each user.
- **First Name**: The user's first name.
- **Last Name**: The user's last name.
- **Username**: The user's chosen username.
- **Password**: Stored in plaintext for testing purposes (no hashing applied).

---

## Requirements
- **Python 3.9+**
- **FastAPI**
- **Uvicorn**

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/usersdump.git
   cd usersdump
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API documentation at `http://127.0.0.1:8000/docs`.

---

## Project Image
![UsersDump](./usersdump_demo.png)

---

## License
This project is licensed under the MIT License.
