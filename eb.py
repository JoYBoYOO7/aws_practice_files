#Create a Project Folder name it my-aws-app.
#application.py
from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    my_name = "Vansh Yadav"
    my_location = "Vellore, India"
    my_interest = "Coding and Music"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My AWS Beanstalk App</title>
        <style>
            body {{ font-family: sans-serif; background-color: #f4f4f4; color: #333; }}
            .container {{ max-width: 700px; margin: 50px auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            h1 {{ color: #005A9C; }}
            p {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from AWS!</h1>
            <p>My name is <strong>{my_name}</strong>.</p>
            <p>I am running this Python application from <strong>{my_location}</strong>.</p>
            <p>One of my interests is: <strong>{my_interest}</strong>.</p>
            <p><small>This app is running on an Amazon Linux server, deployed via the AWS Console.</small></p>
        </div>
    </body>
    </html>
    """
    return html_content

# Create the Requirements File
# Inside the same my-aws-app folder, create another text file named requirements.txt. This file tells AWS which Python libraries to install. Add the following line to it:
# Flask
# Create the Deployment ZIP File
# This is the most important step for the manual process. You need to create a .zip file that contains your code.
# Open your my-aws-app folder.
# Select both files: application.py and requirements.txt.
# Right-click on the selected files and choose "Compress" or "Send to > Compressed (zipped) folder".
# Name the resulting zip file my-app.zip.
# Crucial: Make sure the .zip file contains application.py and requirements.txt directly, not the my-aws-app folder itself.
# Correct Structure inside my-app.zip:
# - application.py
# - requirements.txt

# Part 2: Deploy Using the AWS Management Console
# Navigate to Elastic Beanstalk
# Create a New Application
# Click the "Create Application" button.
# Configure Environment Settings
# You will now see a form to configure your application.
# Environment tier: Keep "Web server environment" selected.
# Application name: Enter a name, for example, My Personal App.
# Environment name: It will auto-fill based on the application name (e.g., My-Personal-App-env). You can leave this as is.
# Domain: You can enter a unique name to form your URL, like [your-unique-name]-app. This must be globally unique.
# Platform:
# From the dropdown, select "Python".
# Platform branch: Choose the latest recommended version available, which will be something like Python 3.11 on 64bit Amazon Linux 2023.
# Note on Python 3.13: The AWS console might not list the absolute latest Python version immediately after its release. Select the newest one available (e.g., 3.11 or 3.12). The simple code we wrote will work perfectly on these versions.
# Application code:
# Select "Upload your code".
# Under "Source code origin", click the "Choose file" button.
# Select the my-app.zip file you created in Part 1.
# Presets: To keep costs low, select "Single instance (Free tier eligible)".
# Create the Environment
# Scroll to the bottom and click "Create environment".
# Wait for the Launch
# AWS will now start building your environment. This process takes 5-10 minutes. You will see a dashboard with logs and the environment's health status. Wait until the health status turns to "Ok" (Green).
# View Your Application
# Once the environment is ready, the URL for your application will be displayed at the top of the dashboard. Click on it to see your live website!
# Part 3: How to Update Your Application
# If you make changes to your application.py file locally:
# Re-create the my-app.zip file with the updated files, following the same steps as in Part 1.
# Go to your Elastic Beanstalk environment's dashboard in the AWS Console.
# Click the "Upload and deploy" button.
# Choose your new my-app.zip file and click "Deploy".
# Wait a few minutes for the update to complete.
