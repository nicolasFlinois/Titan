from titanembeds.database import db
import json

class GuildMembers(db.Model):
    __tablename__ = "guild_members"
    id = db.Column(db.Integer, primary_key=True)                    # Auto incremented id
    guild_id = db.Column(db.String(255), nullable=False)            # Discord guild id
    user_id = db.Column(db.String(255), nullable=False)             # Discord user id
    username = db.Column(db.String(255), nullable=False)            # Name
    discriminator = db.Column(db.Integer, nullable=False)           # User discriminator
    nickname = db.Column(db.String(255))                            # User nickname
    avatar = db.Column(db.String(255))                              # The avatar str of the user
    active = db.Column(db.Boolean(), nullable=False)                # If the user is a member of the guild
    banned = db.Column(db.Boolean(), nullable=False)                # If the user is banned in the guild
    roles = db.Column(db.Text(), nullable=False)                    # Member roles

    def __init__(self, guild_id, user_id, username, discriminator, nickname, avatar, active, banned, roles):
        self.guild_id = guild_id
        self.user_id = user_id
        self.username = username
        self.discriminator = discriminator
        self.nickname = nickname
        self.avatar = avatar
        self.active = active
        self.banned = banned
        self.roles = roles

    def __repr__(self):
        return '<GuildMembers {0} {1} {2} {3} {4}>'.format(self.id, self.guild_id, self.user_id, self.username, self.discriminator)

def list_all_guild_members(guild_id):
    memlist = []
    members = db.session.query(GuildMembers).filter(GuildMembers.guild_id == guild_id).all()
    for member in members:
        memlist.append({
            "user": {
                "username": member.username,
                "discriminator": member.discriminator,
                "id": member.user_id,
                "avatar": member.avatar
            },
            "roles": json.loads(member.roles),
            "nickname": member.nickname,
        })
    return memlist

def get_guild_member(guild_id, member_id):
    return db.session.query(GuildMembers).filter(GuildMembers.guild_id == guild_id, GuildMembers.user_id == member_id).first()
