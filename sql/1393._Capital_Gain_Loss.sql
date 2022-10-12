SELECT gl.stock_name, (sell_col - buy_col) AS capital_gain_loss
FROM (
SELECT stock_name
    , SUM(CASE WHEN operation = 'Buy' then price else 0 END) AS buy_col
    , SUM(CASE WHEN operation = 'Sell' then price else 0 END) AS sell_col
FROM Stocks AS S
GROUP BY stock_name) AS gl;
