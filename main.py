import parser

import command.factory as factory
from db import DBFile

args = parser.create()
db = DBFile("books.txt")
factory.create(args, db).execute()
