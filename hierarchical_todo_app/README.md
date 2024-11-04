# Hierarchical Todo List App

## Description

This application is designed to help users organize tasks within a hierarchical to-do list structure. Users can create multiple lists, each containing tasks, sub-tasks, and sub-sub-tasks, enabling efficient task management. The hierarchy allows users to prioritize tasks, hiding details when necessary for focused work. Key features include task creation, editing, deletion, and task movement between lists, as well as the ability to collapse and expand task levels for easier navigation.

## Features

- **User Authentication**: Each user has a private account to manage their own lists and tasks securely.
- **Hierarchical Structure**: Tasks can be organized up to three levels deep (tasks, sub-tasks, sub-sub-tasks).
- **Task Management**: Users can create, edit, delete, and complete tasks within lists.
- **Visibility Control**: Expand or collapse tasks to show or hide sub-tasks for better focus.
- **Task Movement**: Easily move top-level tasks between different lists.
- **Persistent Storage**: Data is stored using SQLAlchemy to ensure durability.

## Installation and Setup

### Prerequisites

- Python 3.x

### Installation Instructions

1. **Download the Project Files**

   Download the ZIP file of the project and extract it to your desired directory.

2. **Set Up a Virtual Environment**

   Run the following commands in your terminal:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate.bat
     ```

4. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

6. **Access the Application**

   Open your browser and navigate to `http://localhost:5000` to start using the app.

## Usage Guide

### User Registration and Login

- **Register**: Create a new account on the registration page.
- **Login**: Access your account via the login page.

### Creating and Managing Lists

- **Create a List**: On the main dashboard, select **"Add New List"** to create a new task group.
- **Delete a List**: Delete any list from the dashboard along with its associated tasks.

### Adding and Managing Tasks

- **Add Tasks**: Open a list and click **"Add Task"** to create a new task. You can also add sub-tasks under any existing task, up to a maximum depth of three levels.
- **Complete Tasks**: Click **"Complete"** next to a task to mark it as complete and remove it from the list.

### Collapsing and Expanding Tasks

Use the **[+]** or **[-]** icons next to tasks to expand or collapse sub-tasks, making it easier to navigate through complex task lists.

### Moving Tasks Between Lists

From within a list, select a task and click **"Move Task"** to transfer it to a different list.

## MVP Requirements Fulfilled

This application meets the following requirements:

1. **User-Specific Task Management**: Each user has private lists and tasks.
2. **Task Completion**: Tasks can be marked as complete.
3. **Collapsible Tasks**: Tasks can be collapsed or expanded to control visibility.
4. **Task Movement**: Top-level tasks can be moved between lists.
5. **Persistent Storage**: Data is saved with SQLAlchemy to ensure persistence.
