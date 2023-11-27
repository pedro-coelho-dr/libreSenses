# LibreSenses
[Prototype](https://libresenses-service-ibu7uv3kqq-rj.a.run.app/)
## Introduction
LibreSenses is a Django web application developed as part of the 'Projects 3' course at [Cesar School](https://cesar.school/). This project enhances the Libreflix platform, a peer-to-peer streaming service focused on free streaming of movies. LibreSenses aligns with the ethos of free culture and software, embodying the principles of [Libreflix](https://libreflix.org).

The core functionality of LibreSenses centers around accessible content submission, specifically designed to meet the diverse requirements of viewers, including those with disabilities.
The application provides a user-friendly interface for submitting and managing films, to enhance accessibility in line with the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/) standards.

### Key Features
- **Film Submission Form**: Mirroring the current Libreflix submission form, enabling new productions to be added to the platform.
- **Film List**: Displays a catalog of registered movies for viewing and interaction.
- **Film Profiles**:  Allows for editing film details and adding accessibility features such as subtitles, audiodescription, sign language and alternative media.
- **Accessibility Techniques**: Implements WCAG-compliant techniques across levels A, AA, and AAA.
- **Additional Resources**: Offers reference links and resources on accessibility guidelines.

LibreSenses is a commitment to digital inclusivity and the spirit of free and opensource software and culture.

Explore the LibreSenses [Prototype](https://libresenses-service-ibu7uv3kqq-rj.a.run.app/).

For more information. visit the [LibreSenses Project Site](https://sites.google.com/cesar.school/libresenses/) (brazilian portuguese).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Development Process](#development-process)
- [Diagrams](#diagrams)
- [Tools](#tools)
- [Team](#team)
- [Credits](#credits)
- [License](#license)

## Installation

### Initial Setup Information
- This project was developed using WSL (Windows Subsystem for Linux) Ubuntu and Visual Studio Code (VSCode). While these are not mandatory, they are recommended.

### Prerequisites
- Python
- pip (Python package manager)

### Setting Up a Development Environment
1. **Clone the repository:** 
    ```
    git clone https://github.com/pedro-coelho-dr/libresenses.git
    ```
2. **Navigate to the project directory:** 
    ```
    cd libresenses
    ```
    _Replace 'libresenses' with your actual project directory._
3. **Set up a virtual environment:**
- Install [virtualenv](https://virtualenv.pypa.io/):
  ```
  pip install virtualenv
  ```
- Create a virtual environment:
  ```
  virtualenv venv
  ```
- Activate the virtual environment:
  - On Windows:
    ```
    .\venv\Scripts\activate
    ```
  - On Unix or MacOS:
    ```
    source venv/bin/activate
    ```
- Alternatively, use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/) (recommended):
  - Install virtualenvwrapper:
    ```
    pip install virtualenvwrapper
    ```
  - See installation instructions on the [documentation](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).
  - Create and work on a new virtual environment:
    ```
    mkvirtualenv venv-libresenses
    workon venv-libresenses
    ```
4. **Install dependencies:**
    ```
    make requirements
    ```
    _This runs 'pip install -r requirements.txt'_

### Note on Deployment Settings
The current project settings are configured for deployment on Google Cloud. So, it might not work immediately for local setups. Refer to `settings.py`, `cloudmigrate.yaml`, `Dockerfile`, and `Makefile` for more details. Additional information is available on [Google Cloud documentation](https://cloud.google.com/python/django/run).

To run the project locally:
- Rename `settings_development.py` to `settings.py`.

### Running the Project

1. **Initialize migrations:**
    ```
    make migrations-init
    ```
    _This runs 'python manage.py makemigrations libresenses'_

3. **Create a superuser:**
    ```
    make superuser
    ```
    _This runs 'python manage.py createsuperuser'_

4. **Apply migrations:**
    ```
    make migrations
    make migrate
    ```
    _This runs 'python manage.py makemigrations' and 'python manage.py migrate'_

5. **Run the server:**
    ```
    make run 
    ```
    _This runs 'python manage.py runserver 8080'_


## Usage

## Development Process

### Creating Models


### Implementing Views


### Designing Forms


### Front-end Development


## Diagrams


## Tools

## Tools

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Poetry](https://python-poetry.org/)
- [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Graphviz](https://graphviz.org/)
- [Figma](https://www.figma.com/)
- [GitHub](https://github.com/)
- [Docker](https://www.docker.com/)
- [Google Cloud](https://cloud.google.com/)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/about)
- [Ubuntu](https://ubuntu.com/)


## Team


## Credits


## License

