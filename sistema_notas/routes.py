from flask import render_template, flash, url_for, redirect
from sistema_notas import app, database
from sistema_notas.forms import FormCriarAluno, FormNotas, FormPesquisarAluno
from sistema_notas.models import Aluno, Notas


@app.route('/', methods=['GET', 'POST'])
def home():
    form_criar_aluno = FormCriarAluno()

    if form_criar_aluno.validate_on_submit():
        aluno = Aluno(nome=form_criar_aluno.nome.data, sobrenome=form_criar_aluno.sobrenome.data)
        database.session.add(aluno)
        database.session.commit()
        flash('Aluno Cadastrado com Sucesso.', 'alert-success')
        return redirect(url_for('home'))
    return render_template('home.html', form_criar_aluno=form_criar_aluno)


@app.route('/cadastro_notas', methods=['GET', 'POST'])
def cadastro_notas():
    form_notas = FormNotas()

    if form_notas.validate_on_submit():
        nome = Aluno.query.filter_by(nome=form_notas.nome_aluno.data).first()
        sobrenome = Aluno.query.filter_by(sobrenome=form_notas.sobrenome_aluno.data).first()
        nota = Notas(nome=form_notas.nome_aluno.data, sobrenome=form_notas.sobrenome_aluno.data, nota1=form_notas.nota1.data, nota2=form_notas.nota2.data, nota3=form_notas.nota3.data, nota4=form_notas.nota4.data)
        if nome and sobrenome:
            database.session.add(nota)
            database.session.commit()
            flash('Notas Cadastradas com Sucesso', 'alert-success')
            return redirect(url_for('cadastro_notas'))
        else:
            flash('Aluno não cadastrado. Por favor cadastre o novo aluno.', 'alert-danger')
            return redirect(url_for('home'))
    return render_template('cadastro_notas.html', form_notas=form_notas)


@app.route('/nota_aluno', methods=['GET', 'POST'])
def nota_aluno():
    form_pesquisa = FormPesquisarAluno()
    nota = Notas.query.order_by(Notas.nome).all()
    nome = Notas.query
    sobrenome = Notas.query
    if form_pesquisa.validate_on_submit():
        nome = nome.filter(Notas.nome.like(form_pesquisa.nome_aluno.data))
        sobrenome = sobrenome.filter(Notas.sobrenome.like(form_pesquisa.sobrenome_aluno.data))

    nome = nome.order_by(Notas.nome).all()
    sobrenome = sobrenome.order_by(Notas.sobrenome).all()

    return render_template('nota_aluno.html', nota=nota, form_pesquisa=form_pesquisa, nome=nome, sobrenome=sobrenome)


@app.route('/notas')
def notas():
    nota = Notas.query.order_by(Notas.nome).all()
    return render_template('notas.html', nota=nota)
