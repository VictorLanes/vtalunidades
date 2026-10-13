import pathlib
d = pathlib.Path(__file__).parent / "front"
css = (d / "style.css").read_text()
js = "".join((d / f"app{i}.js").read_text() for i in range(1, 6))
html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b1220">
<meta name="robots" content="noindex, nofollow">
<title>VTAL Unidades</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231e52ed'/%3E%3Cpath d='M9 11h14v10H9z' fill='none' stroke='%23fff' stroke-width='2.2' stroke-linejoin='round'/%3E%3Ccircle cx='16' cy='16' r='2.6' fill='%23fff'/%3E%3C/svg%3E">
<style>
{css}
</style>
</head>
<body>
<div id="app"></div>
<noscript>Ative o JavaScript para usar o sistema.</noscript>
<script>
{js}
</script>
</body>
</html>
"""
(pathlib.Path(__file__).parent / "index.html").write_text(html)
print(len(html))
