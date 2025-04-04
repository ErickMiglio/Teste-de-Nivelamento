-- Importa os dados do CSV das operadoras
COPY operadoras(
    registro_ans,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    regiao_de_comercializacao,
    data_registro_ans
)
FROM 'D:/Programador/Teste de Nivelamento/codigo/relatorio_cadop.csv' DELIMITER ';' CSV HEADER;

-- Importa os dados das demonstrações contábeis
-- Importa 1T2024.csv
COPY demonstracoes(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'D:/Programador/Teste de Nivelamento/codigo/1T2024.csv'
DELIMITER ';'
CSV HEADER;

-- Importa 2T2024.csv
COPY demonstracoes(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'D:/Programador/Teste de Nivelamento/codigo/2T2024.csv'
DELIMITER ';'
CSV HEADER;

-- Importa 3T2024.csv
COPY demonstracoes(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'D:/Programador/Teste de Nivelamento/codigo/3T2024.csv'
DELIMITER ';'
CSV HEADER;

-- Importa 4T2024.csv
COPY demonstracoes(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'D:/Programador/Teste de Nivelamento/codigo/4T2024.csv'
DELIMITER ';'
CSV HEADER;