# Padrão de organização de arquivos

Padrão adotado para cadastro e documentação de elementos. As regras de nomes e estrutura dos pacotes aplicam-se às próximas entregas; os arquivos e pacotes da versão 0.1.0 conservam seus nomes, conteúdo e links originais.

## 1. Separar biblioteca, acervo de trabalho e manuscrito

Estrutura de referência para o ambiente local, inteiramente dentro de `Artigo`:

```text
Artigo/
├── biblioteca-hbim-arcos/          # cópia Git: documentação e metadados
├── trabalho-hbim/                 # acervo fora da cópia Git
│   ├── elementos/
│   │   └── HBIM-JAN-0001/
│   │       ├── captura/           # fontes originais e sessão de levantamento
│   │       ├── processamento/     # projetos fotogramétricos e intermediários
│   │       ├── modelagem/
│   │       │   ├── revit2026/
│   │       │   └── revit2027/
│   │       └── exportacao/        # derivados e mídia preparada para revisão
│   ├── preparacao-releases/
│   │   └── v0.2.0/               # exemplo de próxima publicação
│   └── historico-entregas/        # cópias exatas dos pacotes distribuídos
└── manuscrito/                    # escrita, revisão e submissão do artigo
```

O acervo local deve ser organizado pela equipe conforme os arquivos disponíveis. Essas pastas de fontes e manuscrito não integram o histórico Git. O acervo precisa de backup independente do Git e de um local compartilhado sob responsabilidade do mantenedor. O endereço de armazenamento de fontes restritas fica em um índice restrito do acervo, sem credenciais ou caminhos pessoais nas fichas públicas.

## 2. Estrutura da biblioteca no Git

```text
biblioteca-hbim-arcos/
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── CITATION.cff
├── SECURITY.md
├── SHA256SUMS.txt                 # checksums da versão destacada no README
├── .gitignore
├── .gitattributes
├── .github/
│   └── pull_request_template.md
├── docs/
│   ├── padrao-arquivos.md
│   ├── guia-colaborador.md
│   ├── diagrama.md
│   └── dicionario-parametros.md
├── catalogo/
│   └── elementos.json             # índice resumido, um registro por ID
├── elementos/
│   ├── HBIM-JAN-0001/
│   │   ├── README.md              # ficha de uso e limitações
│   │   ├── metadados.json          # informação técnica estruturada
│   │   └── CHANGELOG.md           # alterações deste elemento
│   └── HBIM-POR-0001/
│       └── ...
├── modelos/
│   ├── ficha-elemento.md
│   ├── metadados-elemento.json
│   └── inventario-pacote.json
└── releases/
    └── v0.1.0/
        ├── README.md              # índice documental da publicação existente
        ├── inventario.json        # pacotes, versões, URLs e hashes dos ZIPs
        └── SHA256SUMS.txt
```

Os diretórios `docs/`, `catalogo/`, `elementos/`, `modelos/` e `releases/v0.1.0/` organizam a documentação da biblioteca. Criar `docs/metodologia.md` quando houver detalhamento revisado para complementar a descrição de pesquisa já presente no README. Criar `scripts/` somente quando houver uma automação real. Criar subpastas opcionais como `imagens/` apenas quando houver imagens pequenas revisadas para documentação.

As pastas por formato ficam dentro do pacote do elemento. Organizar a raiz por `rfa/`, `obj/` e `mp4/` separaria informações que precisam ser compreendidas juntas. Organizar por tipo de arco ou edifício faria os caminhos mudarem quando o conhecimento sobre o elemento fosse atualizado.

## 3. ID permanente e cadastro

Formato: `HBIM-<tipo>-<numero>`.

| Parte | Regra |
| --- | --- |
| Prefixo | `HBIM` |
| Tipo inicial | `JAN` para janela; `POR` para porta |
| Número | Sequência com no mínimo quatro dígitos, global por tipo na biblioteca |
| Exemplo | `HBIM-JAN-0001` |

O mantenedor reserva o ID no catálogo antes do início de uma contribuição. Nunca reutilizar ID removido; conservar o registro como retirado ou substituído. Não reiniciar a numeração por edifício. Caso surjam novos tipos, documentar a sigla antes de usá-la. O ID permanece mesmo que a classificação seja corrigida; o tipo atualizado aparece nos metadados.

Correspondência inicial adotada: Janela 01 → `HBIM-JAN-0001`; Janela 02 → `HBIM-JAN-0002`; Janela 05 → `HBIM-JAN-0005`; Janela 06 → `HBIM-JAN-0006`; Porta 01 → `HBIM-POR-0001`. Manter as lacunas até esclarecer os elementos 03 e 04; não presumir que não existam.

Um ID representa o elemento documentado. Arquivos de folha, moldura e bandeira são componentes dele. Reutilizar uma família em outro elemento não torna os dois elementos físicos iguais. Registrar compartilhamento e derivação nos metadados. Um novo levantamento do mesmo elemento mantém o ID e ganha uma nova sessão de captura.

Se houver múltiplos edifícios, cadastrar um `edificio_id` estável e suas informações uma única vez em `catalogo/edificios.json`, referenciado pelos elementos. Até haver confirmação, usar `null`. Dados de localização restritos ficam no acervo restrito.

## 4. Nomes de arquivos

Pastas operacionais e descrições: minúsculas, sem espaços e sem acentos, com hífen entre palavras. IDs: maiúsculas. Documentos convencionais mantêm nomes como `README.md`, `CHANGELOG.md` e `SHA256SUMS.txt`. A extensão deve representar o formato real; converter o arquivo antes de mudar sua extensão.

**Arquivo de trabalho:** `<ID>_<componente-ou-produto>_<software>_rNNN.<ext>`.

```text
HBIM-JAN-0001_conjunto_revit2026_r003.rfa
HBIM-JAN-0001_folha_revit2027_r002.rfa
HBIM-JAN-0001_malha-densa_realityscan2-2_r001.obj
HBIM-JAN-0001_referencia-sem-audio_h264_r001.mp4
```

`rNNN` é uma revisão local registrada no histórico de trabalho. Quando várias pessoas editarem um mesmo binário, definir um responsável pela revisão seguinte; não usar merge textual de RFA ou projeto fotogramétrico. Trabalhos paralelos ficam em subpastas de tarefa no acervo, com responsável indicado no registro da tarefa.

**Arquivo preparado para distribuição:** `<ID>_<componente-ou-produto>_<software>_vX.Y.Z.<ext>`.

```text
HBIM-JAN-0001_conjunto_revit2026_v0.2.0.rfa
HBIM-JAN-0001_moldura_revit2027_v0.2.0.rfa
HBIM-JAN-0001_malha-densa_realityscan2-2_v0.2.0.obj
HBIM-JAN-0001_referencia-sem-audio_h264_v0.2.0.mp4
HBIM-JAN-0001_hbim_v0.2.0.zip
```

Os exemplos mostram o padrão; não comprovam que tais arquivos existam. Para software não identificado, usar `software-nao-informado` e registrar a lacuna. Para fontes de captura, usar `<ID>_captura_YYYY-MM-DD_sNN/` e conservar nomes originais, registrando a associação no índice da sessão. A data é a da captura, nunca a data presumida de criação do arquivo.

Vocabulário inicial de componentes: `conjunto`, `folha`, `moldura`, `bandeira`. Havendo duas folhas diferentes, usar `folha-01` e `folha-02` e explicar a correspondência na ficha. Para produtos: `malha-densa`, `malha-simplificada`, `referencia-sem-audio`. Novos termos entram no dicionário antes de serem usados.

Evitar `final`, `final2`, `novo`, nomes de pessoas e datas como único indicador de versão. Não incluir estilo ou tipo de arco no nome: essas classificações pertencem aos metadados.

## 5. Estrutura de cada pacote de distribuição

```text
HBIM-JAN-0001_hbim_v0.2.0.zip
└── HBIM-JAN-0001/
    ├── README.md
    ├── metadados.json
    ├── inventario.json
    ├── LICENSE.md
    ├── CITATION.cff
    ├── SHA256SUMS.txt
    ├── revit/
    │   ├── revit2026/
    │   │   └── HBIM-JAN-0001_conjunto_revit2026_v0.2.0.rfa
    │   └── revit2027/
    │       └── HBIM-JAN-0001_folha_revit2027_v0.2.0.rfa
    ├── mesh/
    │   └── HBIM-JAN-0001_malha-densa_realityscan2-2_v0.2.0.obj
    └── video/
        └── HBIM-JAN-0001_referencia-sem-audio_h264_v0.2.0.mp4
```

Criar apenas as pastas com conteúdo disponível. A ficha informa explicitamente o que está ausente. `revit/`, `mesh/` e `video/` preservam os termos já apresentados no README. Se no futuro houver IFC, incluir `ifc/` após documentar exportador, esquema e validação, sem prometer equivalência automática à família nativa.

OBJ, MTL e texturas devem manter caminhos relativos válidos. Ao renomear um OBJ, revisar `mtllib`, referências do MTL e imagens associadas. Se os materiais não estiverem disponíveis, registrar a ausência; não criar um MTL fictício para aparentar um pacote completo.

Famílias aninhadas, catálogos de tipos e outras dependências necessárias devem acompanhar o pacote ou estar comprovadamente incorporadas. A ficha informa como carregar o conjunto. Preservar os identificadores e nomes internos do Revit durante a adoção inicial; alterá-los exige avaliação dos vínculos e registro específico.

## 6. Versões e compatibilidade

| Informação | Exemplo | Uso |
| --- | --- | --- |
| Versão do software | `revit2027` | Compatibilidade de abertura |
| Revisão de trabalho | `r003` | Histórico local antes da publicação |
| Versão do pacote do elemento | `0.2.0` | Identifica o conteúdo distribuído |
| Versão do esquema de metadados | `1.0.0` | Define como interpretar os campos |
| Tag da biblioteca | `v0.2.0` | Reúne versões exatas dos pacotes publicados |

Uma Release futura pode reutilizar o pacote inalterado `0.1.0` de um elemento e acrescentar outro em `0.2.0`. O inventário da Release informa a versão e URL exatas de cada pacote. Não renomear ou recarregar um pacote antigo só para igualar sua versão à tag nova.

Convenção para as próximas versões de pacote: `PATCH` para ajustes de documentação sem impacto de uso; `MINOR` para novos componentes ou derivados compatíveis; `MAJOR` para alteração que exija adaptação de uso, como parâmetros incompatíveis, escala ou mudança da versão mínima do software. Na fase `0.x`, explicar qualquer incompatibilidade nas notas, além do número. Mudanças só na documentação do Git não exigem reempacotar binários.

Manter cópia em Revit 2026 antes de salvar em 2027. Não considerar uma cópia 2027 como substituta de uma 2026. Registrar a compatibilidade de cada arquivo separadamente; não atribuir ao conjunto inteiro uma compatibilidade que só foi confirmada para uma parte.

## 7. Metadados e parâmetros

Cada elemento deve informar identificação, nomes legados, componente disponível, procedência, método, software, autoria, licença, referências de publicação, limitações, unidades e estado de revisão.

Cada arquivo publicado deve ter caminho relativo, função, componente, software, tamanho em bytes, SHA-256, dependências e unidades. Cada etapa deve registrar entrada, saída, programa, versão, responsável e operação aplicada. Transformações de escala, orientação, simplificação ou remoção de mídia precisam ficar explícitas.

Para geometria, registrar separadamente unidades da malha, unidades dos parâmetros dimensionais, sistema de coordenadas e sua origem. `null` significa desconhecido; `nao_aplicavel` deve ser acompanhado de justificativa. Nunca inferir metros apenas por ser um fluxo BIM. Registrar erro dimensional e nível de detalhe somente se houver método e evidência; não atribuir precisão ou nível BIM por aparência visual.

O dicionário de parâmetros do Revit deve reunir: nome exato, significado, tipo de dado, unidade, instância ou tipo, obrigatório ou opcional, fórmula ou regra, GUID quando for parâmetro compartilhado e versão de introdução. Não renomear parâmetros já publicados apenas para padronizar sua grafia. As lacunas iniciais são registradas até que as famílias sejam examinadas.

O catálogo é um índice de descoberta; os metadados individuais são a referência técnica. Copiar para o catálogo apenas ID, nome, tipo, edifício, caminho da ficha e versão publicada. Toda alteração desses campos precisa atualizar ambos na mesma contribuição. Se a biblioteca crescer, gerar o índice a partir das fichas com um script, evitando manutenção duplicada.

## 8. Integridade e publicação

O `inventario.json` interno lista os arquivos de conteúdo do pacote, com hashes e dependências. Ele não lista a si próprio nem o `SHA256SUMS.txt`, evitando hashes circulares. O checksum interno pode incluir o inventário, mas nunca inclui a si próprio. O checksum externo da Release verifica os ZIPs completos e fica fora deles.

Gerar hashes somente depois da revisão e dos nomes definitivos. Validar o ZIP extraído em outra pasta, suas referências de materiais e compatibilidade documentada. Publicar documentação e inventário vinculados ao mesmo commit da tag. Preservar cada Release já publicada; mudanças geram novo pacote e novas notas.

Git continua armazenando documentação e metadados. RFA, OBJ, MTL, MP4, ZIP, projetos de fotogrametria e intermediários ficam no acervo e, quando aprovados para distribuição, em Releases. Git LFS só deve ser avaliado se a equipe precisar versionar binários no desenvolvimento; não é necessário para o fluxo atual de distribuição.
