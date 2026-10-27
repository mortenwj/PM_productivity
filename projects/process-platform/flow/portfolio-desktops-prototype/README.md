# Flow portfolio & reporting — clickable prototype

Local **Vite + React** prototype for manager **worklists**, **portfolio desktops**, and **reporting** in the 360° Flow story.

See [SCOPE.md](./SCOPE.md) for problem framing, screen list, and open questions.

## Run locally

```powershell
cd projects/process-platform/flow/portfolio-desktops-prototype
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`).

```powershell
npm run build    # production build
npm run preview  # preview production build
```

## Project layout

| Path | Purpose |
|------|---------|
| `SCOPE.md` | What we are exploring and why |
| `src/data/mockPortfolio.ts` | Sample cases, metrics, filters |
| `src/screens/` | Worklist, Portfolio, Reporting, Case detail |
| `src/components/` | Shell, navigation, shared UI |

## Iteration workflow

1. Adjust mock data in `src/data/mockPortfolio.ts` to match a customer scenario.
2. Change screen behaviour in `src/screens/`.
3. Capture decisions and deltas in `SCOPE.md` or a dated note under `../` Flow docs.
