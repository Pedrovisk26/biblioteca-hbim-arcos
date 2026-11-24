"""Acrescenta o vídeo de referência aos pacotes IFC da v0.2.0 (uso único)."""
import hashlib, json, sys, zipfile, os

origem, videos, saida = sys.argv[1:4]
IDS = ["HBIM-JAN-0004", "HBIM-JAN-0010", "HBIM-JAN-0011", "HBIM-JAN-0012", "HBIM-JAN-0013"]
h = lambda b: hashlib.sha256(b).hexdigest()
os.makedirs(saida, exist_ok=True)

for i in IDS:
    nome_zip = f"{i}_hbim_v0.2.0.zip"
    video_rel = f"video/{i}_referencia-sem-audio_h264_v0.2.0.mp4"
    with zipfile.ZipFile(os.path.join(origem, nome_zip)) as zi:
        infos = zi.infolist()
        arq = {x.filename: zi.read(x) for x in infos}
    p = f"{i}/"
    assert not any("video/" in n for n in arq), i
    vid = open(os.path.join(videos, os.path.basename(video_rel)), "rb").read()

    # Ficha
    ficha = arq[p + "README.md"].decode()
    marca = "[Baixar o pacote v0.2.0]"
    assert ficha.count(marca) == 1, i
    bloco = (
        "## Vídeo de referência\n\n"
        f"- Arquivo `{video_rel}`.\n"
        "- Registro visual do levantamento, sem áudio e sem metadados de captura, "
        "convertido para H.264 vertical em 608 × 1080 pixels.\n\n"
    )
    arq[p + "README.md"] = ficha.replace(marca, bloco + marca).encode()

    # Metadados
    raw = arq[p + "metadados.json"]
    m = json.loads(raw)
    m["componentes_disponiveis"].append({
        "componente": "referencia-visual", "formato": "MP4", "arquivo": video_rel,
        "codec": "H.264", "resolucao": "608 × 1080", "audio": False,
        "compatibilidade_por_arquivo": None,
    })
    aus = [a for a in m["componentes_ausentes"] if a["formato"] == "OBJ e MP4"]
    assert len(aus) == 1, i
    aus[0]["formato"] = "OBJ"
    arq[p + "metadados.json"] = (json.dumps(m, ensure_ascii=False, indent=2)
                                 + ("\n" if raw.endswith(b"\n") else "")).encode()

    arq[p + video_rel] = vid

    # Inventário interno
    raw = arq[p + "inventario.json"]
    inv = json.loads(raw)
    inv["arquivos"].append({
        "caminho": video_rel, "funcao": "referencia-visual", "componente": None,
        "formato": "MP4", "software": None, "unidades": None,
        "tamanho_bytes": 0, "sha256": "", "dependencias": [], "licenca": "CC-BY-4.0",
    })
    for a in inv["arquivos"]:
        b = arq[p + a["caminho"]]
        a["sha256"], a["tamanho_bytes"] = h(b), len(b)
    arq[p + "inventario.json"] = (json.dumps(inv, ensure_ascii=False, indent=2)
                                  + ("\n" if raw.endswith(b"\n") else "")).encode()

    # Checksums internos
    sums = arq[p + "SHA256SUMS.txt"].decode()
    nomes = [l.split("  ", 1)[1] for l in sums.splitlines()] + [video_rel]
    arq[p + "SHA256SUMS.txt"] = "".join(f"{h(arq[p + n])}  {n}\n" for n in sorted(nomes)).encode()

    destino = os.path.join(saida, nome_zip)
    with zipfile.ZipFile(destino, "w") as zo:
        ordem = [x for x in infos] + [None]
        for x in ordem:
            nome = x.filename if x else p + video_rel
            dt = x.date_time if x else infos[0].date_time
            ni = zipfile.ZipInfo(nome, date_time=dt)
            ni.external_attr = infos[0].external_attr
            if nome.endswith(".mp4"):
                ni.compress_type = zipfile.ZIP_STORED
                zo.writestr(ni, arq[nome])
            else:
                ni.compress_type = zipfile.ZIP_DEFLATED
                zo.writestr(ni, arq[nome], compresslevel=9)
    with zipfile.ZipFile(destino) as zt:
        assert zt.testzip() is None
        s = zt.read(p + "SHA256SUMS.txt").decode()
        for l in s.splitlines():
            hh, n = l.split("  ", 1)
            assert h(zt.read(p + n)) == hh, (i, n)
    print(f"{h(open(destino, 'rb').read())}  {nome_zip}  {os.path.getsize(destino)}")
