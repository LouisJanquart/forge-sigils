"""Fabrique index.html à partir de la page de travail (artefact Claude, sans squelette)."""
import sys
src = open(sys.argv[1]).read()
title_end = src.index("</title>") + len("</title>")
head, rest = src[:title_end], src[title_end:]
corps_start = rest.index('<div class="app">')
dans_head, corps = rest[:corps_start], rest[corps_start:]
dans_head = dans_head.replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
open("index.html", "w").write(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Générateur de motifs cybersigilism : des lignes, des branches, puis une contraction qui les change en lames chromées.">
{head}
{dans_head}
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}} body{{margin:0}} [hidden]{{display:none!important}}</style>
</head>
<body>
{corps}
</body>
</html>
''')
