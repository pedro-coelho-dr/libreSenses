# LibreSenses
[Prototype](https://libresenses-service-ibu7uv3kqq-rj.a.run.app/)
## Intro
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

For more information, visit the [LibreSenses Project Site](https://sites.google.com/cesar.school/libresenses/).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Diagrams](#diagrams)
- [Tools](#tools)
- [Team](#team)

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
### Submit film
To submit a film, navigate to the 'Enviar um filme'(Submit Film) section. Fill out the film submission form with the required details including title, description, and upload options.
<br><img width="547" alt="New film form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/5b735e12-c37f-41b1-8269-6b4f5fe93440">
### Film profile
View and manage film profiles by selecting a film from the list. Here you can review detailed information and access editing options.
<br><img width="496" alt="Screenshot 2023-11-29 175352" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/e9e2f08b-0293-4ab3-8973-00b9f3a90ba5">
#### Accessibility profile

View the accessibility features that have been added to your film. 
<br><img width="492" alt="film profile form accesibility details" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/a9432bf6-1c68-4c10-ae00-428b5985fa51">
#### Delete film entry
To remove a film, simply use the 'Remover Conteúdo Audiovisual' (Delete) button option available in the film's profile.
<br><img width="161" alt="remove button form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/aade7aa4-4188-4640-924e-1dde6236c6bb">
### Edit film informations
Update film details through the 'Editar'(Edit) option in the film profile. Make sure to save changes after editing.
<br><img width="494" alt="edit film info form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/b3828082-166e-44c2-9818-8d344461cf11">
### Add accessibility
Enhance the accessibility of your films by adding various features. Each type of accessibility feature can be easily added through dedicated forms.
#### Captions
Add captions to your film to make it accessible for the deaf or hard of hearing audience. 
<br><img width="495" alt="caption form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/3a418329-cf49-4853-b24f-9cf860bf90e3"><br>
#### Audiodescription
Provide an audiodescription to describe visual elements for visually impaired viewers. 
<br><img width="497" alt="audio description form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/2d966860-7f46-497a-a855-2e85a52abd2b"><br>
#### Sign language
Incorporate sign language interpretation into your film.
<br><img width="497" alt="sign language form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/cdd46925-d7ba-4e7e-ae3f-8a81906993d5">
#### Media Alternative
Offer alternative media options for enhanced accessibility. This could include different formats like Braille or simplified text versions.
<br><img width="493" alt="media alternative form" src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/84ff3dcf-fcf5-45a9-935c-05a46924cc58">


## Development

### Creating Models

The `models.py` file is at the heart of the application's data representation, defining the structure of the data that the application will work with using Python and Django's ORM (Object-Relational Mapping) system. It also defines the structure of the database, using classes and fields that Django translates into database tables.

#### Class Representation
Each model in Django is a Python class that subclasses `django.db.models.Model`. This is similar to defining a class in Java, where each class represents an entity with its attributes and behaviors. For example, the `Film` class represents the film entity with attributes like title, year, rating, and methods that define its actions.

#### Encapsulation
The models encapsulate the data fields and database operations. Each class, like `Caption` or `AudioDescription`, manages its interaction with the database, making sure that the data handling is secure and consistent.

#### Associations and Relationships
Models handle relationships between different data entities effectively. For example, the use of ForeignKey in `Caption`, `AudioDescription`, `SignLanguage`, and `MediaAlternative` models to link to the `Film` model and establish associations between the objects.

#### Validations
The models also handle data validation. Methods like `validate_file_size` and validators like `FileExtensionValidator` and `MinValueValidator` are the last layer of validation to ensure data integrity.

---

### Implementing Views

`views.py` role is to handle the logic and control of the application (Django doesn´t have a separeted controller layer). It is responsible for processing incoming requests, preparing the data and sending the response back to the user. Views act as an intermediary between the models and templates.

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

---

### Designing Forms

`forms.py` role is to define forms for user input interacting with the models. Views and forms work together, with views rendering forms and handling form submissions. Forms prioritize user inputs and validations, while views handle the request-response logic.

#### Class-Based
Each form is a class that defines how a model should be in the interface. `FilmForm` encapsulates all the fields and behaviors necessary to create or edit a film.

#### Encapsulation
Each form class in `forms.py` manages its state and behavior, encapsulating data, validation and presentation logic. This is evident in the `FilmForm` class, which handles the logic for input fields related to films.

#### Validation Layers
The forms have two layers of validation. The first layer comes from Django's built-in form validation. The second layer are custom validation methods in the form classes, like `validate_image_file_size` in `FilmForm` or `clean_caption_file` in `CaptionForm`.

#### Crispy Forms
Crispy Forms is used for layouts and styling, and may be integrated with Bootstrap. It allows for establishing layouts declaratively. For example, in `FilmForm`, the FormHelper and layout objects define how the form should be rendered, making it easy to manage form presentation.

---

### Front-end Development

Templates are used for generating HTML dynamically. They allow the mixing of static HTML with Django Template Language (DTL) for dynamic content rendering. 

#### Template Inheritance
Using `{% extends 'index.html' %}` demonstrates template inheritance, allowing for a base template structure that can extend or override child templates.

#### Bootstrap for Responsive Design
This project integrates Bootstrap for responsive design. This framework provides a variety of pre-designed components and a grid system, simplifying the layout and design process.

#### Custom CSS
Together with Bootstrap, `custom.css` is used for additional styling for customization beyond Bootstrap's default styles, enabling personalized designs.

## Diagrams

![diagrama](https://github.com/pedro-coelho-dr/libresenses/assets/111138996/ad792ecc-4fe9-4143-8925-45f9980aac74)<br>
![libresenses_models](https://github.com/pedro-coelho-dr/libresenses/assets/111138996/14a715b2-6b35-4baa-8d4e-7374a87deba1)<br>

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

Gabriela Lyra<br>
Marília Pacífico<br>
Raul Correia<br>
Yanne Lopes<br>
Camila Cirne<br>
Lucas Lucena<br>
Lucas Dias<br>
Pedro Coelho<br>
Rafael Menezes<br>
Matheus Lazzarotto<br>

---

[<img src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/13bbf93e-6d09-4dbd-852a-6207e525b8ec" width="80">](https://sites.google.com/cesar.school/libresenses/)<br><br>
[<img src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/9d8731c2-66ed-418d-ac4a-86df53dd06dc" width="80">](https://libreflix.org)<br><br>
[<img src="https://github.com/pedro-coelho-dr/libresenses/assets/111138996/87ec00b4-772a-46ae-88ea-f19d6d486b5d" width="80">](https://cesar.school/)<br><br>


