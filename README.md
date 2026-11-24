# Biblioteca HBIM de elementos arqueados históricos

Dados e objetos digitais produzidos para a pesquisa **“Modelagem paramétrica e biblioteca de objetos em HBIM como ativo de informação para valorização do patrimônio histórico”** (*Parametric modeling and object libraries in HBIM as information assets for heritage preservation*).

**Autores:** PEDRO LUCAS COUTINHO e RAQUEL RIBEIRO.

## Sobre a pesquisa

O projeto investiga um fluxo de trabalho replicável para documentar, modelar e disponibilizar elementos arqueados de edificações históricas brasileiras. A proposta relaciona fotogrametria, malhas densas e famílias paramétricas no contexto do *Heritage Building Information Modeling* (HBIM), tratando o patrimônio edificado como ativo físico e como ativo de informação.

O recorte inicial reúne janelas e portas de linguagem neoclássica e eclética, com ênfase em arcos plenos, abatidos e semi-elipticos. Os materiais apoiam atividades de documentação, conservação, modelagem e gestão do patrimônio.

Este repositório acompanha um **manuscrito em elaboração** para o 9º Congresso Internacional A ERA BIM – SINAENCO (São Paulo, 24–26 de novembro de 2026). O PDF de trabalho não integra a distribuição pública, pois ainda contém comentários editoriais e seções em revisão. A presença desta referência não significa aceite ou publicação do artigo.

## Conteúdo da versão inicial

| Elemento | Famílias Revit | Versão do Revit | Malha fotogramétrica | Vídeo de referência |
| --- | --- | --- | --- | --- |
| Janela 01 | conjunto, bandeira e folha | 2026/2027 | OBJ | MP4 sem áudio |
| Janela 02 | folha e moldura | 2027 | OBJ | MP4 sem áudio |
| Janela 05 | conjunto | 2027 | OBJ | MP4 sem áudio |
| Janela 06 | conjunto e folha | 2027 | OBJ | MP4 sem áudio |
| Porta 01 | moldura | 2027 | OBJ | MP4 sem áudio |

Os arquivos estão agrupados por elemento na seção [Releases](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases). Cada pacote contém, conforme disponível:

```text
elemento/
├── revit/   # famílias RFA
├── mesh/    # malha densa OBJ
└── video/   # registro visual sanitizado, sem áudio e sem metadados de captura
```

Use o arquivo `SHA256SUMS.txt` da versão para verificar a integridade dos pacotes após o download.

| Pacote da versão 0.1.0 | Tamanho aproximado |
| --- | ---: |
| `Janela_01_HBIM_v0.1.0.zip` | 92 MiB |
| `Janela_02_HBIM_v0.1.0.zip` | 405 MiB |
| `Janela_05_HBIM_v0.1.0.zip` | 378 MiB |
| `Janela_06_HBIM_v0.1.0.zip` | 496 MiB |
| `Porta_01_HBIM_v0.1.0.zip` | 81 MiB |

## Conteúdo da versão 0.2.0

Após o envio do manuscrito ao congresso, um estudo complementar gerou modelos IFC4 de nove janelas. Quatro delas já integravam a versão inicial (Janelas 01, 02, 05 e 06) e cinco são novas na biblioteca (Janelas 04, 10, 11, 12 e 13). Esta versão acrescenta os modelos IFC4 e, para as cinco janelas novas, o vídeo de referência sem áudio. As famílias RFA, as malhas OBJ e os vídeos das Janelas 01, 02, 05 e 06 continuam disponíveis nos pacotes da [versão 0.1.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.1.0).

A reconstrução em sólidos partiu de vistas ortográficas das malhas fotogramétricas em OBJ e da conferência visual de vídeos ou fotogramas do levantamento. O Codex (OpenAI), ferramenta de inteligência artificial generativa, auxiliou na elaboração de scripts em Python. Os scripts usaram a biblioteca IfcOpenShell (versão 0.9.0.post1) para gerar os arquivos IFC4, com materiais de representação atribuídos aos componentes.

Os nove arquivos foram reabertos no IfcOpenShell para conferir o esquema IFC4, a geometria dos sólidos e as associações de materiais. O IFC da Janela 04 também foi aberto no Autodesk Revit 2026, onde foi importado como DirectShape na categoria Janelas.

| Elemento | ID | Arquivos | Vão (largura × altura, m) |
| --- | --- | --- | --- |
| Janela 01 | `HBIM-JAN-0001` | IFC4 | 1,876 × 2,838 |
| Janela 02 | `HBIM-JAN-0002` | IFC4 | 1,296 × 2,690 |
| Janela 04 | `HBIM-JAN-0004` | IFC4 e MP4 sem áudio | 1,180 × 2,698 |
| Janela 05 | `HBIM-JAN-0005` | IFC4 | 1,452 × 3,384 |
| Janela 06 | `HBIM-JAN-0006` | IFC4 | 1,513 × 2,905 |
| Janela 10 | `HBIM-JAN-0010` | IFC4 e MP4 sem áudio | 1,192 × 2,707 |
| Janela 11 | `HBIM-JAN-0011` | IFC4 e MP4 sem áudio | 1,208 × 2,803 |
| Janela 12 | `HBIM-JAN-0012` | IFC4 e MP4 sem áudio | 1,505 × 3,404 |
| Janela 13 | `HBIM-JAN-0013` | IFC4 e MP4 sem áudio | 1,947 × 3,191 |

Cada pacote da versão 0.2.0 contém:

```text
ID-do-elemento/
├── ifc/              # modelo IFC4
├── video/            # vídeo de referência sem áudio (janelas 04, 10, 11, 12 e 13)
├── README.md         # ficha do elemento
├── metadados.json
├── inventario.json   # lista dos arquivos do pacote
├── SHA256SUMS.txt    # checksums dos arquivos do pacote
├── CITATION.cff
└── LICENSE.md
```

| Pacote da versão 0.2.0 | Tamanho aproximado |
| --- | ---: |
| [`HBIM-JAN-0001_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0001_hbim_v0.2.0.zip) | 19 KiB |
| [`HBIM-JAN-0002_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0002_hbim_v0.2.0.zip) | 19 KiB |
| [`HBIM-JAN-0004_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0004_hbim_v0.2.0.zip) | 69 MiB |
| [`HBIM-JAN-0005_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0005_hbim_v0.2.0.zip) | 18 KiB |
| [`HBIM-JAN-0006_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0006_hbim_v0.2.0.zip) | 17 KiB |
| [`HBIM-JAN-0010_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0010_hbim_v0.2.0.zip) | 37 MiB |
| [`HBIM-JAN-0011_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0011_hbim_v0.2.0.zip) | 56 MiB |
| [`HBIM-JAN-0012_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0012_hbim_v0.2.0.zip) | 34 MiB |
| [`HBIM-JAN-0013_hbim_v0.2.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0013_hbim_v0.2.0.zip) | 51 MiB |

## Como usar

1. Baixe o pacote do elemento desejado: famílias RFA, malhas OBJ e vídeos na [versão 0.1.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.1.0); modelos IFC4 na [versão 0.2.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.2.0).
2. Confira o checksum SHA-256.
3. Extraia o pacote mantendo sua estrutura de pastas.
4. Abra os arquivos RFA em uma versão compatível do Autodesk Revit.
5. Importe a malha OBJ apenas em ferramentas que suportem a escala, a densidade e as extensões de cor utilizadas pelo arquivo.
6. Abra o IFC em um visualizador BIM ou vincule-o a um projeto no Autodesk Revit.

Os arquivos RFA não são retrocompatíveis: uma família salva no Revit 2027 não abre diretamente em versões anteriores. Faça uma cópia de trabalho antes de atualizar qualquer família para uma versão mais recente.

## Limitações conhecidas

- As malhas foram geradas no RealityScan 2.2 e são densas; a maior possui aproximadamente 6,9 milhões de vértices e 13,8 milhões de faces.
- Os arquivos OBJ possuem coordenadas de textura e referências a materiais, mas os arquivos MTL e as imagens de textura originais não estão disponíveis na versão 0.1.0. Algumas aplicações conseguem exibir as cores armazenadas junto aos vértices; outras mostrarão apenas a geometria.
- A referência de material interna de `Janela_02.obj` conserva o nome `Janela_01.mtl`, herdado da exportação original. Como nenhum MTL é distribuído, essa referência não deve ser usada para associar materiais.
- Nem todos os elementos possuem uma família RFA principal completa; a tabela acima informa os componentes efetivamente disponíveis.
- Os modelos IFC4 da versão 0.2.0 são reconstruções simplificadas: perfis, profundidades, ferragens e ornamentos foram simplificados, os materiais têm apenas cores de visualização, sem texturas fotográficas, e os arquivos não possuem os parâmetros de edição de uma família Revit nativa.
- Na Janela 04, a largura do vão foi calibrada para a medida de referência de 1,18 m. Nas demais janelas, a escala métrica vem das malhas OBJ de origem.
- Os modelos representam o estado documentado durante o levantamento e não substituem inspeção, projeto, laudo, diagnóstico de conservação ou levantamento dimensional no local.

## Proteção, privacidade e procedência

- O manuscrito inédito, os vídeos originais com áudio e os arquivos temporários de trabalho são excluídos do Git e não fazem parte das versões públicas.
- Os vídeos distribuídos foram derivados dos originais com remoção de áudio e metadados de captura e conversão para H.264 vertical em 608 × 1080 pixels.
- Amostras visuais dos vídeos foram revisadas para reduzir o risco de exposição de pessoas ou informações pessoais. Ainda assim, comunique qualquer problema pelos canais indicados em [SECURITY.md](SECURITY.md).
- Os arquivos RFA podem conservar metadados técnicos próprios do Autodesk Revit, como versão, identificadores internos e histórico do documento.

## Como citar

Consulte [`CITATION.cff`](CITATION.cff) ou utilize, provisoriamente:

> COUTINHO, Pedro Lucas; RIBEIRO, Raquel. *Biblioteca HBIM de elementos arqueados históricos*. Versão 0.2.0, 2026. Disponível em: https://github.com/Pedrovisk26/biblioteca-hbim-arcos.

Quando o artigo receber referência bibliográfica definitiva, esta seção deverá ser atualizada com título final, evento, ano, páginas e DOI, se aplicável.

## Licença e atribuição

Salvo indicação em contrário, a documentação, os modelos, as malhas e os vídeos distribuídos neste projeto estão licenciados sob a [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](LICENSE.md). A licença permite compartilhamento e adaptação, inclusive para fins comerciais, desde que Pedro Lucas Coutinho e Raquel Ribeiro sejam creditados, a licença seja indicada e eventuais alterações sejam identificadas.

Autodesk e Revit são marcas de seus respectivos titulares. A disponibilização dos arquivos não implica vínculo, certificação ou endosso da Autodesk nem dos responsáveis pelos imóveis documentados.

## Financiamento

De acordo com o manuscrito em elaboração, esta pesquisa não recebeu financiamento específico de agências dos setores público, comercial ou sem fins lucrativos.

## Organização dos arquivos e continuidade do projeto

A biblioteca conta com um [catálogo de elementos](catalogo/README.md), com IDs permanentes, fichas de uso e metadados individuais. O cadastro relaciona esses IDs aos nomes e pacotes das versões 0.1.0 e 0.2.0, mantendo os downloads existentes. As fichas dos modelos IFC4 estão dentro de cada pacote da versão 0.2.0.

- [Padrão de pastas, nomes e versões](docs/padrao-arquivos.md).
- [Guia de salvamento e entrega para colaboradores](docs/guia-colaborador.md).
- [Diagrama de demonstração](docs/diagrama.md).
- [Modelos de ficha, metadados e inventário](modelos/README.md).
- [Inventário documental da versão 0.1.0](releases/v0.1.0/README.md).
- [Inventário documental da versão 0.2.0](releases/v0.2.0/README.md).

O Git mantém documentação e metadados. Fontes de captura, projetos de processamento e modelos em edição ficam no acervo de trabalho. Arquivos pesados revisados continuam sendo distribuídos por Releases. As convenções de nomes e pacotes novos aplicam-se às próximas entregas; os pacotes já publicados conservam seus nomes e conteúdo.
