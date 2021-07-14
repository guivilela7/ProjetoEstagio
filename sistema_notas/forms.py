from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Optional
from sistema_notas.models import Aluno, Notas


class FormCriarAluno(FlaskForm):
    nome = StringField('Nome do Aluno', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome do Aluno', validators=[DataRequired()])
    botao_submit_criar_aluno = SubmitField('Cadastrar Novo Aluno')

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        aluno = Aluno.query.filter_by(nome=self.nome.data, sobrenome=self.sobrenome.data).first()
        if aluno is not None:
            self.nome.errors.append('Aluno já cadastrado')
            return False

        return True


class FormNotas(FlaskForm):
    nome_aluno = StringField('Nome Aluno', validators=[DataRequired()])
    sobrenome_aluno = StringField('Sobrenome Aluno', validators=[DataRequired()])
    nota1 = FloatField('Nota 1', validators=[DataRequired()])
    nota2 = FloatField('Nota 2', validators=[Optional()])
    nota3 = FloatField('Nota 3', validators=[Optional()])
    nota4 = FloatField('Nota 4', validators=[Optional()])
    botao_submit_notas = SubmitField('Enviar Notas')


class FormPesquisarAluno(FlaskForm):
    nome_aluno = StringField('Nome Aluno', validators=[DataRequired()], default='')
    sobrenome_aluno = StringField('Sobrenome Aluno', validators=[Optional()], default='')
    botao_submit_pesquisa = SubmitField('Pesquisar Aluno')
