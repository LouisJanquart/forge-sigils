# Forge à sigils

Générateur de motifs cybersigilism, en une seule page (HTML + JS, sans build).

1. **Lignes** : des lignes de base au hasard, ou dessinées / importées en SVG.
2. **Branches** : sur chaque ligne poussent des branches, sur chaque branche des sous-branches.
3. **Forme** : les lignes sont épaissies et posées sur une grille, puis chaque point de la grille glisse vers la moyenne de ses voisins, des centaines de fois (lissage de Laplace). Les bords fondent, l'intérieur tient : les bouts deviennent des pointes, les croisements restent palmés.
4. **Rendu** : chrome biseauté (hauteur = distance au bord), encre ou blanc sur noir ; vue 3D (three.js) ; export SVG à coller dans Figma.

Méthode inspirée du générateur Blender à nodes de The Well Tarot (« Create the most lethal Cyber Sigil Generator with nodes! »).

Hébergé sur Netlify : https://forge-sigils.netlify.app
