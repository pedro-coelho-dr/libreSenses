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

LibreSenses is a commitment to digital inclusivity and the spirit of free and open-source software and culture.

Explore the LibreSenses [Prototype](https://libresenses-service-ibu7uv3kqq-rj.a.run.app/).

For more information, visit the [LibreSenses Project Site](https://sites.google.com/cesar.school/libresenses/) (brazilian portuguese).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Development Process](#development-process)
- [Diagrams](#diagrams)
- [Tools](#tools)
- [Team](#team)
- [Credits](#credits)

## Installation

### Initial Setup Information
- This project was developed using WSL with Ubuntu and Visual Studio Code. While these are not mandatory, they are recommended.

### Prerequisites
- Python
- pip

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
  - See installation [documentation](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).
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
The current project settings are configured for deployment on Google Cloud. So it might not work immediately for local setups. Refer to `settings.py`, `cloudmigrate.yaml`, `Dockerfile`, and `Makefile` for more details. Additional information is available on [Google Cloud documentation](https://cloud.google.com/python/django/run).

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

In Django, the `models.py` file is at the heart of the application's data representation, defining the structure of the data that the application will work with using Python and Django's ORM (Object-Relational Mapping) system. It also defines the structure of the database, using classes and fields that Django translates into database tables.

#### Class Representation
Each model in Django is a Python class that subclasses `django.db.models.Model`. This is similar to defining a class in Java, where each class represents an entity with its attributes and behaviors. For example, the `Film` class represents the film entity with attributes like title, year, rating, and methods that define its actions.

#### Encapsulation
The models encapsulate the data fields and database operations. Each class, like `Caption` or `AudioDescription`, manages its interaction with the database, making sure that the data handling is secure and consistent.

#### Associations and Relationships
Django models handle relationships between different data entities effectively. For example, the use of ForeignKey in `Caption`, `AudioDescription`, `SignLanguage`, and `MediaAlternative` models to link to the `Film` model and establish associations between the objects.

#### Validations
The models also handle data validation. Methods like `validate_file_size` and validators like `FileExtensionValidator` and `MinValueValidator` are the last layer of validation to ensure data integrity.


### Implementing Views

In Django, `views.py` role is to handle the logic and control of the application (Django doesn´t have a separeted controller layer). It is responsible for processing incoming requests, preparing the data and sending the response back to the user. Views act as an intermediary between the models and templates.

This project utilizes class-based views. This method aligns with object-oriented principles, enhancing the code's organization, readability and maintainability.

#### Encapsulation
Each view class functions as an independent unit, managing its own state and behavior. For example, `FilmList` encapsulates the logic to retrieve and display the list of films, making the code more modular.

#### Inheritance
The use of class-based views allows for inheritance and extension of the view functionalities. This is useful for customizing specific behaviors for different views, like in `FilmProfile`, which can extend a generic view class with additional methods specific to film profiles.

#### Polymorphism
Different view classes can have methods with the same name but designed to handle different tasks. For example, the `post` method in `AddCaption` and `AddAudioDescription` classes are uniquely to handle different types of content submissions.

#### Abstraction
Class-based views abstract the complexity of operations. Methods like `get` or `post` in classes like `SubmitFilm` and `UpdateFilm` provides a simplified interface, hiding the complexity and making the code more friendly.

#### Modularity
Using class-based views also promotes a modular code structure, facilitating the development and testing of each component.


### Designing Forms

In Django, `forms.py` role is to define forms for user input interacting with the models. Views and forms work together, with views rendering forms and handling form submissions. Forms prioritize user inputs and validations, while views handle the request-response logic.

#### Class-Based
Each form is a class that defines how a model should be in the interface. `FilmForm` encapsulates all the fields and behaviors necessary to create or edit a film.

#### Encapsulation
Each form class in `forms.py` manages its state and behavior, encapsulating data, validation and presentation logic. This is evident in the `FilmForm` class, which handles the logic for input fields related to films.

#### Validation Layers
The forms have two layers of validation. The first layer comes from Django's built-in form validation. The second layer are custom validation methods in the form classes, like `validate_image_file_size` in `FilmForm` or `clean_caption_file` in `CaptionForm`.

#### Crispy Forms
Django Crispy Forms is used for layouts and styling, and may be integrated with Bootstrap. It allows for establishing layouts declaratively. For example, in `FilmForm`, the FormHelper and layout objects define how the form should be rendered, making it easy to manage form presentation.

### Front-end Development

In Django, templates are used for generating HTML dynamically. They allow the mixing of static HTML with Django Template Language (DTL) for dynamic content rendering. 

#### Template Inheritance
Using `{% extends 'index.html' %}` demonstrates template inheritance, allowing for a base template structure that can be extended or overridden in child templates.

#### Bootstrap for Responsive Design
This project integrates Bootstrap for responsive design. This framework provides a variety of pre-designed components and a grid system, simplifying the layout and design process.

#### Custom CSS
Together with Bootstrap, `custom.css` is used for additional styling for customization beyond Bootstrap's default styles, enabling personalized designs.

## Diagrams

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



