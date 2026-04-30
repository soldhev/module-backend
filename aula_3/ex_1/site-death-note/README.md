# 🖊️ Death Note Store

> Projeto desenvolvido para avaliação da UC de Front-End — SENAC Tech RS

---

##  Sobre o Projeto

Site de e-commerce temático inspirado no anime **Death Note**, simulando uma loja real de produtos colecionáveis. O projeto foi desenvolvido inteiramente com **HTML5, CSS3 e JavaScript puro**, sem o uso de frameworks ou bibliotecas externas.

---

##  Páginas

| Página | Descrição |
|---|---|
| `index.html` | Home com hero, destaques, FAQ, Trabalhe Conosco e Contatos |
| `produtos.html` | Catálogo com filtros, ordenação e modal de detalhes |
| `cadastro.html` | Formulário de cadastro e login com validação completa |

---

##  Tecnologias Utilizadas

- **HTML5** — estrutura semântica com tags `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- **CSS3** — variáveis, Grid, Flexbox, transições, animações e responsividade com media queries
- **JavaScript** — interatividade sem frameworks: DOM, eventos, validações e manipulação de classes
- **Google Fonts** — fontes Inter e Playfair Display via CDN
- **VLibras** — widget de acessibilidade em Libras (gov.br)
- **Google Maps** — localização embarcada via `<iframe>`

---

##  Funcionalidades JavaScript

- **Header com scroll** — fundo aparece ao rolar a página (`scroll` event + `classList.toggle`)
- **FAQ Accordion** — abre e fecha respostas com animação CSS (`max-height` transition)
- **Filtro por categoria** — mostra/esconde cards pelo atributo `data-cat`
- **Ordenação por preço** — reordena o DOM pelo atributo `data-price`
- **Modal de produto** — exibe detalhes completos com especificações e formas de pagamento
- **Toast de carrinho** — notificação animada ao adicionar um produto
- **Abas login/cadastro** — alternância entre formulários
- **Validação de CPF** — algoritmo oficial dos dígitos verificadores
- **Máscara de CPF e telefone** — formatação automática enquanto digita
- **Indicador de força de senha** — 4 níveis com barras coloridas
- **Validação de idade** — mínimo 16 anos pela data de nascimento

---

##  Estrutura de Arquivos

```
📁 death-note-store/
├── index.html
├── produtos.html
├── cadastro.html
├── style.css
└── 📁 imgs/
    ├── p1.jpg   → Caderno Death Note + Pena
    ├── p2.jpg   → Figure Misa Amane
    ├── p3.jpg   → Figure Ryuk
    ├── p4.jpg   → Figure Light Yagami
    ├── p5.jpg   → Figure L Lawliet
```

---

##  Como Executar

1. Baixe todos os arquivos
2. Mantenha a estrutura de pastas conforme acima
3. Abra o arquivo `index.html` no navegador

> Nenhuma instalação necessária — o projeto roda diretamente no browser.

---

##  Acessibilidade

- Widget **VLibras** integrado em todas as páginas (tradução em Língua Brasileira de Sinais)
- Atributos `alt` em todas as imagens
- Contraste adequado entre texto e fundo
- Semântica HTML correta para leitores de tela

---

##  Responsividade

O site é adaptado para diferentes tamanhos de tela via **media queries**:

- **Desktop** → 4 colunas de produtos
- **Tablet** → 2–3 colunas
- **Mobile** → 2 colunas, menu oculto

---

##  Autor

**Carlos Eduardo Cavalcante da Rocha**  
GitHub: [@soldhev](https://github.com/soldhev)  
LinkedIn: [carlos-eduardo-rocha](https://www.linkedin.com/in/carlos-eduardo-rocha-809394375/)  

---

##  Instituição

**SENAC Tech RS**
Ano: 2026

---

