# Create character daily/weekly check boxes for lost ark.
# Log in and enter character name and gear score, generate table for available content.
# Reset dailies at appropriate time as well as weekly.
# Offer check boxes to keep track of each character activities.
# Daily chaos, guardians, uni tasks.
# Weekly abyssal, uni and guild missions.


from app import create_app
from flask_migrate import Migrate
from app.models import db, User, Character

app = create_app('testing')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User, Character = Character) #db, user, post, etc