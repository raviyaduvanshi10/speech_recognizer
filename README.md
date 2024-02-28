# Django App Setup Guide

This guide provides step-by-step instructions for setting up and running the Django app.

## Prerequisites

- Python 3.x installed on your system
- Anaconda or Miniconda installed ([Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html))

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/raviyaduvanshi10/speech_recognizer.git
   cd speech_recognizer
2. **Create Conda Enviornment:**
   conda env create -f environment.yml
   conda activate myDjangoEnv
3. **Run the Django Development Server:**
   python manage.py runserver