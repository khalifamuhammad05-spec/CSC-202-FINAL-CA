
HEALTH CLINIC QUEUE MANAGER

## Project Overview
The Clinic Queue Manager is a simple web-based application developed using Python and Flask. It helps simulate a clinic's patient queue system where patients can be registered, placed in a queue, and called in the order they arrived.

The system follows the **FIFO (First In First Out)** principle using a queue data structure. It also keeps track of patients that have been attended to and records the time they were called.


---

## Features
- Register new patients into the queue
- View the current queue of waiting patients
- Call the next patient in line
- Display the number of patients waiting
- Display the number of patients seen today
- Track the last patient called
- Maintain a history of patients served with checkout time
- Toggle button to show/hide patient history
- Simple dashboard-style user interface

---

## Technologies Used
- **Python**
- **Flask (Web Framework)**
- **HTML**
- **CSS**
- **Git & GitHub**
- **datetime module (Python Standard Library)**

---


**File descriptions**

- `app.py` – Main Flask application and routes
- `queue_manager.py` – Handles queue logic and patient management
- `models.py` – Contains the Patient class
- `templates/` – HTML pages used by Flask

---

## How the System Works
1. A patient is registered using the **Register Patient** form.
2. The patient is added to a queue.
3. The system displays all waiting patients on the dashboard.
4. When **Call Next Patient** is clicked, the first patient in the queue is removed.
5. The system records the patient in the **history list** with the checkout time.
6. The dashboard updates automatically with the new queue status.

---

## How to Run the Project
```bash
Step 1: Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/CSC-202-FINAL-CA.git

Step 2: Navigate into the Project Folder
cd CSC-202-FINAL-CA

Step 3: Install Flask (if not installed)
pip install flask

Step 4: Run the Application
python app.py

Step 5: Open the Application in Your Browser
Go to: http://127.0.0.1:5000
You will now see the Clinic Queue Manager dashboard.

## Author
Usman Usman Muhammad
MAAUN/24/CBS/0044 
CSC 202 – Continuous Assessment Project