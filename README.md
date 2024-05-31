# flask-dynamic-postgres-db
This is a quick toy project to explore programmatically creating postgres databases in Flask using a webform.

## Overview
This simply demonstrates that new postgres databases can be created using a webform in flask.

I have opted to use docker to manage the postgreSQL DBMS. It is a quick and clean way to do this and 
is a lot less cumbersome than running posgres locally on my machine.

Sure! Here is a sample documentation for your Flask application with PostgreSQL running in a Docker container.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.6 or higher.
- Virtual environment (optional but recommended).

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Create a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate 
```

### Step 3: Install Dependencies

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Docker

Ensure your `docker-compose.yml` file is configured correctly:

```yaml
services:
  db:
    image: postgres:14
    container_name: postgres_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: Password123
      POSTGRES_DB: admin_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Step 5: Start Docker Containers

Start the PostgreSQL container:

```bash
docker-compose up -d
```

### Step 6: Run the Flask Application

Run the Flask application:

```bash
python app.py
```

Open your web browser and navigate to `http://localhost:5000/` to access the application.

## Features

### Landing Page

The landing page displays a welcome message and a button to navigate to the database creation page.

### Create Database

On the database creation page, users can input the name of the new database and create it. The application will check if the database already exists and display appropriate messages.

## Scripts

### List All Databases

You can list all databases in the PostgreSQL container using the provided `list_databases.sh` script.

1. **Create the Script:**

   Create a file named `list_databases.sh` with the following content:

   ```bash
   #!/bin/bash

   CONTAINER_NAME="postgres_db"

   echo "Listing all databases in the PostgreSQL container '$CONTAINER_NAME':"
   docker exec -it $CONTAINER_NAME psql -U postgres -c "\l"
   ```

2. **Make the Script Executable:**

   ```bash
   chmod +x list_databases.sh
   ```

3. **Run the Script:**

   ```bash
   ./list_databases.sh
   ```

### Check Specific Database

To check if a specific database exists, you can use the following script `check_db.sh`:

1. **Create the Script:**

   Create a file named `check_db.sh` with the following content:

   ```bash
   #!/bin/bash

   DB_NAME="$1"
   CONTAINER_NAME="postgres_db"

   EXISTS=$(docker exec -it $CONTAINER_NAME psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")

   if [ "$EXISTS" = "1" ]; then
     echo "Database '$DB_NAME' exists."
   else
     echo "Database '$DB_NAME' does not exist."
   fi
   ```

2. **Make the Script Executable:**

   ```bash
   chmod +x check_db.sh
   ```

3. **Run the Script:**

   ```bash
   ./check_db.sh <database_name>
   ```

## Application Structure

- `app.py`: Main application file.
- `forms.py`: Contains the form for database creation.
- `templates/`: Contains HTML templates.
  - `index.html`: Landing page template.
  - `create_db.html`: Database creation page template.
- `list_databases.sh`: Script to list all databases.
- `check_db.sh`: Script to check the existence of a specific database.

## Environment Variables

The Flask application uses environment variables for configuration. Update these variables in your `docker-compose.yml` file:

- `POSTGRES_USER`: PostgreSQL user.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `POSTGRES_DB`: Default database.

## Troubleshooting

### Common Issues

1. **Database Role Does Not Exist:**

   If you encounter an error indicating that the role does not exist, ensure that the role is created within the PostgreSQL container.

   ```bash
   docker exec -it postgres_db psql -U postgres -c "CREATE ROLE your_username WITH LOGIN PASSWORD 'your_password';"
   ```

2. **Connection Issues:**

   Ensure the PostgreSQL container is running and accessible at the specified ports.

   ```bash
   docker-compose ps
   ```

### Logs

To view logs for the PostgreSQL container:

```bash
docker logs postgres_db
```

