CREATE DATABASE teleconsulta;
USE teleconsulta;

CREATE TABLE usuario (
    id CHAR(36) PRIMARY KEY,
    nome_completo VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    role ENUM('ADMIN','MEDICO','PACIENTE') NOT NULL,
    status ENUM('PENDENTE','ATIVO','BLOQUEADO','REJEITADO') NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE medico (
    id CHAR(36) PRIMARY KEY,
    crm VARCHAR(20) NOT NULL UNIQUE,
    especialidade VARCHAR(100) NOT NULL,

    CONSTRAINT fk_medico_usuario
        FOREIGN KEY (id) REFERENCES usuario(id)
        ON DELETE CASCADE
);

CREATE TABLE paciente (
    id CHAR(36) PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,

    CONSTRAINT fk_paciente_usuario
        FOREIGN KEY (id) REFERENCES usuario(id)
        ON DELETE CASCADE
);

CREATE TABLE admin (
    id CHAR(36) PRIMARY KEY,

    CONSTRAINT fk_admin_usuario
        FOREIGN KEY (id) REFERENCES usuario(id)
        ON DELETE CASCADE
);

CREATE TABLE horario (
    id CHAR(36) PRIMARY KEY,
    medico_id CHAR(36) NOT NULL,
    data_hora_inicio DATETIME NOT NULL,
    data_hora_fim DATETIME NOT NULL,
    disponivel BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_horario_medico
        FOREIGN KEY (medico_id) REFERENCES medico(id)
        ON DELETE CASCADE
);

CREATE TABLE consulta (
    id CHAR(36) PRIMARY KEY,
    medico_id CHAR(36) NOT NULL,
    paciente_id CHAR(36) NOT NULL,
    horario_id CHAR(36) UNIQUE,
    
    status ENUM(
        'DISPONIVEL',
        'RESERVADA',
        'AGUARDANDO_PAGAMENTO',
        'CONFIRMADA',
        'CANCELADA',
        'FINALIZADA'
    ) NOT NULL,

    data_hora_inicio DATETIME NOT NULL,
    data_hora_fim DATETIME NOT NULL,
    link_video VARCHAR(255),
    codigo_acesso VARCHAR(100),

    CONSTRAINT fk_consulta_medico
        FOREIGN KEY (medico_id) REFERENCES medico(id),

    CONSTRAINT fk_consulta_paciente
        FOREIGN KEY (paciente_id) REFERENCES paciente(id),

    CONSTRAINT fk_consulta_horario
        FOREIGN KEY (horario_id) REFERENCES horario(id)
);

CREATE TABLE pagamento (
    id CHAR(36) PRIMARY KEY,
    consulta_id CHAR(36) UNIQUE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,

    status ENUM('PENDENTE','APROVADO','RECUSADO','ESTORNADO') NOT NULL,

    data_pagamento DATETIME,
    gateway VARCHAR(100),

    CONSTRAINT fk_pagamento_consulta
        FOREIGN KEY (consulta_id) REFERENCES consulta(id)
        ON DELETE CASCADE
);

CREATE TABLE notificacao (
    id CHAR(36) PRIMARY KEY,
    consulta_id CHAR(36) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio DATETIME NOT NULL,

    CONSTRAINT fk_notificacao_consulta
        FOREIGN KEY (consulta_id) REFERENCES consulta(id)
        ON DELETE CASCADE
);

CREATE TABLE log_auditoria (
    id CHAR(36) PRIMARY KEY,
    usuario_id CHAR(36) NOT NULL,
    acao VARCHAR(255) NOT NULL,
    data_hora DATETIME NOT NULL,
    ip VARCHAR(45),

    CONSTRAINT fk_log_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        ON DELETE CASCADE
);

CREATE TABLE token_jwt (
    usuario_id CHAR(36) PRIMARY KEY,
    token TEXT NOT NULL,
    data_expiracao DATETIME NOT NULL,

    CONSTRAINT fk_token_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        ON DELETE CASCADE
);