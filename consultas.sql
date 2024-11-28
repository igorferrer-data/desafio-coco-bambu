-- Consultas SQL para Validação

SHOW TABLES;

SELECT * FROM fato_pedidos;
SELECT * FROM detail_metadata;

SELECT f.guestCheckId, l.nome_loja, f.subTtl, f.chkTtl
FROM fato_pedidos f
JOIN dim_lojas l ON f.store_id = l.store_id;

SELECT d.lineItemId, i.nome_item, d.dspQty, d.aggTtl
FROM detail_lines d
JOIN dim_itens i ON d.guestCheckId = 1122334455

SELECT dm.metadataType, dm.metadataKey, dm.metadataValue
FROM detail_metadata dm
WHERE dm.lineItemId = 1;

