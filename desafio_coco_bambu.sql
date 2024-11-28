SELECT d.lineItemId, i.nome_item, d.dspQty, d.aggTtl
FROM detail_lines d
JOIN dim_itens i ON d.guestCheckId = 1122334455
