-- Criação da tabela de usuários (com senha hash)
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    login TEXT UNIQUE NOT NULL,
    senha_hash BLOB NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('admin', 'atendente', 'tecnico'))
);
-- Tabela de endereços
CREATE TABLE IF NOT EXISTS endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cep TEXT,
    estado TEXT,
    cidade TEXT,
    bairro TEXT,
    rua TEXT,
    numero TEXT,
);

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    cpf TEXT,
    endereco_id INTEGER,
    FOREIGN KEY (endereco_id) REFERENCES endereco(id)
);

-- Tabela de equipamentos dos clientes
CREATE TABLE IF NOT EXISTS equipamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    marca TEXT,
    modelo TEXT,
    identificador TEXT,
    acessorios TEXT,
    detalhes TEXT,
    condicoes TEXT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

-- Tabela de ordens de serviço

CREATE TABLE if NOT EXISTS ordens_de_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    telefone_cliente TEXT NOT NULL,
    marca_aparelho TEXT NOT NULL,
    modelo_aparelho TEXT NOT NULL,
    descricao_problema TEXT,
    diagnostico TEXT NOT NULL,
    valor_servico REAL NOT NULL,
    valor_pecas REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pendente', 'em andamento', 'concluída')),
    data_criacao TEXT NOT NULL,
    data_finalizacao TEXT,
    observacoes TEXT
);

