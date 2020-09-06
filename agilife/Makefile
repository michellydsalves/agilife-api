include .env
export $(shell sed 's/=.*//' .env)
export REGISTRY_APP=$(APP_NAME)

# TEXT/COLORS
GREEN:=$(shell tput setaf 2)
BOLD:=$(shell tput bold)
RESET:=$(shell tput sgr0)


# MESSAGES
SUCCESS_MESSAGE:=OK
SUCCESS:=$(GREEN)$(SUCCESS_MESSAGE)$(RESET)

# PYTHON
PYTHON_VERSION=$(shell python3 --version)
ifndef PYTHON_VERSION
$(error Python 3 não instalado (https://www.python.org/downloads/))
endif

.PHONY: clean help

help:
	@echo "$(BOLD)clear$(RESET): limpar arquivos temporários"
	@echo ""
	@echo "$(BOLD)install$(RESET): executar todo processo pra iniciar o desenvolvimento ($(BOLD)$(GREEN)recomendado$(RESET))."
	@echo "$(BOLD)migrations$(RESET): criar e atualizar migrações."
	@echo "$(BOLD)create-superuser$(RESET): criar um usuário admin."
	@echo "$(BOLD)run$(RESET): subir a API (Django)."
	@echo ""
	@echo "$(BOLD)system-packages$(RESET): instalar dependências de sistema (pip e virtualenv)."
	@echo "$(BOLD)packages$(RESET): instalar dependências do projeto"
	@echo "$(BOLD)env-create$(RESET): criar ambiente virtual para desenvolvimento."
	@echo "$(BOLD)env-destroy$(RESET): apagar ambiente virtual de desenvolvimento."
	@echo ""
	@echo "$(BOLD)help$(RESET): exibir esta mensagem."

clear:
	@printf "Limpando arquivos temporários... "
	@rm -f dist/*.gz
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "$(SUCCESS)"

system-packages:
	@printf "Instalando 'pip' e 'virtualenv'... "
	@curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	@python3  -q  get-pip.py 1> /dev/null
	@pip install -q -U pip
	@pip install -q virtualenv
	@rm get-pip.py
	@echo "$(SUCCESS)"

env-create: env-destroy
	@printf "Criando ambiente virtual... "
	@virtualenv -q -p python3.6 venv
	@echo "$(SUCCESS)"

env-destroy:
	@printf "Destruindo ambiente virtual... "
	@rm -rfd venv
	@rm -rfd migrations
	@echo "$(SUCCESS)"

packages: env-create
	@printf "Instalando bibliotecas... "
	@venv/bin/pip install -q --no-cache-dir -r requirements.txt
	@echo "$(SUCCESS)"

install: clear system-packages packages
	@echo "============================================"
	@echo "Tudo pronto para o desenvolvimento"
	@echo ""
	@echo "Digite para ativar o ambiente: "
	@echo ""
	@echo "source venv/bin/activate"
	@echo "============================================"

migrations:
	@python manage.py makemigrations
	@python manage.py migrate

create-superuser:
	@python manage.py createsuperuser

run:
	@python manage.py runserver