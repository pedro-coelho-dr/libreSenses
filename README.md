Libresenses

https://libresenses.onrender.com/

============
-> O que é?

Setup inicial 
-> Explicar render
-> explicar como rodar em modo dev.
->
-> Explicar funcionamento do app
-> models e forms / + validações
-> views CBV
-> Templates
-> wireframe/prototipo
-> arquitetura/diagrama
--
Ferramentas
Equipe


Project setup

[Virtualenvwrapper]
(https://virtualenvwrapper.readthedocs.io/)

sudo pip install virtualenvwrapper

virtualenvwrapper --version

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

workon

mkvirtualenv venv-libresenses

workon venv-libresenses

[Poetry]
(https://python-poetry.org/)

curl -sSL https://install.python-poetry.org | python3 -

poetry --version

poetry self update

poetry install


[Makefile]

Commands:

make venv
make install
make migrate
make migrations
make runserver
make superuser

