WITH TB_VALOR AS (
SELECT cliente.nome, 
transacao.valor_total, 
ISNULL(transacao.percentual_desconto,0) AS percentual_desconto, 
transacao.valor_total * (1-ISNULL(transacao.percentual_desconto,0)/100) AS valor_com_desconto,
contrato.percentual,
contrato.ativo
FROM desafio_engenheiro.dbo.transacao transacao
LEFT JOIN desafio_engenheiro.dbo.contrato contrato
ON transacao.contrato_id = contrato.contrato_id
LEFT JOIN desafio_engenheiro.dbo.cliente cliente
ON contrato.cliente_id = cliente.cliente_id
)

SELECT nome AS cliente_nome,
ROUND(SUM(valor_com_desconto * percentual/100),2) AS valor
FROM TB_VALOR
WHERE ativo = 1
GROUP BY nome;