# Guia de salvamento para colaboradores

Este guia orienta o salvamento e a entrega de novas contribuições. Consulte também o [padrão de arquivos](padrao-arquivos.md) e as [regras de contribuição](../CONTRIBUTING.md). A versão 0.1.0 permanece disponível com seus nomes e pacotes originais.

## Onde salvar

| Arquivo | Destino | Entra no Git? |
| --- | --- | --- |
| Ficha e metadados do elemento | `biblioteca-hbim-arcos/elementos/<ID>/` | Sim |
| Resumo do cadastro | `biblioteca-hbim-arcos/catalogo/elementos.json` | Sim |
| Metodologia e convenções | `biblioteca-hbim-arcos/docs/` | Sim |
| Foto ou vídeo original | `trabalho-hbim/elementos/<ID>/captura/<sessao>/` | Não |
| Projeto de fotogrametria e intermediários | `trabalho-hbim/elementos/<ID>/processamento/` | Não |
| Família em edição | `trabalho-hbim/elementos/<ID>/modelagem/revit<ano>/` | Não |
| Malha exportada e vídeo revisado | `trabalho-hbim/elementos/<ID>/exportacao/` | Não |
| Conteúdo revisado para empacotar | `trabalho-hbim/preparacao-releases/<tag>/<ID>/` | Não |
| ZIP distribuído | `trabalho-hbim/historico-entregas/<tag>/` e assets da Release | Não |
| Inventário e notas da Release | `biblioteca-hbim-arcos/releases/<tag>/` | Sim |
| Manuscrito, revisão e submissão | `Artigo/manuscrito/` | Não |

## Antes de começar

1. Ler o README e o CONTRIBUTING atuais. Descrever a contribuição em uma issue, como já orienta o projeto.
2. Conferir se o elemento já tem ID. Para elemento novo, solicitar reserva ao mantenedor no catálogo. Para outro levantamento do mesmo elemento, criar uma sessão sem duplicar o ID.
3. Usar uma branch curta, por exemplo `dados/HBIM-JAN-0001-metadados` ou `docs/padrao-arquivos`, para a documentação.
4. Definir responsável pelo arquivo binário e pelo backup do acervo. Para trabalhos simultâneos, registrar tarefa e revisão de origem antes de editar.

## Ao salvar uma família

Exemplo hipotético: terceira revisão do conjunto de `HBIM-JAN-0001`, em Revit 2026.

```text
Artigo/trabalho-hbim/elementos/HBIM-JAN-0001/modelagem/revit2026/
└── HBIM-JAN-0001_conjunto_revit2026_r003.rfa
```

Registrar o que mudou desde `r002`, a versão do Revit, os componentes associados e a revisão de origem. Backups automáticos ficam no acervo e não devem ser confundidos com arquivos entregáveis. Para migrar a 2027, criar uma cópia na pasta `revit2027/` e conservar o arquivo 2026.

## Ao exportar uma malha

Salvar em `exportacao/`, usando o ID e a revisão. Registrar programa e versão, unidade, transformação de escala/orientação, quantidade de vértices e faces quando medida, materiais disponíveis e derivados usados. Conservar as fontes em `processamento/`.

Se houver OBJ, MTL e imagens, conferir as referências relativas com a estrutura final. Se não houver MTL, declarar a ausência. Não alterar o conteúdo de uma malha já distribuída sem registrá-lo e gerar outra versão.

## Ao entregar documentação

Copiar [os modelos](../modelos/README.md) para a pasta do elemento e preencher o que estiver confirmado. Usar `null` para desconhecido e explicar a pendência na ficha. Não copiar os exemplos como se fossem medições.

A ficha deve permitir que outra pessoa entenda quais arquivos estão disponíveis, o que pode abrir, em qual software e com quais limitações. O catálogo permite localizar a ficha; os metadados guardam os detalhes técnicos.

## Ao preparar uma publicação

1. Escolher a versão do pacote e registrar a alteração no `CHANGELOG.md` do elemento.
2. Copiar os arquivos selecionados para `preparacao-releases/<tag>/<ID>/`; conservar fontes e originais no acervo.
3. Aplicar nomes de publicação, organizar `revit/`, `mesh/` e `video/`, incluir somente as pastas existentes.
4. Acrescentar ficha, metadados, inventário, licença e citação. Registrar autoria e exceções de licença por arquivo quando existirem, conforme a política atual.
5. Aplicar a revisão de mídia e procedência prevista no CONTRIBUTING: derivados sem áudio ambiente e sem metadados de localização; originais não entram no pacote.
6. Conferir os arquivos no software declarado e documentar as limitações. Quando uma validação não tiver sido feita, identificá-la como pendente.
7. Gerar inventário e hashes internos, preparar o ZIP e testar sua extração em pasta separada. Depois gerar o SHA-256 externo do ZIP.
8. Enviar a documentação em pull request e disponibilizar o pacote ao mantenedor pelo acervo compartilhado restrito. A publicação em Releases é feita após a revisão.

Para conferir um ZIP no PowerShell, execute a partir da pasta que o contém:

```powershell
Get-FileHash -LiteralPath '.\HBIM-JAN-0001_hbim_v0.2.0.zip' -Algorithm SHA256
```

Comparar o resultado com o checksum externo da Release. Esse comando verifica integridade; não verifica escala, qualidade geométrica ou privacidade.

## Checklist de revisão

- [ ] ID reservado, sem duplicação, e correspondência legada registrada.
- [ ] Cada arquivo está na pasta prevista, com nome e versão corretos.
- [ ] Componentes presentes e ausentes estão explícitos.
- [ ] Compatibilidade foi registrada por arquivo; cópia de versão anterior foi preservada.
- [ ] Unidades, coordenadas, origem e transformações estão preenchidas ou marcadas como desconhecidas.
- [ ] Dependências necessárias e limitações de materiais estão documentadas.
- [ ] Autoria, licença e revisão de mídia seguem o CONTRIBUTING existente.
- [ ] Metadados e catálogo concordam nos campos resumidos.
- [ ] Inventário corresponde ao pacote final e hashes foram calculados depois das alterações.
- [ ] ZIP foi extraído e conferido; resultados e pendências constam nas notas.

Usar este checklist junto das verificações do modelo de pull request e do CONTRIBUTING. Os dados técnicos ainda não examinados devem permanecer identificados como pendentes.
