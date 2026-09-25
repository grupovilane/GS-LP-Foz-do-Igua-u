# GS Infinity Travel | Landing Page Foz do Iguaçu

Landing page de página única, sem build e sem dependências. Basta abrir o `index.html`
ou subir a pasta inteira em qualquer hospedagem (Hostinger, Netlify, Vercel, GitHub Pages…).

```
GS/
├── index.html          ← a página inteira (HTML + CSS + JS)
├── assets/             ← logo e imagens
├── CREDITOS.md         ← autoria e licença das imagens
└── README.md
```

---

## ⚠️ Ajustes antes de publicar

### 1. Nome das fundadoras
As fotos em "Sobre nós" estão legendadas como **Gel** e **Sol**, que foi o que deu para
deduzir dos nomes dos arquivos (`gel.png` e `sol.png`). Confirme se é assim que elas
querem aparecer, ou troque pelos nomes completos no `index.html`, dentro de
`<figcaption>`.

### 2. Garganta do Diabo
O aviso de que a passarela está fechada fica no fim do roteiro, num card damasco. Quando
ela reabrir, é só apagar o bloco `<div class="aviso">` do `index.html` e devolver a
menção ao texto do 3º dia.

### 3. Foto de dois depoimentos
Aurora Cardozo e Vitoria ainda aparecem com a inicial no círculo, porque não veio foto
com esses nomes. A pasta `assets/provas sociais` tem uma `helena.jpg` que sobrou: se ela
for uma das duas, me diga qual que eu troco.

> **Contato já configurado:** o WhatsApp da página é o **(11) 94085-6046**. Ele fica em
> duas constantes no fim do `index.html`, dentro do `<script>`:
>
> ```js
> const WHATSAPP = "5511940856046";        // 55 + DDD + número, só dígitos
> const TELEFONE_EXIBIDO = "(11) 94085-6046";  // como aparece na tela
> ```
>
> A primeira alimenta os 7 botões da página e o envio do formulário. A segunda é só o
> texto mostrado no fim do formulário. Para trocar de número, mude as duas.

> O valor **R$ 5.000 por pessoa** e a lista de itens inclusos vieram direto das peças
> de campanha da GS para Foz do Iguaçu, então já estão corretos.

---

## Identidade visual

Toda a paleta está em variáveis CSS no topo do `index.html`, em `:root`. As cores foram
amostradas diretamente do logo oficial e das peças de campanha da marca.

| Token | Cor | Onde aparece |
|---|---|---|
| `--navy` | `#120D44` | Marinho: header, hero, roteiro, FAQ, depoimentos, rodapé |
| `--mint` | `#71E6CC` | Menta: destaques, faixa animada, CTA final |
| `--gold` | `#FFC100` | Dourado: rota de voo, botão do header, números dos dias |
| `--apricot` | `#FDCE82` | Damasco: card "Incluso", accordion, botões |
| `--cream` | `#FAF9F6` | Base clara: fundos e painéis |
| `--teal` | `#40A3B6` | Petróleo: seção "Sobre nós" e labels |
| `--royal` | `#051D7D` | Azul royal: reserva de apoio |
| `--serenity` | `#BFDCF2` | Serenity: links do menu do topo |
| `--nav-pill` | `#08051D` | Cápsula escura que envolve o menu |

**Tipografia:** três níveis, iguais aos das peças de campanha.

| Fonte | Onde | Papel |
|---|---|---|
| `Titan One` | "FOZ DO IGUAÇU", títulos de seção, faixa menta, "R$ 5.000" | o display gordinho e redondo dos criativos |
| `Fredoka` (600) | botões, títulos dos dias, hotéis, accordion, pilares | títulos de apoio |
| `Poppins` (300–600) | textos, rótulos em caixa alta com tracking largo | leitura |

Para trocar o display, basta mudar `--bubble` em `:root`.

**Menu do topo:** os links ficam dentro de uma cápsula arredondada escura, em negrito e
azul claro, no mesmo padrão da referência. A logo tem 78px de altura no desktop e 65px no
celular (30% maior que antes), e as âncoras param abaixo do cabeçalho fixo por causa do
`scroll-padding-top`.

**Elementos de assinatura reproduzidos das peças:**
- Rota de voo tracejada em dourado, com o aviãozinho percorrendo a linha inteira em
  loop contínuo de 15s (`animateMotion` + `rotate="auto"`, então ele se inclina
  acompanhando a curva). Divide as seções (`.flightpath`)
- Gotinhas damasco ao lado dos números (`.sparkle`)
- Botão pill com "knob" damasco, no estilo do "RESERVE AGORA" (`.toggle`)
- Card damasco com ícones circulares marinho e itens sublinhados (seção "Incluso")

**Logo:** `assets/logo-light.png` (para fundos escuros) e `assets/logo-navy.png` (para
fundos claros), ambos em PNG com fundo transparente, extraídos do manual da marca.

---

## Estrutura da página

1. **Header** marinho fixo, com a logo à esquerda e o menu numa cápsula escura à direita
   (vira menu hambúrguer abaixo de 1024px). Na base dele corre a **barra de progresso**
   de leitura, em degradê menta para dourado
2. **Hero** marinho, com "Foz do Iguaçu", foto com moldura menta, selo de preço damasco
3. **Faixa menta** animada com os destaques do roteiro
4. **Incluso**: card damasco com os 7 itens do pacote + "não está incluso" + assinatura da marca
5. **Rota de voo** tracejada (divisor)
6. **O roteiro**: 5 dias alternando foto e painel creme, fechando com o aviso de que a Garganta do Diabo está fechada
7. **Banner** "Cuidamos de tudo"
8. **Valor**: o card marinho com R$ 5.000 por pessoa e o botão de reserva
9. **Dúvidas frequentes**: 7 perguntas em accordion damasco sobre fundo marinho
10. **Sobre nós**: petróleo, com o conceito da marca, as duas fundadoras e 3 pilares
11. **O que te espera**: as 5 atrações do pacote
12. **Quem viajou**: 4 depoimentos
13. **CTA final** menta, com o botão que abre o formulário em etapas
14. **Siga a GS**: grade de 6 publicações do Instagram
15. **Rodapé** marinho com logo, navegação e link do Instagram, mais os botões flutuantes de WhatsApp e voltar ao topo

---

## Formulário em etapas

**Todos os botões de reservar** da página abrem este popup: o "Reservar" do header, o
"Reservar agora" do menu mobile e os três "Reserve agora" (hero, bloco de valor e CTA
final). Continuam indo direto para o WhatsApp apenas o botão flutuante, o link do rodapé
e o contato mostrado no fim do formulário.

O popup faz **uma pergunta por vez**, com botão "Avançar" entre elas:

1. Nome
2. WhatsApp (com máscara automática, aceita fixo e celular)
3. E-mail
4. Quantas pessoas (botões de mais e menos, começa em 2)
5. Vai alguma criança? (Sim / Não, e a escolha já avança sozinha)
6. Quantas crianças (**só se respondeu Sim**)
7. Idade de cada criança (**só se respondeu Sim**): uma linha por criança, de 0 a 17 anos,
   com 0 valendo bebê de menos de 1 ano
8. Resumo, para conferir antes de enviar

Sem crianças são 6 perguntas; com crianças, 8. O contador no topo se ajusta sozinho.

Cada etapa valida antes de deixar passar, e a mensagem de erro aparece embaixo do campo.
O número de crianças nunca passa de "pessoas menos um", já que toda criança viaja
acompanhada. Se você voltar e mudar a quantidade de crianças, as linhas de idade se
refazem mantendo o que já tinha sido digitado.

**Para onde vai o preenchimento:** ao final, abre o WhatsApp com tudo já escrito na
mensagem, usando a mesma constante `WHATSAPP` do resto da página. Se preferir receber
por e-mail ou num sistema, troque a função `enviar()` no script por um `fetch` para o
seu endpoint; os dados estão prontos no objeto `dados`.

No fim, além da confirmação, aparece o contato direto **(11) 94085-6046** com link para
o WhatsApp, para quem preferir chamar na hora.

Detalhes de uso: fecha no X, no Esc ou clicando fora; trava a rolagem do fundo sem
deixar a página pular; devolve o foco ao botão ao fechar; o Enter avança; e no celular
o popup vira uma folha que sobe de baixo.

---

## Responsividade

Três faixas, com o layout mudando de estratégia em cada uma.

| Faixa | Largura | O que muda |
|---|---|---|
| Celular | até 640px | galeria em 2 colunas; respiros verticais menores; botões flutuantes de 50px; rodapé com folga para não ficar embaixo deles |
| Tablet | 641 a 1023px | menu hambúrguer; hero empilhado com a foto alinhada pela margem do texto; foto do roteiro em 16:10 para encurtar a rolagem; galeria em 4 colunas; rodapé em 2 colunas até 899px |
| Desktop | 1024px ou mais | menu completo; hero em 2 colunas; roteiro alternando foto e painel sobreposto; galeria em 4 colunas |

Há ainda ajustes finos para telas de até 380px e para celular deitado.

Testado em 360, 390, 640, 660, 768, 820, 1024, 1280, 1440 e 1920px: nenhuma rolagem
horizontal, nenhum alvo de toque abaixo de 40px e nenhuma imagem quebrada.

### Peso por plataforma

Cada foto tem uma versão leve (`nome-sm.jpg`) declarada em `srcset`, com `sizes`
descrevendo o espaço real que ela ocupa. O navegador escolhe sozinho conforme a largura
da tela e a densidade de pixels, então celular e tablet baixam bem menos:

| Família | Versão leve | Versão cheia |
|---|---|---|
| `banner` | 900px | 1920px |
| `dia1..dia6` | 900px | 1200px |
| `insta1..insta9`, `arg`, `cde` | 400px | 760px |
| `sol`, `gel` (fundadoras, PNG) | 240px | 420px |

Os avatares dos depoimentos ficam em `assets/depoimentos/`, já recortados em 140px
(39 KB somados). As fotos originais continuam intactas em `assets/provas sociais/`.

A `hero.jpg` não tem variante porque já é pequena.

Os arquivos `hotel1..hotel4` continuam em `assets/`, sem uso, caso a dobra de hospedagem
volte um dia. Pode apagar se preferir.

O `trocar-imagem.py` gera as duas versões automaticamente, então é só usar ele para
trocar qualquer foto e o `srcset` continua válido.

---

## Detalhes técnicos

- HTML/CSS/JS puro, arquivo único, ~2 KB de JS. Sem framework, sem build.
- Imagens redimensionadas e comprimidas, com versão leve para celular e tablet.
- Responsivo de 360px a 1920px, sem rolagem horizontal (ver seção acima).
- Animações de entrada via `IntersectionObserver` e barra de progresso em
  `requestAnimationFrame`, ambas respeitando `prefers-reduced-motion`.
- Acessibilidade: landmarks, `aria-expanded` no menu e no accordion, foco visível, textos alternativos.
- Sem travessões em nenhum texto da página.

---

## Arquivos de imagem sem uso

Estes ficaram em `assets/` depois das últimas mudanças e podem ser apagados (1,6 MB no total):

- `hotel1..hotel4` (mais `-sm`): da dobra de hospedagem, removida
- `insta1`, `insta2`, `insta3`, `insta4`, `insta6`, `insta9` (mais `-sm`): da galeria antiga de 8 fotos
- `dia3`, `dia4` (mais `-sm`): Itaipu e a placa da Garganta do Diabo, trocados
- `logo-navy.png`: versão do logo para fundo claro, ainda não usada
- `depoimentos/helena.jpg`: a foto que sobrou dos depoimentos

---

## Publicações do Instagram

A seção "Siga a GS", logo antes do rodapé, tem uma grade de 6 quadrados. Hoje eles são
**placeholders** em marinho com a marca d'água da logo, em `assets/instagram/`.

Há três formas de colocar as publicações reais ali. A seção já está pronta para as três.

### 1. Manual
Salve uma imagem de cada publicação como `assets/instagram/post1.jpg` até `post6.jpg`
e troque o `href` de cada `<a class="insta__post">` pelo link da publicação.

- Custo zero, nenhuma dependência externa, e fica idêntico ao visual do resto da página
- Precisa ser atualizado na mão quando quiser trocar os destaques
- Para gerar a versão leve de cada uma: `python trocar-imagem.py caminho/foto.jpg`
  não cobre essa pasta, então use uma cópia em 760px e outra em 400px terminada em `-sm`

### 2. Embed oficial do Instagram
Trocar cada `<a>` por um `<blockquote class="instagram-media">` com o link da publicação,
mais o script `//www.instagram.com/embed.js`.

- Oficial, gratuito, sem cadastro
- Cada publicação ainda entra na mão, e o visual é o cartão branco do Instagram, que
  destoa do marinho da página

### 3. Feed automático (escolhida, já implementada)
A página busca as publicações sozinha e as desenha com o CSS dela mesma, então elas ficam
com a cara do site em vez do cartão branco do Instagram.

**Falta só um passo:** criar o feed no [behold.so](https://behold.so), conectar a conta
`@gsinfinitytravel` e colar o endereço JSON que ele gera aqui, no fim do `index.html`:

```js
const FEED_INSTAGRAM = "";   // ex.: "https://feeds.behold.so/XXXXXXXXXXXX"
```

Enquanto estiver vazio, ficam os quadrados de exemplo. Assim que o endereço entrar, a
grade passa a mostrar as 6 publicações mais recentes, cada uma linkando para o post.

Se o feed sair do ar ou o endereço estiver errado, a página volta sozinha para os
quadrados de exemplo, sem quebrar nada.

O código lê os nomes de campo mais comuns (`thumbnailUrl`, `mediaUrl`, `permalink`,
`caption`), então serve também para LightWidget, SnapWidget ou qualquer serviço que
devolva JSON. O que muda de um para outro é só o endereço.

> A API oficial do Instagram (Graph API) também existe, mas exige conta comercial ligada
> a uma página do Facebook, app no Facebook Developers e um token que precisa ser
> renovado a cada 60 dias por um servidor. Não dá para fazer numa página estática como
> esta sem adicionar um backend.
