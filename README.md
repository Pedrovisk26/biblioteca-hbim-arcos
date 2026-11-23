# Biblioteca HBIM de elementos arqueados históricos

Dados e objetos digitais produzidos para a pesquisa **“Modelagem paramétrica e biblioteca de objetos em HBIM como ativo de informação para valorização do patrimônio histórico”** (*Parametric modeling and object libraries in HBIM as information assets for heritage preservation*).

**Autores:** Pedro Lucas Coutinho e Raquel Ribeiro.

## Sobre a pesquisa

O projeto investiga um fluxo de trabalho replicável para documentar, modelar e disponibilizar elementos arqueados de edificações históricas brasileiras. A proposta relaciona fotogrametria, malhas densas e famílias paramétricas no contexto do *Heritage Building Information Modeling* (HBIM), tratando o patrimônio edificado como ativo físico e como ativo de informação.

O recorte inicial reúne janelas e portas de linguagem neoclássica e eclética, com ênfase em arcos plenos, abatidos e semi-elipticos. Os materiais apoiam atividades de documentação, conservação, modelagem e gestão do patrimônio.

Este repositório acompanha um **manuscrito em elaboração** para o 9º Congresso Internacional A ERA BIM – SINAENCO (São Paulo, 24–26 de novembro de 2026). O PDF de trabalho não integra a distribuição pública, pois ainda contém comentários editoriais e seções em revisão. A presença desta referência não significa aceite ou publicação do artigo.

## Janelas em IFC4 — versão 0.2.0

Nove janelas reconstruídas em sólidos a partir das malhas fotogramétricas, com dimensões em metros e materiais por componente. Cada ZIP contém o modelo em `ifc/`, a ficha e os arquivos de documentação e integridade.

Os arquivos IFC4 foram gerados em uma etapa posterior ao estudo inicial. O Codex (OpenAI), ferramenta de inteligência artificial generativa, auxiliou na elaboração de scripts em Python. A reconstrução em sólidos partiu de vistas ortográficas das malhas fotogramétricas em OBJ e da conferência visual de vídeos ou fotogramas do levantamento. Os scripts usaram a biblioteca IfcOpenShell (versão 0.9.0.post1) para gerar os IFC4 com materiais de representação atribuídos aos componentes.

Os nove arquivos foram reabertos no IfcOpenShell para conferir o esquema IFC4, a geometria dos sólidos e as associações de materiais. O IFC da Janela 04 também foi aberto no Autodesk Revit 2026, onde foi importado como DirectShape na categoria Janelas.

| Elemento | ID | Vão (m) | Pacote IFC4 |
| --- | --- | --- | --- |
| [Janela 01](elementos/HBIM-JAN-0001/README.md) | HBIM-JAN-0001 | 1,876 × 2,8375 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0001_hbim_v0.2.0.zip) |
| [Janela 02](elementos/HBIM-JAN-0002/README.md) | HBIM-JAN-0002 | 1,2963 × 2,6899 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0002_hbim_v0.2.0.zip) |
| [Janela 05](elementos/HBIM-JAN-0005/README.md) | HBIM-JAN-0005 | 1,4521 × 3,3837 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0005_hbim_v0.2.0.zip) |
| [Janela 06](elementos/HBIM-JAN-0006/README.md) | HBIM-JAN-0006 | 1,5131 × 2,9054 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0006_hbim_v0.2.0.zip) |
| [Janela 04](elementos/HBIM-JAN-0014/README.md) | HBIM-JAN-0014 | 1,18 × 2,6977 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0014_hbim_v0.2.0.zip) |
| [Janela 10.2](elementos/HBIM-JAN-0015/README.md) | HBIM-JAN-0015 | 1,192 × 2,707 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0015_hbim_v0.2.0.zip) |
| [Janela 11](elementos/HBIM-JAN-0016/README.md) | HBIM-JAN-0016 | 1,208 × 2,803 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0016_hbim_v0.2.0.zip) |
| [Janela 12](elementos/HBIM-JAN-0017/README.md) | HBIM-JAN-0017 | 1,505 × 3,404 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0017_hbim_v0.2.0.zip) |
| [Janela 13](elementos/HBIM-JAN-0018/README.md) | HBIM-JAN-0018 | 1,947 × 3,191 | [ZIP](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-JAN-0018_hbim_v0.2.0.zip) |

[Release v0.2.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.2.0) · [Inventário e verificações](releases/v0.2.0/README.md)

## Porta 01 — pacote reorganizado

[Baixar Porta 01 — HBIM-POR-0001](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.2.0/HBIM-POR-0001_hbim_v0.2.0.zip). O pacote reúne a moldura Revit, a malha OBJ e o vídeo de referência nas pastas `revit/revit2027/`, `mesh/` e `video/`. Consulte a [ficha da porta](elementos/HBIM-POR-0001/README.md).

## Conteúdo da versão 0.1.0

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

## Como usar

1. Baixe o pacote IFC na [v0.2.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.2.0) ou procure os pacotes com RFA, OBJ e MP4 na [v0.1.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.1.0).
2. Confira o checksum SHA-256.
3. Extraia o pacote mantendo sua estrutura de pastas.
4. Use um visualizador BIM para ver o IFC. No Revit, abra ou vincule o arquivo.
5. Abra os arquivos RFA da v0.1.0 em uma versão compatível do Revit.
6. Importe a malha OBJ apenas em ferramentas que suportem a escala, a densidade e as extensões de cor utilizadas pelo arquivo.

Os arquivos RFA não são retrocompatíveis: uma família salva no Revit 2027 não abre diretamente em versões anteriores. Faça uma cópia de trabalho antes de atualizar qualquer família para uma versão mais recente.

## Limitações dos modelos IFC

Os sólidos IFC têm detalhes simplificados e materiais com cores de visualização. As famílias Revit publicadas anteriormente ficam na v0.1.0.

## Limitações conhecidas dos arquivos da versão 0.1.0

- As malhas foram geradas no RealityScan 2.2 e são densas; a maior possui aproximadamente 6,9 milhões de vértices e 13,8 milhões de faces.
- Os arquivos OBJ possuem coordenadas de textura e referências a materiais, mas os arquivos MTL e as imagens de textura originais não estão disponíveis nesta versão. Algumas aplicações conseguem exibir as cores armazenadas junto aos vértices; outras mostrarão apenas a geometria.
- A referência de material interna de `Janela_02.obj` conserva o nome `Janela_01.mtl`, herdado da exportação original. Como nenhum MTL é distribuído, essa referência não deve ser usada para associar materiais.
- Nem todos os elementos possuem uma família RFA principal completa; a tabela acima informa os componentes efetivamente disponíveis.
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

A biblioteca conta com um [catálogo de elementos](catalogo/README.md), com IDs permanentes, fichas de uso e metadados individuais. O cadastro relaciona esses IDs aos nomes e pacotes da versão 0.1.0, mantendo os downloads existentes.

- [Padrão de pastas, nomes e versões](docs/padrao-arquivos.md).
- [Guia de salvamento e entrega para colaboradores](docs/guia-colaborador.md).
- [Diagrama de demonstração](docs/diagrama.md).
- [Modelos de ficha, metadados e inventário](modelos/README.md).
- [Inventário documental da versão 0.1.0](releases/v0.1.0/README.md).

O Git mantém documentação e metadados. Fontes de captura, projetos de processamento e modelos em edição ficam no acervo de trabalho. Arquivos pesados revisados continuam sendo distribuídos por Releases. As convenções de nomes e pacotes novos aplicam-se às próximas entregas; os pacotes já publicados conservam seus nomes e conteúdo.
