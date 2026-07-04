await page.goto('https://4devtool.com/br/validar-inscricao-estadual/')
await page.fill('#inscricaoEstadual', '110.042.490.114')
await page.fill('#uf', 'SP')
await page.click('button:has-text("Validar")')
