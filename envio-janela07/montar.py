"""Monta HBIM-JAN-0007_hbim_v0.2.0.zip (uso único)."""
import hashlib, json, os, sys, zipfile
base, video, destino = sys.argv[1:4]
p = "HBIM-JAN-0007/"
vrel = "video/HBIM-JAN-0007_referencia-sem-audio_h264_v0.2.0.mp4"
h = lambda b: hashlib.sha256(b).hexdigest()
arq = {}
for raiz, _, nomes in os.walk(os.path.join(base, "HBIM-JAN-0007")):
    for n in nomes:
        c = os.path.join(raiz, n)
        arq[os.path.relpath(c, base).replace(os.sep, "/")] = open(c, "rb").read()
arq[p + vrel] = open(video, "rb").read()
inv = json.loads(arq[p + "inventario.json"])
for a in inv["arquivos"]:
    b = arq[p + a["caminho"]]; a["sha256"], a["tamanho_bytes"] = h(b), len(b)
arq[p + "inventario.json"] = (json.dumps(inv, ensure_ascii=False, indent=2) + "\n").encode()
nomes = [l.split("  ", 1)[1] for l in arq[p + "SHA256SUMS.txt"].decode().splitlines()]
assert sorted(nomes) == sorted(n[len(p):] for n in arq if not n.endswith("SHA256SUMS.txt")), nomes
arq[p + "SHA256SUMS.txt"] = "".join(f"{h(arq[p + n])}  {n}\n" for n in sorted(nomes)).encode()
ordem = ["CITATION.cff", "LICENSE.md", "README.md", "SHA256SUMS.txt",
         "ifc/HBIM-JAN-0007_janela-hbim_v0.2.0.ifc", "inventario.json", "metadados.json", vrel]
assert sorted(p + o for o in ordem) == sorted(arq)
with zipfile.ZipFile(destino, "w") as zo:
    for o in ordem:
        zi = zipfile.ZipInfo(p + o, date_time=(2026, 11, 24, 12, 0, 0))
        zi.external_attr = 0o644 << 16
        zi.compress_type = zipfile.ZIP_STORED if o.endswith(".mp4") else zipfile.ZIP_DEFLATED
        zo.writestr(zi, arq[p + o], compresslevel=None if o.endswith(".mp4") else 9)
with zipfile.ZipFile(destino) as zt:
    assert zt.testzip() is None
    for l in zt.read(p + "SHA256SUMS.txt").decode().splitlines():
        hh, n = l.split("  ", 1); assert h(zt.read(p + n)) == hh, n
print(f"{h(open(destino, 'rb').read())}  {os.path.basename(destino)}  {os.path.getsize(destino)}")
