# Getting Started 

This repo is the submission of Challenge No. 1/4 mentioned in the Assignment Guidelines and I've done my best to see if all the requirements that were mentioned
in the assignment guidelines are met and instructions for evaluation and testing are given below in the [Usage and Testing](https://github.com/adamofarch/nextbige_assignment/blob/main/README.md#usage-and-testing) section below.

# Installation 

## Method 1: Using Docker(Recommended)

**Step 1:** Install Docker for your machine:
  - **Linux (Debian based)**
    1. Set up Docker's apt repository
       ```sh
        # Add Docker's official GPG key:
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc
        
        # Add the repository to Apt sources:
        echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
          $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
          sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update
      - Note: `If you use an Ubuntu derivative distribution, such as Linux Mint, you may need to use UBUNTU_CODENAME instead of VERSION_CODENAME`

    2. Install the Docker Package
       ```sh
       sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    3. Verify the Installation
       ```sh
       sudo docker run hello-world

    **Note: Arch Linux Users can install Docker with `sudo pacman -S docker` or any AUR helper then further start the daemon with `sudo systemctl start docker docker.socket` if not started automatically.**

  - **Windows**
    - Refer to the documentation **[Here](https://docs.docker.com/desktop/setup/install/windows-install/)** for step by step guide to install docker engine and docker desktop on your system.
    
**Step 2**: Clone the Repository
  1. ```sh
     git clone https://github.com/adamofarch/nextbige_assignment.git
     cd nextbige_assignment/

**Step 3**: Start the Containers
  1. ```sh
     docker-compose up --build
  Note: `You can find the container details, environment variables for the postgresql in the docker-compose.yml`
     
**Step 4**: Access the application
  - You can test the application either with Postman or just CURL requests at `http://localhost:8000/api/<endpoint>`

## Method 2: Local Environment 

**Step 1**: Make sure you have Python 3.x installed on your system

**Step 2**: Setup Postgresql with django Refer to the django docs for detailed instructions **[Here](https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-notes)**

**Step 3**: Clone the Repository
  - ```sh
     git clone https://github.com/adamofarch/nextbige_assignment.git
     cd nextbige_assignment/
  
**Step 4**: Setup a Virtual Environment
  - ```sh
     python -m venv venv

**Step 5**: Activate the Virtual Environment
  - Linux and Mac:
    ```sh
    source venv/bin/activate
  - Windows:
    ```sh
    .\venv\Scripts\activate

**Step 6**: Install the required Dependencies
  - ```sh
     pip install -r requirements.txt

**Step 7**: Configure the django settings for the local environment
  - Look for the following options and replace them with static values, e.g. `DEBUG=True` or create a `.env` file in the root directory of the project and reference all of these variables from that file to avoid encountering any errors 
    ```text
    DEBUG = os.getenv('DEBUG')
    
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('DATABASE_HOST'),
            'PORT': os.getenv('DATABASE_PORT'),
        }
    }

       
**Step 8**: Migrate the changes to the new database
  - ```sh
    python manage.py migrate

**Step 9**: Run the development server
  - ```sh
    python manage.py runserver

# Usage and Testing

## Endpoints 

1. `/api/register/` -- As expected of the endpoint it expects form-data sent with the POST request and registers the user and save the details on the database. Also one important thing to note here is, field `date_of_birth` is formatted as YYYY-MM-DD so do keep in mind while sending a dob field data to the api, so it correctly registers it.

2. `/api/login/` -- This endpoint as expected of it, logs in the user through the django's default SessionAuthentication using the form-data(username and password) provided in the request, and as it is also a POST request this endpoint is also CSRF validated. To test this endpoint(using Postman) one would need to set the content type request headers to application/json or application/x-www-form-urlencoded and provide the valid username and password in body of the request. 

3. `/api/profile` -- This endpoint is protected with JWT Authentication and requires user's AuthToken to authenticate, which is generated automatically upon registering and can be obtained with hitting a login request to the application. You can also find the AuthToken in the database, Log into the admin panel to find it manually. To access this endpoint one would need to mention Authorization header in the request headers with the `Token <your_token>` as it's value, and not to forget, it is a GET request only endpoint as per the requirement.

## Testing Using Pytest 

This application includes pytest testcases to verify the functionality of the endpoints listed above. Refer to the code for the detailed insight about the testcases I've written in the directory `/api/tests/` 
- You can use the command `pytest` inside the container's interactive shell to run the testcases and check the results for the testcases

# Additional Takeaways/Notes

1. The `last_login_ip` field is left editable in order to let it show up in the Admin Panel, but it is not recommended to insert any values into it if creating a user manually through the Django admin panel as it will be replaced by the ip address captured by the `IPAddressMiddleware` at the login after the request life cycle is completed. And the field will be updated and an Ip address will be there next time you hit a login endpoint. 

2. The `phone_number` field implemented uses a django's builtin validator to ensure seamless validation of the phone number entered by the user as input which meets all the conditions of being an Indian originated phone number.

3. `Pytest-django` package is used to write tests which is basically pytest but for better integration with django, you can find all the tests in `tests/` directory inside the app `api/` which is also mentioned in the 

4. After starting the containers, Please run `python manage.py migrate` if there are any migrations available before running the server and create a superuser to access django admin panel. 





