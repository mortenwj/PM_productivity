---
version: beta 2026-06-16.01
name: Tieto Brand
description: The visual identity of Tieto, written for AI agents that generate brand-compliant PowerPoint presentations. Tokens are derived from the official Tieto PPT template, logotype and brand portal.

colors:
  # Core
  primary: "#021E57"        # Tieto deep navy. The brand anchor, matches the logotype.
  ink: "#272A2C"            # Near-black for body text on light surfaces.
  background: "#FFFFFF"
  surface: "#D2D0CB"        # Warm light grey for panels, quotes, alternating rows.
  secondary: "#78716E"      # Warm grey for supporting text, rules, metadata.
  accent: "#F5FF56"         # Signal yellow. The single pop color. Use sparingly.

  # Brand blues (interaction, charts, emphasis)
  blue-700: "#3531CF"
  blue-500: "#4E60E7"
  blue-300: "#839DF9"

  # On-colors (guaranteed legibility)
  on-primary: "#FFFFFF"
  on-accent: "#021E57"      # Navy text on the yellow accent.
  on-surface: "#272A2C"
  on-background: "#272A2C"

  # Utility
  muted: "#78716E"
  divider: "#D2D0CB"

  # Chart palette. Apply in numeric order so a series keeps its color across the deck.
  chart-1: "#021E57"
  chart-2: "#3531CF"
  chart-3: "#4E60E7"
  chart-4: "#839DF9"
  chart-5: "#F5FF56"
  chart-6: "#78716E"

typography:
  # Tieto Sans throughout. Sizes in px so the file validates; PowerPoint pt = px * 0.75.
  # Weights: Thin 100, Light 300, Regular 400, Medium 500, Bold 700.
  slide-title:
    fontFamily: Tieto Sans
    fontSize: 60px          # 45pt
    fontWeight: 700
    lineHeight: 1.05
  section-header:
    fontFamily: Tieto Sans
    fontSize: 44px          # 33pt
    fontWeight: 700
    lineHeight: 1.1
  subtitle:
    fontFamily: Tieto Sans
    fontSize: 28px          # 21pt
    fontWeight: 300
    lineHeight: 1.3
  heading:
    fontFamily: Tieto Sans
    fontSize: 32px          # 24pt
    fontWeight: 500
    lineHeight: 1.2
  body:
    fontFamily: Tieto Sans
    fontSize: 24px          # 18pt
    fontWeight: 400
    lineHeight: 1.4
  bullet:
    fontFamily: Tieto Sans
    fontSize: 24px          # 18pt
    fontWeight: 400
    lineHeight: 1.4
  kpi-number:
    fontFamily: Tieto Numerals
    fontSize: 80px          # 60pt
    fontWeight: 700
    lineHeight: 1.0
  data-label:
    fontFamily: Tieto Sans
    fontSize: 18px          # 13.5pt
    fontWeight: 500
    lineHeight: 1.2
  kicker:
    fontFamily: Tieto Sans
    fontSize: 16px          # 12pt
    fontWeight: 500
    letterSpacing: 0.10em
    lineHeight: 1.2
  quote:
    fontFamily: Tieto Sans
    fontSize: 40px          # 30pt
    fontWeight: 300
    lineHeight: 1.3
  caption:
    fontFamily: Tieto Sans
    fontSize: 16px          # 12pt
    fontWeight: 400
    lineHeight: 1.3
  footer:
    fontFamily: Tieto Sans
    fontSize: 13px          # 9.75pt
    fontWeight: 400
    lineHeight: 1.2

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px

spacing:
  # 16:9 canvas, 33.87 x 19.05 cm (13.33 x 7.5 in).
  slide-margin: 48px
  content-gap: 24px
  block-padding: 32px
  sm: 8px
  md: 16px
  lg: 32px

components:
  cover-slide:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.slide-title}"
    padding: 64px
  speaker-slide:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.subtitle}"
    padding: 64px
  chapter-slide:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.section-header}"
    padding: 64px
  content-slide:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-background}"
    typography: "{typography.body}"
    padding: 48px
  slide-header:
    textColor: "{colors.primary}"
    typography: "{typography.heading}"
    padding: 16px
  kicker-label:
    textColor: "{colors.blue-700}"
    typography: "{typography.kicker}"
  bullet-list:
    textColor: "{colors.on-background}"
    typography: "{typography.bullet}"
  agenda-item:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-background}"
    typography: "{typography.heading}"
    padding: 16px
  callout-box:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  callout-box-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  callout-box-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  kpi-stat:
    textColor: "{colors.primary}"
    typography: "{typography.kpi-number}"
  kpi-label:
    textColor: "{colors.secondary}"
    typography: "{typography.data-label}"
  column-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.data-label}"
    padding: 12px
  table-row:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-background}"
    typography: "{typography.body}"
    padding: 12px
  table-row-alt:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body}"
    padding: 12px
  quote-slide:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.quote}"
    padding: 64px
  image-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.background}"
    textColor: "{colors.muted}"
    typography: "{typography.footer}"
    padding: 16px
  page-number:
    textColor: "{colors.muted}"
    typography: "{typography.footer}"
  end-slide:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.slide-title}"
    padding: 64px
  body-text:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  link-inline:
    textColor: "{colors.blue-500}"
    typography: "{typography.body}"
  tag-info:
    backgroundColor: "{colors.blue-300}"
    textColor: "{colors.primary}"
    typography: "{typography.data-label}"
    rounded: "{rounded.sm}"
    padding: 8px
  divider-rule:
    backgroundColor: "{colors.divider}"
    height: 1px
  icon-default:
    textColor: "{colors.primary}"
    size: 48px
  icon-on-navy:
    textColor: "{colors.on-primary}"
    size: 48px
  icon-accent:
    textColor: "{colors.blue-500}"
    size: 48px
  chart-series-1:
    backgroundColor: "{colors.chart-1}"
  chart-series-2:
    backgroundColor: "{colors.chart-2}"
  chart-series-3:
    backgroundColor: "{colors.chart-3}"
  chart-series-4:
    backgroundColor: "{colors.chart-4}"
  chart-series-5:
    backgroundColor: "{colors.chart-5}"
  chart-series-6:
    backgroundColor: "{colors.chart-6}"
---

## Overview

This file is the single source of truth for how Tieto looks on a slide. It exists so that any AI agent, regardless of tool, builds presentations that are unmistakably Tieto.

Read it in two layers. The YAML front matter holds the exact values, the design tokens, and those are non negotiable. The prose below explains the intent behind each value and how to apply it. When a token and instinct disagree, the token wins.

How to use it: pull colors, typography, spacing and component recipes straight from the tokens. Resolve references like `{colors.primary}` to their actual values. Apply the component definitions verbatim. Treat the prose as rationale, not as decoration.

The Tieto deck system is calm, confident and corporate, carried by deep navy with a single electric signal color. The template ships these slide families: Cover, Speaker, Chapter, Content (one to six columns), Agenda, Quote, and End. The components below map to that vocabulary. Presentations are built in 16:9.

Logo usage: the white logotype goes on navy and other dark or busy backgrounds, the blue logotype goes on white and light backgrounds. Keep clear space around it and never recolor it.

## Colors

The palette runs on deep navy and warm neutrals, with one deliberate signal color.

- **Primary (#021E57):** Tieto deep navy. The anchor. Covers, chapters, end slides, headings and key text. Same value as the logotype.
- **Ink (#272A2C):** Near-black for body text on light surfaces. Softer than pure black.
- **Background (#FFFFFF):** The base surface for content slides.
- **Surface (#D2D0CB):** Warm light grey for panels, quote slides and alternating table rows.
- **Secondary (#78716E):** Warm grey for supporting text, rules and metadata.
- **Accent (#F5FF56):** Signal yellow. The single pop color. One highlight per slide, never as a background wash behind text.
- **Blue-700, blue-500, blue-300 (#3531CF, #4E60E7, #839DF9):** The blue family for emphasis, links, diagram fills and gradients of data.
- **On-primary, on-accent, on-surface, on-background:** Text colors that keep contrast safe. White on navy, navy on yellow.
- **Divider (#D2D0CB):** Hairlines and separators.
- **Chart-1 through chart-6:** The data palette. Apply in numeric order so the same series keeps the same color across the whole deck.

Never set the accent yellow as a text color, it fails contrast at any size. Reserve yellow for fills, markers and the one thing that must be seen first. Keep all text to background pairings above WCAG AA (4.5:1).

## Typography

Tieto Sans is the single typeface across the entire system. Tieto Numerals is used only for large standout figures. Sizes are stored in px so the file validates cleanly. PowerPoint measures in points, so convert with pt = px multiplied by 0.75 (for example 24px is 18pt, 80px is 60pt).

- **Slide-title:** Cover and end slides. Bold and certain.
- **Section-header:** Chapter dividers that mark a new part.
- **Subtitle:** The light supporting line on covers and speaker slides, for example date, event or presenter.
- **Heading:** The headline at the top of a content slide, Medium weight.
- **Body:** Standard running text, Regular weight.
- **Bullet:** Bullet lists. Three levels maximum.
- **Kpi-number:** Large headline figures in Tieto Numerals.
- **Data-label:** Chart labels and metric captions.
- **Kicker:** A small uppercase line above a heading. It adds structure and rhythm.
- **Quote:** Quote slides, set light for air.
- **Caption:** Image captions and source lines.
- **Footer:** Footer and page numbers.

Use Tieto Sans only. Vary weight and size, never the typeface. If Tieto Sans is unavailable in the rendering environment, fall back to a neutral grotesque sans (for example Inter, Helvetica or Arial) and flag the substitution.

## Layout

Slides are 16:9, 33.87 x 19.05 cm.

- **Slide-margin:** A fixed margin around all content. Nothing crosses it.
- **Content-gap:** The space between blocks on the same slide.
- **Block-padding:** The inner padding of boxes and panels.

Build on the template grid. Left align headings and text. Center only on Cover, Chapter, Quote and End slides. The column layouts (two to six) split the content area evenly with one content-gap between columns.

## Elevation & Depth

Keep the surface flat. Avoid heavy shadows and 3D effects. Depth comes from the color step between background and surface, and from the navy blocks, not from drop shadows. If a faint lift is needed on a panel, keep the shadow soft and low.

## Shapes

Corner radii stay small and consistent. Panels and callouts use `rounded.md`. Tags and small markers may use `rounded.sm`. Keep most blocks square cornered to match the template. Avoid fully rounded shapes, they do not belong to the system.

## Components

These components cover everything a complete Tieto deck needs and map to the template families.

- **cover-slide:** The opener. Navy background, large title, room for the white logotype and a subtitle.
- **speaker-slide:** Presenter intro on navy, name and role in the subtitle style.
- **chapter-slide:** The break between parts. Navy background with the section title.
- **content-slide:** The workhorse. White background, heading on top, content below.
- **slide-header:** The heading row on a content slide.
- **kicker-label:** A small blue uppercase line above the heading.
- **bullet-list:** A bullet list in body style.
- **agenda-item:** A single line in an agenda or contents slide.
- **callout-box:** A highlighted panel on the warm surface for one key point.
- **callout-box-accent:** The loud variant on signal yellow with navy text. One per slide, used sparingly.
- **callout-box-navy:** A navy panel with white text for emphasis without using yellow.
- **kpi-stat / kpi-label:** A headline figure in Tieto Numerals with its caption. The number leads, the label supports.
- **column-panel:** A panel for the two to six column layouts.
- **table-header:** The header row, navy background.
- **table-row / table-row-alt:** Rows alternate between background and surface for readability.
- **quote-slide:** A quote on the warm surface, navy text.
- **image-caption:** The caption under an image or chart.
- **footer / page-number:** Footer furniture in muted grey.
- **end-slide:** The closing slide on navy, mirrors the cover.
- **body-text:** Default running text in ink on light surfaces.
- **link-inline:** An inline link or interactive word, set in brand blue.
- **tag-info:** A small rounded tag or chip on light blue with navy text.
- **divider-rule:** A one pixel hairline in the divider grey.
- **icon-default / icon-on-navy / icon-accent:** The icon set rendered in navy, in white on dark backgrounds, or in brand blue. Icons are 48 by 48.
- **chart-series-1 through chart-series-6:** Fill colors for data series, applied in numeric order so each series keeps its color across the deck.

Allowed component properties: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`.

## Do's and Don'ts

**Do**

- One idea per slide.
- Carry the deck on navy and white, and let yellow appear once per slide as the spotlight.
- Use Tieto Numerals for the big figures, Tieto Sans for everything else.
- Keep bullet lists short, ideally under six points.
- Apply the chart palette in numeric order.
- Put the white logo on navy and the blue logo on white.

**Don't**

- Use the yellow accent as text or as a full background behind copy.
- Use any typeface other than Tieto Sans (and Tieto Numerals for figures).
- Add heavy shadows, 3D or decorative effects.
- Recolor, stretch or crowd the logotype.
- Let content cross the slide margin.

## Logo

The Tieto logotype ships in two color versions. The aspect ratio is fixed at roughly 2.09 to 1, never stretch or distort it.

- **Blue logotype (#021E57):** For white and light backgrounds.
- **White logotype:** For navy, dark or photographic backgrounds where the blue would not read.

Clear space: keep a margin around the logotype on all sides equal to at least half the logotype height, and more where possible. Nothing, no text, image edge or shape, enters that zone.

Placement on slides: the logotype sits in a consistent corner across the deck, typically top left on content slides and centered on the cover. The favicon (square mark) is for small contexts such as browser tabs and avatars, not for slide branding.

Do not recolor the logotype, add effects, place it on a low contrast background, or crowd it. When in doubt, use the white version on navy.

## Iconography

The kit includes a set of 67 line icons drawn on a 48 by 48 grid in a single consistent stroke style. Use them to support content, never as decoration for its own sake.

- **Color:** Icons inherit a single color. Render them in navy on light backgrounds, in white on navy, or in brand blue for an active or highlighted state. Never fill an icon with the yellow accent.
- **Size:** Keep icons at a consistent size within a slide. The native grid is 48 by 48, scale proportionally.
- **Pairing:** One icon per idea. When pairing an icon with a KPI or a column heading, align it to the same baseline and keep spacing even.
- **Available icons (selection):** Ai, Cloud 2, Server 2, Shield, Security system, Internet of things, People network, Handshake, Rocket, Target 3, Trend, Chart line, Chart column, Pie chart, Coins, Credit card, Bank 2, Trophy, Light bulb 2, Compass, Connect, Link, Lock and others. The full set covers technology, business, finance, communication and navigation themes.

Do not redraw, recolor into gradients, or mix the Tieto icons with icons from another library. Consistency of stroke and grid is what keeps them on brand.
