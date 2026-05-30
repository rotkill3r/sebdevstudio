# Auditoría UX — Seb_Proyect

> Generado: 2026-05-29 · Build: v1.0 · Propósito: Seguimiento de integraciones continuas

---

## 1. Resumen Ejecutivo

| Dimensión | Score | Estado |
|---|---|---|
| **UX General** | 82/100 | Bueno |
| **Accesibilidad** | 68/100 | Mejorable |
| **Performance (CDN)** | 75/100 | Bueno |
| **CRO (Conversión)** | 85/100 | Bueno |
| **Semántica/SEO** | 70/100 | Mejorable |

---

## 2. Accesibilidad

### Aciertos
- Roles semánticos: `header`, `section`, `footer`, `nav` correctamente usados
- Contraste suficiente en textos principales (#FFFFFF sobre #050A14)
- `aria-label` implícito en links de navegación con texto visible
- `font-family` con fallback (`serif`, `sans-serif`)

### Por corregir
- **`<html>` sin `lang="es"` correcto** → ✓ Ya tiene `lang="es"`
- **Formulario sin `id`/`for`** → ✓ Corregido en esta build
- **Iconos `material-symbols-outlined` sin `aria-hidden="true"`** — agregar en próxima iteración
- **Botones hamburguesa sin `aria-expanded`** — agregar en próxima iteración
- **Sin skip-to-content link** para navegación por teclado
- **Focus styles** dependen del navegador, no hay `:focus-visible` personalizado

---

## 3. Performance

### CDN externos (render-blocking)

| Recurso | Peso (aprox) | Impacto |
|---|---|---|
| Tailwind CSS (CDN) | ~300 KB | Alto — usa plugin `forms,container-queries` |
| Alpine.js + Collapse | ~40 KB | Medio |
| Google Fonts (Inter + DM Serif) | ~30 KB | Medio |
| Google Icons (Material Symbols) | ~50 KB | Bajo (carga asíncrona) |
| Video hero (Pixabay CDN) | ~10.3 MB | Alto en móvil — LCP impactado |

### Recomendaciones
1. **Reemplazar Tailwind CDN por build local** (purge reduce a ~15 KB)
2. **Agregar `loading="lazy"`** en imágenes del portfolio → ✓ Hecho
3. **Video hero** tiene `poster` y `opacity: 0.3` — mitigación parcial
4. **Preload** del video hero con `<link rel="preload">` para mejorar LCP

---

## 4. CRO (Optimización de Conversión)

### Implementado en esta build
- Botón CTA "Diagnostic Assessment" ahora visible en mobile
- Formulario con `id`/`for` en todos los campos
- CTA de servicios con efecto `translate-x` en hover (más notorio)
- Hero metrics con gap reducido en mobile
- Scroll reveal con rootMargin mejorado para mobile

### Pendiente
- **Anclas de footer** apuntan genéricamente a `#services` — idealmente conectar a filtros específicos
- **Trust signals** visibles (logos de clientes, testimonios) — no implementado
- **Sticky CTA** en mobile para el formulario de contacto

---

## 5. Semántica y SEO

### Meta tags
| Tag | Presente | Valor |
|---|---|---|
| `title` | ✓ | "Seb_Proyect — AI Marketing Intelligence" |
| `meta description` | ✗ | **No presente** — agregar |
| `og:title` | ✗ | **No presente** |
| `og:description` | ✗ | **No presente** |
| `og:image` | ✗ | **No presente** |
| `canonical` | ✗ | **No presente** |
| `robots` | ✗ | **No presente** |
| JSON-LD Schema | ✗ | **No presente** |

### Estructura de headings
| Nivel | Uso |
|---|---|
| `h1` | "Marketing de Precisión Impulsado por IA" |
| `h2` | 5 secciones (Servicios, Proceso, Metodología, Casos, Contacto) |
| `h3` | Subtítulos dentro de secciones |

### Recomendaciones inmediatas
1. Agregar `meta description` y `og:tags`
2. Agregar JSON-LD con `@type: ProfessionalService` y `name: Seb_Proyect`
3. Agregar `canonical` URL

---

## 6. Arquitectura de la Página

| Elemento | Estado | Nota |
|---|---|---|
| Header fixed | ✓ | `backdrop-glass` + scroll detection |
| Hero con video | ✓ Nuevo | Pixabay CDN + gradiente fallback |
| 8 Servicios | ✓ | Con filtros Alpine.js + agente chip (nuevo) |
| 5 Sub-Agentes | ✓ | Grid con scores ponderados |
| Metodología (accordion) | ✓ | 4 pasos con Alpine collapse |
| Portfolio (marquee) | ✓ | Imágenes reales desde portadas GAP |
| Formulario contacto | ✓ | Con labels corregidos |
| Footer | ✓ | 3 columnas con links |

---

## 7. Assets e Imágenes

| Tipo | Cantidad | Tamaño total |
|---|---|---|
| Portadas (portfolio) | 10 PNGs | ~9.1 MB |
| Video hero (CDN) | 1 MP4 | ~10.3 MB |
| Iconos (CDN) | ~30 | ~50 KB |

### Observación
Las portadas están en `assets/img/` con nombres normalizados (`portfolio-01.png`…`portfolio-10.png`). El proyecto es autocontenido y portable.

---

## 8. Checklist para Integraciones Futuras

- [ ] **Meta tags SEO** (`description`, `og:*`, `twitter:*`, `canonical`)
- [ ] **JSON-LD** schema markup para organización y servicios
- [ ] **Build local de Tailwind** (reducir payload ~300 KB → ~15 KB)
- [ ] **`aria-hidden`** en iconos decorativos
- [ ] **`aria-expanded`** en menú mobile
- [ ] **Skip-to-content link** al inicio del `body`
- [ ] **Focus styles** personalizados (`:focus-visible`)
- [ ] **Sticky CTA mobile** en formulario de contacto
- [ ] **Testimonios/logos clientes** como trust signals
- [ ] **Sitemap XML** para SEO técnico
- [ ] **Analytics** (GA4 / Plausible) con consentimiento
- [ ] **Service Worker** para cacheo de assets estáticos
- [ ] **Modo oscuro** toggle funcional (ya hay `darkMode: "class"` en Tailwind config)
- [ ] **PDF report generator** integrado con el formulario de contacto

---

## 9. Historial de Cambios

| Fecha | Versión | Cambios |
|---|---|---|
| 2026-05-29 | v1.0 | Build inicial con 8 servicios, 5 agentes, Alpine.js |
| 2026-05-29 | v1.1 | Hero video, portfolio con imágenes reales, 8 fixes CRO, agent chip, labels accesibles |

---

*Auditoría generada manualmente desde análisis de código. Para regenerar automáticamente: `python scripts/analyze_page.py <url>` con Python + BeautifulSoup.*
