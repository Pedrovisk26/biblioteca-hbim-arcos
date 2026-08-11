# Biblioteca HBIM de elementos arqueados históricos

Dados e objetos digitais produzidos para a pesquisa **“Modelagem paramétrica e biblioteca de objetos em HBIM como ativo de informação para valorização do patrimônio histórico”** (*Parametric modeling and object libraries in HBIM as information assets for heritage preservation*).

**Autores:** Pedro Lucas Coutinho e Raquel Ribeiro.

## Sobre a pesquisa

O projeto investiga um fluxo de trabalho replicável para documentar, modelar e disponibilizar elementos arqueados de edificações históricas brasileiras. A proposta relaciona fotogrametria, malhas densas e famílias paramétricas no contexto do *Heritage Building Information Modeling* (HBIM), tratando o patrimônio edificado como ativo físico e como ativo de informação.

O recorte inicial reúne portas e janelas de linguagem neoclássica ou eclética, com ênfase em arcos plenos e abatidos. Os materiais apoiam atividades de documentação, conservação, modelagem e gestão do patrimônio.

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
| `Janela_01_HBIM_v0.1.0.zip` | 197 MiB |
| `Janela_02_HBIM_v0.1.0.zip` | 486 MiB |
| `Janela_05_HBIM_v0.1.0.zip` | 571 MiB |
| `Janela_06_HBIM_v0.1.0.zip` | 1,10 GiB |
| `Porta_01_HBIM_v0.1.0.zip` | 191 MiB |

## Como usar

1. Baixe o pacote do elemento desejado na [versão mais recente](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/latest).
2. Confira o checksum SHA-256.
3. Extraia o pacote mantendo sua estrutura de pastas.
4. Abra os arquivos RFA em uma versão compatível do Autodesk Revit.
5. Importe a malha OBJ apenas em ferramentas que suportem a escala, a densidade e as extensões de cor utilizadas pelo arquivo.

Os arquivos RFA não são retrocompatíveis: uma família salva no Revit 2027 não abre diretamente em versões anteriores. Faça uma cópia de trabalho antes de atualizar qualquer família para uma versão mais recente.

## Limitações conhecidas

- As malhas foram geradas no RealityScan 2.2 e são densas; a maior possui aproximadamente 6,9 milhões de vértices e 13,8 milhões de faces.
- Os arquivos OBJ possuem coordenadas de textura e referências a materiais, mas os arquivos MTL e as imagens de textura originais não estão disponíveis nesta versão. Algumas aplicações conseguem exibir as cores armazenadas junto aos vértices; outras mostrarão apenas a geometria.
- A referência de material interna de `Janela_02.obj` conserva o nome `Janela_01.mtl`, herdado da exportação original. Como nenhum MTL é distribuído, essa referência não deve ser usada para associar materiais.
- Nem todos os elementos possuem uma família RFA principal completa; a tabela acima informa os componentes efetivamente disponíveis.
- Os modelos representam o estado documentado durante o levantamento e não substituem inspeção, projeto, laudo, diagnóstico de conservação ou levantamento dimensional no local.

## Proteção, privacidade e procedência

- O manuscrito inédito, os vídeos originais com áudio e os arquivos temporários de trabalho são excluídos do Git e não fazem parte das versões públicas.
- Os vídeos distribuídos foram derivados dos originais com remoção de áudio e metadados de captura.
- Amostras visuais dos vídeos foram revisadas para reduzir o risco de exposição de pessoas ou informações pessoais. Ainda assim, comunique qualquer problema pelos canais indicados em [SECURITY.md](SECURITY.md).
- Os arquivos RFA podem conservar metadados técnicos próprios do Autodesk Revit, como versão, identificadores internos e histórico do documento.

## Como citar

Consulte [`CITATION.cff`](CITATION.cff) ou utilize, provisoriamente:

> COUTINHO, Pedro Lucas; RIBEIRO, Raquel. *Biblioteca HBIM de elementos arqueados históricos*. Versão 0.1.0, 2026. Disponível em: https://github.com/Pedrovisk26/biblioteca-hbim-arcos.

Quando o artigo receber referência bibliográfica definitiva, esta seção deverá ser atualizada com título final, evento, ano, páginas e DOI, se aplicável.

## Licença e atribuição

Salvo indicação em contrário, a documentação, os modelos, as malhas e os vídeos distribuídos neste projeto estão licenciados sob a [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](LICENSE.md). A licença permite compartilhamento e adaptação, inclusive para fins comerciais, desde que Pedro Lucas Coutinho e Raquel Ribeiro sejam creditados, a licença seja indicada e eventuais alterações sejam identificadas.

Autodesk e Revit são marcas de seus respectivos titulares. A disponibilização dos arquivos não implica vínculo, certificação ou endosso da Autodesk nem dos responsáveis pelos imóveis documentados.

## Financiamento

De acordo com o manuscrito em elaboração, esta pesquisa não recebeu financiamento específico de agências dos setores público, comercial ou sem fins lucrativos.
