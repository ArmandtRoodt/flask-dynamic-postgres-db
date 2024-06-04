from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from forms import CreateDatabaseForm

app = Flask(__name__)

# Configure the database URI for the main admin database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost:5432/admin_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_db', methods=['GET', 'POST'])
def create_db():
    form = CreateDatabaseForm()
    if form.validate_on_submit():
        db_name = form.db_name.data
        new_db_uri = f'postgresql://postgres:Password123@localhost:5432/{db_name}'
        engine = create_engine(new_db_uri)

        if not database_exists(engine.url):
            create_database(engine.url)
            flash(f"Database '{db_name}' created successfully!", 'success')
        else:
            flash(f"Database '{db_name}' already exists!", 'warning')
        return redirect(url_for('create_db'))

    return render_template('create_db.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
