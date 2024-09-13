from flask import Flask #cria o API
from flask_sqlalchemy import SQLAlchemy #cria o banco de dados


#Criar um API flask
app = Flask(__name__)
#Criar uma instância de SQL Alchemy
app.config['SECRET_KEY'] = 'noth$ebastian144'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ooarapkgjpggeachcpgv:1Corintio$7@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

db = SQLAlchemy(app)
db:SQLAlchemy
#Definir a estrutura da tabela Postagem
# toda postagem deve conter id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor')) #relacionamento com a tabela
    
# Definir a estrutura da tabela autor
# todo autor deve possuir id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db. String)
    email = db. Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship(Postagem) #relacionamento com a classe

# Executar o comando para criar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()
# Criar usuários administradores
        autor = Autor(nome='jose', email='jose@email.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()
