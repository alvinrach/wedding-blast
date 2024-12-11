# Wedding-Blast
- [Introduction](https://github.com/alvinrach/wedding-blast) 
- [Installation](https://github.com/alvinrach/wedding-blast) 
- [Usage](https://github.com/alvinrach/wedding-blast) 

#### Introduction
Creating a "wedding blast" for WhatsApp using Python can be interpreted in several ways. Most likely, you want to send out a large number of wedding-related messages to friends and family, either as invitations, reminders, or thank-you notes. To do this, you can use Python along with libraries like pywhatkit to automate WhatsApp messaging.

I’ll guide you through two common ways to do this:
#### Installation
##### Prerequisites
Install [Newer Python](https://www.python.org/downloads/) and runs also on  [Visual Studio Code](https://code.visualstudio.com/) or [PyPy](https://www.pypy.org/) or any others code editor
To check if you have Python installed, run the following command in your terminal:
``` 
python --version
```
and
``` 
python -m pip install --upgrade pip
```
##### Setting up a Virtual Environment
Step 1: Install `venv`
For most systems, `venv` is installed by default. If not, you can install it manually:
    On Windows: `venv` is included by default.

Step 2: Create a Virtual Environment
Navigate to your project folder:
``` 
cd /path/to/your/project
```
Create a virtual environment:
``` 
python -m venv venv
```

Step 3: Activate the Virtual Environment
``` 
.\venv\Scripts\activate
```
##### Installing Required Libraries
installs the Python packages specified in a requirements.txt file. This is a common practice to manage and share project dependencies, ensuring consistency across different environments or machines
``` 
pip install -r requirements.txt
```

#### Usage
Running Python Automation
1. Open a terminal (or command prompt) and navigate to the directory where script.py is located.
2. Run the following command:
``` 
python script.py
```
3. This will execute the script and perform the automation (sending whatsapp blast)
