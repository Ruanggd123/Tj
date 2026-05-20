# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
"""
Script de Download de Provas FCC - TJ-CE 2026
Autor: Calendario de Estudos Antigravity

Baixa todas as provas disponíveis da banca FCC para Analista de TI
e salva na pasta 04_Provas_Anteriores.

Como usar:
  python download_provas_fcc.py
"""

import requests
import os
import sys

BASE_FOLDER = r"c:\Users\Ruan Gomes\Downloads\TJC"
PROVAS_FOLDER = os.path.join(BASE_FOLDER, "04_Provas_Anteriores")
GABARITOS_FOLDER = os.path.join(BASE_FOLDER, "04_Provas_Anteriores", "Gabaritos")

for folder in [PROVAS_FOLDER, GABARITOS_FOLDER]:
    os.makedirs(folder, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream,*/*",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Referer": "https://www.pciconcursos.com.br/",
}

# ============================================================
# LISTA DE PROVAS DA FCC - ANALISTA TI / CARGOS CORRELATOS
# Fontes: PCI Concursos, FCC, questões2.net, www.tribunaisdefcc.com.br
# ============================================================
PROVAS = [
    # --- JA BAIXADAS (semana passada) ---
    {
        "nome": "TRT11_2017_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/25807168/512fb6ef324b/analista_jud_apoio_esp_tecnologia_da_informacao.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT11_2017_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/25807168/e6b67ad8aff6/gabarito.pdf",
        "destino": GABARITOS_FOLDER,
    },
    {
        "nome": "TRT14_2016_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/24224855/03df429a37b5/prova_c03_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT14_2016_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/24224855/aab04b875038/gabarito.pdf",
        "destino": GABARITOS_FOLDER,
    },
    {
        "nome": "TRT23_2016_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/24150123/dd752d4708b2/prova_h08_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT24_2017_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/25868628/64b37eb99bc6/analista_judiciario_tecnologia_da_informacao.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT24_2017_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/25868628/3438fc499b5a/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },

    # --- NOVAS PROVAS COLETADAS ---
    # TRT 15 (FCC 2015)
    {
        "nome": "TRT15_2015_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/22293885/060222a6ead/analista_judiciario_tecnologia_da_informacao.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT15_2015_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/22293885/5deebcf6276/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 9 (FCC 2015)
    {
        "nome": "TRT9_2015_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/23621286/862543ce36d7/prova_d04_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT9_2015_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/23621286/cf69fc78dcb0/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 3 (FCC 2015)
    {
        "nome": "TRT3_2015_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/22775455/87e52b62b262/prova_a28_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT3_2015_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/22775455/4f2bcee6e7c1/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 6 (FCC 2012)
    {
        "nome": "TRT6_2012_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/17725104/9b6596ba2555/prova_t20_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT6_2012_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/17725104/a32f787f214c/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 4 (FCC 2011)
    {
        "nome": "TRT4_2011_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/15626195/0e2599f4afa7/prova_at_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT4_2011_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/15626195/96dce7e95075/gabaritos.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 7 (FCC 2009)
    {
        "nome": "TRT7_2009_Analista_TI",
        "url": "https://www.pciconcursos.com.br/provas/12839532/cfb7e67c81c/prova_g_tipo_001.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT7_2009_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/12839532/c26f29cca40/gabaritos_trt7.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 22 (FCC 2004) - Analista de Sistemas
    {
        "nome": "TRT22_2004_Analista_Sistemas",
        "url": "https://www.pciconcursos.com.br/provas/10032967/91c333cf2aa/prova.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT22_2004_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/10032967/b3b2df9745f0/gabarito.pdf",
        "destino": GABARITOS_FOLDER,
    },
    # TRT 2 (FCC 2006) - Analise de Sistemas
    {
        "nome": "TRT2_2006_Analista_Sistemas",
        "url": "https://www.pciconcursos.com.br/provas/12440869/9f20a4e4f6fc/prova_trt_sp_d01_analise_sistesmas_tipo1_20060620.pdf",
        "destino": PROVAS_FOLDER,
    },
    {
        "nome": "TRT2_2006_Gabarito",
        "url": "https://www.pciconcursos.com.br/provas/12440869/9368c63f1748/gab_trt_sp_d01_analise_sistesmas_tipo1_20060620.pdf",
        "destino": GABARITOS_FOLDER,
    },
]




# ============================================================
def download_file(url, destination, nome):
    if os.path.exists(destination):
        print(f"  [SKIP] Já existe: {nome}")
        return True

    try:
        print(f"  [↓] Baixando: {nome}...")
        r = requests.get(url, headers=HEADERS, stream=True, timeout=30, allow_redirects=True)

        content_type = r.headers.get("Content-Type", "")
        if r.status_code != 200:
            print(f"  [ERRO {r.status_code}] {nome}")
            return False
        if "pdf" not in content_type and "octet-stream" not in content_type and "binary" not in content_type:
            print(f"  [AVISO] Conteúdo inesperado ({content_type}) para: {nome}")
            return False

        with open(destination, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        size_kb = os.path.getsize(destination) // 1024
        if size_kb < 50:
            os.remove(destination)
            print(f"  [ERRO] Arquivo muito pequeno (provavelmente erro ou CAPTCHA): {nome}")
            return False

        print(f"  [OK] Salvo! ({size_kb} KB) -> {destination}")
        return True

    except Exception as e:
        print(f"  [EXCEÇÃO] {nome}: {e}")
        return False

# ============================================================
def main():
    print("=" * 60)
    print("  DOWNLOAD DE PROVAS FCC - ANALISTA TI (TJ-CE 2026)")
    print("=" * 60)
    print(f"  Pasta destino: {PROVAS_FOLDER}\n")

    ok = 0
    fail = 0
    for prova in PROVAS:
        nome = prova["nome"]
        url = prova["url"]
        pasta = prova.get("destino", PROVAS_FOLDER)
        destino = os.path.join(pasta, f"{nome}.pdf")
        resultado = download_file(url, destino, nome)
        if resultado:
            ok += 1
        else:
            fail += 1

    print("\n" + "=" * 60)
    print(f"  CONCLUÍDO: {ok} baixadas | {fail} falhas")
    print("=" * 60)

    if fail > 0:
        print("\n[ATENCAO] Alguns downloads falharam.")
        print("   Isso e normal pois sites de concurso usam protecao anti-robo.")
        print("   Para essas provas, baixe manualmente nos links abaixo:\n")
        print("   [DOWNLOAD] PCI Concursos (FCC + TI):")
        print("      https://www.pciconcursos.com.br/provas/fcc/")
        print("   [DOWNLOAD] Qconcursos (banca FCC, cargo Analista TI):")
        print("      https://www.qconcursos.com.br/questoes-de-concursos/filtro?banca=fcc&cargo=analista+de+tecnologia+da+informacao")
        print("   [DOWNLOAD] Tec Concursos:")
        print("      https://www.tecconcursos.com.br/questoes/cadernos")

if __name__ == "__main__":
    main()
