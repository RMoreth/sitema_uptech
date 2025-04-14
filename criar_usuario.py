import sqlite3
import bcrypt  # Importando bcrypt

# Caminho do banco de dados
DB_PATH = "banco.db"


def hash_senha(senha):
    # Gera o salt e cria o hash da senha usando bcrypt
    salt = bcrypt.gensalt()
    senha_hashed = bcrypt.hashpw(senha.encode(), salt)
    return senha_hashed


def criar_usuario(nome, login, senha, tipo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    senha_hashed = hash_senha(senha)  # Usando bcrypt para gerar o hash

    try:
        cursor.execute("""
            INSERT INTO usuario (nome, login, senha_hash, tipo)
            VALUES (?, ?, ?, ?)
        """, (nome, login, senha_hashed, tipo))
        conn.commit()
        print("✅ Usuário criado com sucesso!")
    except sqlite3.IntegrityError:
        print("❌ Já existe um usuário com esse login.")
    finally:
        conn.close()


# 👉 Altere esses dados como quiser
if __name__ == "__main__":
    nome = "Administrador"
    login = "admin"
    senha = "admin123"
    tipo = "admin"  # pode ser 'admin', 'atendente' ou 'tecnico'

    criar_usuario(nome, login, senha, tipo)
