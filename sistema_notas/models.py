from sistema_notas import database, app


class Aluno(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    sobrenome = database.Column(database.String, nullable=False)


class Notas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    sobrenome = database.Column(database.String, nullable=False)
    nota1 = database.Column(database.Float)
    nota2 = database.Column(database.Float)
    nota3 = database.Column(database.Float)
    nota4 = database.Column(database.Float)
