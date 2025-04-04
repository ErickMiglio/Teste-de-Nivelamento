--Junta as tabelas demosntrações e operadoras usando(operadoras.registro_ans=demonstracoes.reg_ans).
--Filtras os registros cuja descrição seja exatamente "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
--Limita os registros aos que tiverem a data nos últimos 3 meses.
--Agrupa os resultados pelo nome fantasia da operadora e soma os valores da coluna vl_saldo_final.
--Ordena os resultados pela soma total decrescente e exibe apenas os 10 primeiras linhas.

SELECT 
    o.nome_fantasia
    ,SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes d
JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE 
    upper(d.descricao) like 'EVENTOS%HOSPITALAR%'
	and d.data >= '2024-10-01'
GROUP BY 
    o.nome_fantasia
ORDER BY 
    total_despesa DESC
LIMIT 10;

--A estrutura desta query é a mesma, mas com a diferença no filtro de data, que agora abrange os últimos 12 meses

SELECT 
    o.nome_fantasia
    ,SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes d
JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE 
    upper(d.descricao) like 'EVENTOS%HOSPITALAR%'
	and d.data >= '2024-01-01'
GROUP BY 
    o.nome_fantasia
ORDER BY 
    total_despesa DESC
LIMIT 10;


