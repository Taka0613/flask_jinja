# Hierarchical Todo List App

## Description

This application allows users to create hierarchical to-do lists with up to three levels of tasks. Users can create multiple lists, with each list containing tasks, sub-tasks, and sub-sub-tasks. The hierarchical structure lets users focus on the most important tasks, hiding details until needed. Users can create, edit, delete, and move tasks between lists, with the option to collapse and expand items to manage visibility.

## Features

- **Multiple Users**: Each user has their own private lists and tasks.
- **Hierarchical Task Structure**: Allows for tasks with sub-tasks, up to three levels deep.
- **Task Management**: Create, edit, delete, and complete tasks.
- **Visibility Control**: Users can collapse/expand tasks to show or hide sub-tasks.
- **Task Movement**: Move top-level tasks between lists.
- **Persistent Data Storage**: Data is saved in a durable format using SQLAlchemy for easy database management.

## Installation and Setup

### Prerequisites

- Python 3.x

### Installation Instructions

1. **Download zip file to your directory**

2. **Set Up the Virtual Environment**:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate.bat
     ```

4. **Install Dependencies**:

   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the Application**:

   - On macOS/Linux:
     ```bash
     python3 app.py
     ```
   - On Windows:
     ```cmd
     python app.py
     ```

6. **Access the Application**:

   Open a browser and go to `http://localhost:5000` to access the app.

## MVP Requirements Fulfilled

This application meets the following minimum viable product (MVP) requirements:

1. **Multiple Users**: User-specific lists and tasks.
2. **Task Ownership**: Users can only see and manage their own tasks.
3. **Task Completion**: Mark tasks as complete.
4. **Collapsible Tasks**: Show or hide sub-tasks.
5. **Task Movement**: Move top-level tasks between different lists.
6. **Durable Storage**: Data stored in SQLAlchemy to ensure persistence.

## Usage Instructions

### Creating a List

1. Log in or register as a new user.
2. On the main dashboard, select "Add New List" to create a new to-do list.

### Adding Tasks

1. Open any list to view or manage tasks.
2. Click "Add Task" to create a new task in the list.
3. You can add sub-tasks to existing tasks, up to a maximum depth of three levels.

### Collapsing and Expanding Tasks

Click on the **[+]** or **[-]** icon next to any task with sub-tasks to toggle visibility.

### Completing Tasks

Click "Complete" next to any task to mark it as complete.

### Moving Tasks Between Lists

From the list view, click "Move Task" to transfer a top-level task to a different list.
