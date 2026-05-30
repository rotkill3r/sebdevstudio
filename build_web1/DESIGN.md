# Seb_DevStudio Design System

## Brand Identity
- **Name**: Seb_DevStudio
- **Tagline**: Desarrollo moderno + AI tools
- **Vibe**: Technical-premium, modern, developer-first

## Color Palette
| Token | Light | Dark |
|---|---|---|
| `brand-indigo` | `#4F46E5` | `#4F46E5` |
| `brand-cyan` | `#06B6D4` | `#06B6D4` |
| `deep-indigo` | `#1E1B4B` | `#1E1B4B` |
| `surface` | `#F8FAFC` | `#0F172A` |
| `surface-mid` | `#FFFFFF` | `#1E293B` |
| `text-primary` | `#0F172A` | `#F1F5F9` |
| `text-secondary` | `#475569` | `#94A3B8` |
| `amber-accent` | `#F59E0B` | `#F59E0B` |

## Typography
- **Display/body**: Instrument Sans (Google Fonts)
- **Code/accents**: JetBrains Mono (Google Fonts)
- **Scale**: text-xs(12px) → text-sm(14px) → text-base(16px) → text-lg(18px) → text-xl(20px) → text-2xl(24px) → text-3xl(30px) → text-4xl(36px) → text-5xl(48px) → text-7xl(72px)

## Layout
- **Max width**: 1200px
- **Section padding**: 120px (`py-section`)
- **Grid gap**: 6 (24px) default

## Components
- **Buttons**: Solid indigo/cyan bg, uppercase tracking-wider, shadow on primary
- **Cards**: White bg, border-black/5, border-top color accent
- **Dark mode**: `.dark` class on `<html>`, toggle via Alpine
- **Forms**: Bottom-border style, focus ring brand color

## Dark Mode
- Apply `dark:` prefix to every color class
- Toggle button swaps `dark_mode` / `light_mode` icons
- Persistent via localStorage (future enhancement)
