# HBIM-POR-0001 — Porta 01

Cadastro documental da versão existente, com verificação técnica por arquivo pendente. O ID organiza o catálogo e não altera o nome nem o conteúdo do pacote publicado.

## Identificação

| Campo | Informação |
| --- | --- |
| ID permanente | `HBIM-POR-0001` |
| Nome legado | Porta 01 |
| Tipo | Porta |
| Edifício | Não informado na documentação consultada |
| Forma do arco | Não individualizada na documentação consultada |
| Data e sessão de captura | Não informadas |

## Conteúdo declarado na versão 0.1.0

| Produto | Informação do README |
| --- | --- |
| Famílias Revit | moldura |
| Versão do Revit | 2027 |
| Malha fotogramétrica | OBJ; RealityScan 2.2 |
| Vídeo de referência | MP4 sem áudio |

Somente os componentes listados acima estão documentados como disponíveis. A correspondência entre componentes, nomes internos e dependências deve ser confirmada ao examinar os arquivos. Não presumir uma família principal completa quando ela não estiver listada.

## Download e integridade

- [Baixar `Porta_01_HBIM_v0.1.0.zip`](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/download/v0.1.0/Porta_01_HBIM_v0.1.0.zip).
- [Consultar a Release v0.1.0](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/releases/tag/v0.1.0).
- [Inventário da publicação](../../releases/v0.1.0/inventario.json) e [checksums](../../releases/v0.1.0/SHA256SUMS.txt).

SHA-256 declarado para o ZIP:

```text
def9b2bcfb4f509f3a943a8543d469b9c59621255ab5bef057f6e359b1f27f6b
```

O hash foi conferido entre as declarações do repositório e da API GitHub. O ZIP não foi baixado nem submetido a novo cálculo nesta organização.

## Uso e compatibilidade

Extrair o pacote mantendo sua estrutura original. Abrir as famílias em uma versão compatível do Autodesk Revit. As famílias não são retrocompatíveis; conservar uma cópia antes de atualizar o software.

O README informa Revit 2027 para o elemento. A abertura e a versão interna de cada família ainda precisam de conferência individual.

Importar a malha somente em ferramenta capaz de lidar com sua densidade e convenções de cor. Unidades, escala, coordenadas e origem ainda não foram confirmadas por arquivo; verificá-las antes da reutilização.

## Limitações e pendências

- MTL e imagens de textura não distribuídos na versão 0.1.0.
- Nomes e tamanhos dos arquivos internos, dependências, parâmetros e resultado de abertura ainda não foram inventariados.
- Escala, coordenadas, classificação do arco, edifício e sessão de captura precisam de documentação individual.
- Os modelos representam o estado documentado e não substituem levantamento de campo, inspeção, projeto ou laudo, conforme o README geral.

## Procedência, autoria e licença

As informações desta ficha foram transcritas do [README no commit de referência](https://github.com/Pedrovisk26/biblioteca-hbim-arcos/blob/cefa868f3636be415f8dd809b02332969f261fed/README.md). A descrição geral da pesquisa, autoria, licença e instruções originais permanece no [README principal](../../README.md).

Autoria indicada: Pedro Lucas Coutinho e Raquel Ribeiro. Licença indicada: [CC BY 4.0](../../LICENSE.md), respeitando as exceções já previstas. Para citar, consultar [CITATION.cff](../../CITATION.cff).

## Continuidade do trabalho

Salvar novas fontes e modelos no acervo local pelo ID `HBIM-POR-0001`. Usar o [guia do colaborador](../../docs/guia-colaborador.md) e o [padrão de arquivos](../../docs/padrao-arquivos.md). As novas regras de empacotamento aplicam-se às próximas entregas; o pacote legado conserva seu nome.

Detalhes estruturados: [metadados.json](metadados.json). Histórico: [CHANGELOG.md](CHANGELOG.md).
