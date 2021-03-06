from titanembeds.database import db
import datetime
import time

class AuthenticatedUsers(db.Model):
    __tablename__ = "authenticated_users"
    id = db.Column(db.Integer, primary_key=True)                    # Auto increment id
    guild_id = db.Column(db.String(255), nullable=False)            # Guild pretaining to the authenticated user
    client_id = db.Column(db.String(255), nullable=False)           # Client ID of the authenticated user
    last_timestamp = db.Column(db.TIMESTAMP, nullable=False)        # The timestamp of when the user has last sent the heartbeat

    def __init__(self, guild_id, client_id):
        self.guild_id = guild_id
        self.client_id = client_id
        self.last_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def bumpTimestamp(self):
        self.last_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        db.session.commit()
        return self.last_timestamp
