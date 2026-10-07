# Modelos para cadastrar elementos

Copiar `ficha-elemento.md` para `elementos/<ID>/README.md` e `metadados-elemento.json` para `elementos/<ID>/metadados.json`. Criar `CHANGELOG.md` com a data e a descrição das alterações do elemento.

`metadados-elemento.json` é um modelo estrutural inicial, não um esquema JSON de validação. O ID é ilustrativo; substituí-lo pelo ID reservado. Campos `null` e listas vazias indicam informação pendente. `estado: "rascunho"` impede que o modelo seja interpretado como cadastro concluído.

## Campos dos metadados

| Campo | Preenchimento |
| --- | --- |
| `schema_version` | Versão deste formato de metadados; formato inicial `1.0.0` |
| `id`, `nome`, `nomes_legados`, `tipo`, `edificio_id` | Identificação e vínculo ao edifício; informações não confirmadas são `null` |
| `classificacao` | Forma do arco, linguagem arquitetônica e base da classificação; não inferir pela numeração |
| `procedencia` | Sessão, método, data e referência permitida para a fonte |
| `geometria` | Unidades, coordenadas, origem e método de verificação; valores `null` se desconhecidos |
| `componentes_disponiveis` | Lista com `componente`, `formato` e `compatibilidade_por_arquivo` |
| `componentes_ausentes` | Componentes procurados e confirmadamente ausentes; vazio não afirma completude |
| `transformacoes` | Lista com `entrada`, `saida`, `operacao`, `software`, `versao`, `responsavel`, `data` |
| `validacoes` | Lista com `verificacao`, `resultado`, `metodo`, `responsavel`, `data` e referência à evidência |
| `autoria`, `licenca` | Autores e licença efetivos; exceções por arquivo no inventário |
| `publicacoes` | Lista com `versao_pacote`, `tag_biblioteca`, `url`, `sha256_zip` |
| `limitacoes`, `pendencias` | Listas de textos específicos, sem esconder desconhecidos |
| `estado`, `revisado_por`, `data_revisao` | Estado documental e revisão; não são uma certificação técnica |

Datas seguem `YYYY-MM-DD`; caminhos dentro do pacote usam `/` e são relativos à pasta raiz do elemento. Não incluir caminhos absolutos de computadores pessoais, tokens ou referências restritas em conteúdo público.

## Inventário por pacote

Copiar `inventario-pacote.json` para `inventario.json` na raiz do conteúdo preparado para o ZIP. Substituir os campos pendentes e listar todos os arquivos de conteúdo, inclusive ficha, metadados, licença, citação e dependências. Excluir `inventario.json` e `SHA256SUMS.txt` desta lista.

Cada entrada de `arquivos` usa a estrutura do arquivo-modelo: caminho, função, componente, formato, software, unidades, tamanho, hash, dependências e licença. Dependências são caminhos relativos existentes ou referências externas explícitas e justificadas. Hashes têm 64 dígitos hexadecimais e tamanhos são inteiros em bytes.

O modelo tem uma entrada ilustrativa com hash e tamanho `null`. Não publicar assim. Nenhum exemplo comprova existência ou compatibilidade de uma família.

Para a Release da biblioteca, criar outro inventário com uma entrada por ZIP: ID, versão do pacote, nome, URL, tamanho em bytes e SHA-256 externo. [O inventário histórico](../releases/v0.1.0/inventario.json) mostra esses campos para os pacotes existentes.
