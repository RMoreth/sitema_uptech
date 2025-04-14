-- Criação da tabela de usuários (com senha hash)
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    login TEXT UNIQUE NOT NULL,
    senha_hash BLOB NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('admin', 'atendente', 'tecnico'))
);

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT
);

-- Tabela de equipamentos dos clientes
CREATE TABLE IF NOT EXISTS equipamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    marca TEXT,
    modelo TEXT,
    observacoes TEXT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

-- Tabela de ordens de serviço
CREATE TABLE IF NOT EXISTS ordem_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    equipamento_id INTEGER NOT NULL,
    data_entrada TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pendente', 'em andamento', 'concluída')),
    descricao_problema TEXT,
    solucao TEXT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (equipamento_id) REFERENCES equipamento(id)
);
