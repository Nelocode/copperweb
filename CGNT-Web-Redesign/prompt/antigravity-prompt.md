# CGNT Web Redesign — Prompt para Antigravity (o Claude Code)

## Ubicación del proyecto
Ruta: `~/Desktop/CGNT-Web-Redesign/`

Contiene:
- `mockups/CGNT-Redesign-v4.html` — versión anterior (referencia visual)
- `assets/logo-cgnt.webp` — logo oficial de Copper Giant Resources
- `textos/contenido-completo.md` — todo el texto para cada sección

---

## Objetivo
Generar un archivo `~/Desktop/CGNT-Web-Redesign/mockups/CGNT-Redesign-v5.html`

**Single-file HTML + CSS**, sin dependencias externas excepto Google Fonts CDN.

---

## Design System

### Filosofía
Apple × Linear × Vercel. Dark mode nativo. Cada sección es **100vh** (full viewport height). Todo es **bento grid** modular — secciones intercambiables que se puedan añadir/quitar/reordenar sin romper el layout. El diseño se siente premium, quirúrgico, espacioso — Apple-level.

### Color System (del logo real)
```css
--accent: #FF002C           /* Rojo exacto del logo */
--accent-hover: #ff3355
--accent-glow: rgba(255, 0, 44, 0.15)
--bg-deep: #010102
--bg-canvas: #08090a
--bg-panel: #0f1011
--bg-surface: #191a1b
--text-primary: #f7f8f8
--text-secondary: #d0d6e0
--text-tertiary: #8a8f98
--border-subtle: rgba(255,255,255,0.05)
--border-accent: rgba(255,0,44,0.25)
```

### Typography
- Body/Headings: Inter (weights 300, 400, 500, 600, 700)
- Data/Labels: JetBrains Mono (weights 400, 500)
- Letter-spacing: -2.4px en H1, -0.8px en H2, -0.4px en body
- Font-feature-settings: 'tnum' en todos los números

### Componentes visuales
- **Glass nav**: fixed top, height 56px, backdrop-filter: saturate(180%) blur(20px), bg rgba(8,9,10,0.8)
- **Bento cards**: bg #191a1b, border rgba(255,255,255,0.05), border-radius 16px, padding 24px, hover: box-shadow con accent glow
- **Bento grid**: 12-column grid, gap 12px. Responsive → single column en mobile
- **Animations**: fadeUp 0.8s ease-out con staggered delay (cada bento card)
- **CTAs**: Pill buttons, border-radius 24px, padding 12px 28px
- **Labels**: JetBrains Mono 11px tracking 2px, color var(--accent)
- **No tables HTML** — todo en bento cards

## Secciones (orden, cada una 100vh)

1. **TICKER BAR** — Compacto, #010102, JetBrains Mono 11px, 3 exchanges: TSXV CGNT C$0.64 | OTC LBCMF $0.48 | FSE 29H0 €0.41

2. **GLASS NAV** — Logo texto "COPPER GIANT", links (Home, Mocoa, Investors, Corporate, News), social icons (Instagram, X, Facebook, LinkedIn con símbolos Unicode), CTA "Rise With Copper" en #FF002C

3. **HERO** — Label rojo "PROPERTY · TEAM · SPONSORSHIP · TIMING", H1 "RISE WITH COPPER" enorme (clamp 64-120px), subtext, CTAs, bento stats row con 6 stats

4. **LATEST NEWS** — Label + 3 bento cards con headlines reales del contenido-completo.md. Flechas prev/next. Modular.

5. **DRILLING HIGHLIGHTS** — Feature card MD-043 + 5 drill hole cards en grid

6. **THE MAKING OF THE GIANT** — Narrativa Mocoa + 4 value props en bento + timeline vertical

7. **MINERAL RESOURCE** — Resource stats + drill stats + location + infrastructure en bento cards

8. **CORPORATE (FIORE GROUP)** — About + Frank Giustra bio + Fiore stats + Values bento

9. **THE COPPER GIANT WAY (ESG)** — Impact stats + values + ESG initiatives en bento

10. **INVESTOR HIGHLIGHTS** — Financial stats + exploration plan + downloads + events con CTAs

11. **CTA FINAL** — "Rise With Copper" + "The copper deficit is coming..." + 2 CTAs

12. **FOOTER** — Logo, exchange info, links, social, copyright

## Reglas de oro
1. NO html tables — todo en bento grid cards
2. Cada sección = 100vh (min-height: 100vh)
3. Cada sección tiene su label JetBrains Mono en #FF002C
4. Todo el contenido REAL del archivo contenido-completo.md
5. Animaciones sutiles fadeUp con Intersection Observer
6. Responsive: desktop 12-col grid → tablet 6-col → mobile 1-col
7. NO gradients excepto accent radial glow sutiles
8. CTA en cada sección (pill buttons)
9. Imágenes: usar el archivo assets/logo-cgnt.webp como referencia del logo

---

## Cómo generar

Lee primero textos/contenido-completo.md para el contenido exacto de cada sección.
Luego mockups/CGNT-Redesign-v4.html para referencia visual del diseño previo (no copiar, solo inspirarse).
Finalmente escribe mockups/CGNT-Redesign-v5.html con el nuevo diseño.
