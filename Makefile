VENV_DIR = .venv
FLASK_APP = app.py
FLASK_RUN = flask run
TEST_DIR = src/tests
TRAIN_SCRIPT = src/models/train_models.py

ifeq ($(OS), Windows_NT)
	PYTHON = python
	PIP = pip
	MAKEDIR_VENV = 	mkdir $(VENV_DIR)
else
	PYTHON = python3
	PIP = pip3
	MAKEDIR_VENV = mkdir -p $(VENV_DIR)
endif

.SILENT:

# Default help target to guide users
help:
	@echo "Please use one of the following options:"
	@echo "  make venv               - Make a virtual environment for python project"
	@echo "  make build              - Setup project, install dependencies, train models."
	@echo "  make serve              - Serve the site without running tests."
	@echo "  make train              - Train the models using train_models script."
	@echo "  make test               - Run all tests in the application."
	@echo "  make clean              - Will remove all untracked file using .gitignore."

venv:
	@echo "Making virtual environment directory..."
	$(MAKEDIR_VENV)
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "To activate the virtual environment:"
	@echo "Run: source $(VENV_DIR)/bin/activate for linux."
	@echo "Run: $(VENV_DIR)\Scripts\activate for windows."

# Install dependencies and set up the project
build:
	$(PIP) install -e .
	$(PIP) install -r requirements.txt
	$(MAKE) train

train:
	@echo "Training prediction models..."
	$(PYTHON) $(TRAIN_SCRIPT)

# Serve the app without running tests
serve:
	$(FLASK_RUN) --debug

# Run all tests
test:
	@echo "Unit testing the project..."
	$(PYTHON) -m unittest discover $(TEST_DIR)

clean:
	echo "Cleaning untracked files..."
	git clean -d -f -X

.PHONY: venv build serve train test clean
