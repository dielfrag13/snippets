# Vue 2 Reactive Playground

A minimal Vue.js 2 project (Webpack-based) for learning and adding small example components.

## Prerequisites

- Node.js (you already have `v20.x`)
- npm (already installed)
- Optional: Yarn

## Install Yarn on Linux

You have a few options:

### Option A: npm global install (common)

```bash
npm install -g yarn
```

### Option B: Corepack (Node-managed Yarn)

```bash
corepack enable
corepack prepare yarn@1.22.22 --activate
yarn -v
```

If `corepack enable` fails with permissions, run with elevated privileges:

```bash
sudo corepack enable
```

## Install dependencies

Using Yarn:

```bash
yarn install
```

Using npm:

```bash
npm install
```

## Run in development (hot reload)

Using Yarn:

```bash
yarn dev
```

Using npm:

```bash
npm run dev
```

Open: `http://localhost:8080`

## Compile production build

Using Yarn:

```bash
yarn build
```

Using npm:

```bash
npm run build
```

Output is generated in `dist/`.

## Serve compiled output

Using Yarn:

```bash
yarn serve
```

Using npm:

```bash
npm run serve
```

Open: `http://localhost:8080`

## Where to add more examples

- Main app entry: `src/main.js`
- Current example component: `src/App.vue`

You can split additional demos into new components under `src/components/` and import them into `App.vue`.
