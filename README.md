# Sticky Notes Application

## Overview

This is a Django-based sticky notes application that allows users to create,
edit, delete, and view sticky notes. Users can also post on a bulletin board.

## Features

- User authentication and session management
- Create, edit, delete, and view sticky notes
- Post on a bulletin board
- Responsive design with Bootstrap

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sticky-notes-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sticky-notes-app
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

After starting the development server, you can access the application at `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
