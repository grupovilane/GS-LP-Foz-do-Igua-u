"""
Troca uma imagem da landing page, já recortando e comprimindo no mesmo
padrão das outras.

Uso:
    python trocar-imagem.py "C:\\caminho\\da\\foto.jpg"            -> vira a hero
    python trocar-imagem.py "C:\\caminho\\da\\foto.jpg" dia3       -> vira a dia3

Nomes aceitos: hero, banner, dia1..dia6, hotel1..hotel4, insta1..insta9
"""
import os
import sys

from PIL import Image, ImageOps

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

TAMANHOS = {
    "hero": (1200, 880),
    "banner": (1920, 1100),
    **{f"dia{i}": (1200, 880) for i in range(1, 7)},
    **{f"hotel{i}": (760, 520) for i in range(1, 5)},
    **{f"insta{i}": (760, 760) for i in range(1, 10)},
}


# largura da versão leve por família de imagem (usada no srcset do index.html)
LARGURA_SM = {"banner": 900, "dia": 900, "hotel": 420, "insta": 400}


def familia(nome):
    if nome == "banner":
        return "banner"
    for f in ("dia", "hotel", "insta"):
        if nome.startswith(f):
            return f
    return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    origem = sys.argv[1].strip('"')
    destino = (sys.argv[2] if len(sys.argv) > 2 else "hero").lower().removesuffix(".jpg")

    if not os.path.isfile(origem):
        print(f"Não encontrei o arquivo: {origem}")
        return 1
    if destino not in TAMANHOS:
        print(f"Nome inválido: {destino}. Use um destes: {', '.join(TAMANHOS)}")
        return 1

    caixa = TAMANHOS[destino]
    saida = os.path.join(ASSETS, destino + ".jpg")

    imagem = ImageOps.exif_transpose(Image.open(origem)).convert("RGB")
    grande = ImageOps.fit(imagem, caixa, Image.LANCZOS, centering=(0.5, 0.45))
    grande.save(saida, "JPEG", quality=80, optimize=True, progressive=True)
    print(f"OK: {destino}.jpg ({caixa[0]}x{caixa[1]}, "
          f"{os.path.getsize(saida) // 1024} KB)")

    # variante leve, servida a celular e tablet via srcset
    largura_sm = LARGURA_SM.get(familia(destino))
    if largura_sm and caixa[0] > largura_sm + 40:
        saida_sm = os.path.join(ASSETS, destino + "-sm.jpg")
        altura_sm = round(caixa[1] * largura_sm / caixa[0])
        grande.resize((largura_sm, altura_sm), Image.LANCZOS).save(
            saida_sm, "JPEG", quality=78, optimize=True, progressive=True
        )
        print(f"OK: {destino}-sm.jpg ({largura_sm}x{altura_sm}, "
              f"{os.path.getsize(saida_sm) // 1024} KB)")

    print("Recarregue a página com Ctrl+F5 para ver.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
