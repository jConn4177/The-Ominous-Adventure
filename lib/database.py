# database.py

from peewee import *

database = SqliteDatabase('game.db')

class BaseModel(Model):
    class Meta:
        database = database

class Players(BaseModel):
    player_id = AutoField(primary_key=True)
    player_name = CharField(null=False)
    scene_id = IntegerField(null=True)

class Scene(BaseModel):
    scene_id = AutoField(primary_key=True)
    scene_name = CharField(null=False)
    scene_description = TextField(null=True)

class Option(BaseModel):
    option_id = AutoField(primary_key=True)
    scene_id = ForeignKeyField(Scene, backref='options')
    next_scene_id = ForeignKeyField(Scene, backref='previous_options', null=True)
    option_description = TextField(null=False)

class Prophecy(BaseModel):
    prophecy_id = AutoField(primary_key=True)
    prophecy_name = CharField(null=True)
    prophecy_description = TextField(null=True)

# Connect the models to the database
def initialize_database():
    with database:
        database.create_tables([Players, Scene, Option, Prophecy])