# Contribuição e governança dos dados

Contribuições que melhorem a documentação, a interoperabilidade ou a reutilização dos objetos são bem-vindas.

## Antes de propor uma alteração

- Abra uma *issue* descrevendo o elemento, o formato e a finalidade da mudança.
- Não envie manuscritos inéditos, arquivos de submissão ou comentários de revisão por pares.
- Não inclua credenciais, caminhos de rede, identificadores de nuvem, dados pessoais ou imagens de pessoas identificáveis sem base e autorização adequadas.
- Remova áudio ambiente e metadados de localização de imagens e vídeos.
- Confirme que você possui os direitos necessários para disponibilizar o material sob CC BY 4.0.
- Informe a versão do software e as unidades adotadas.

## Arquivos grandes

RFA, OBJ, MTL e MP4 são ignorados no histórico Git. Novos conjuntos devem ser preparados como pacotes de versão, acompanhados de inventário e checksum SHA-256. Não altere o `.gitignore` apenas para contornar esse fluxo.

## Revisão mínima

Toda contribuição de dados deve indicar:

1. origem e método de captura;
2. transformações e programas utilizados;
3. escala, unidades e sistema de coordenadas, quando conhecidos;
4. limitações ou partes ausentes;
5. licença e autoria; e
6. resultado de uma revisão de privacidade e segurança.
