# Vue 2 Reactive Playground

A minimal Vue.js 2 project (Webpack-based) for learning and adding small example components.

## Tooling used in this project

Administrative/runtime tools used:

- Node.js: JavaScript runtime used to run build/dev tools
- npm: default package manager that ships with Node.js
- Yarn (optional): alternative package manager you can use instead of npm
- Webpack: bundles application code
- webpack-dev-server: local development server with hot reload
- http-server: serves static files from `dist/`

## Package manager options (npm vs Yarn)

- You can use either npm or Yarn for this project.
- Do not mix lockfiles long-term (`package-lock.json` vs `yarn.lock`) if you want reproducible installs.
- In this repo, commands are documented for both, but npm works out-of-the-box.

How Yarn fits in:

- Yarn does the same core job as npm: install dependencies and run scripts.
- Yarn command equivalents:
	- `npm install` ↔ `yarn install`
	- `npm run dev` ↔ `yarn dev`
	- `npm run build` ↔ `yarn build`
	- `npm run serve` ↔ `yarn serve`

## Packages installed in this project

Application dependency:

- `vue@^2.7.16`

Development dependencies:

- `webpack@^4.46.0`
- `webpack-cli@^3.3.12`
- `webpack-dev-server@^3.11.3`
- `vue-loader@^15.10.2`
- `vue-template-compiler@^2.7.16`
- `html-webpack-plugin@^4.5.2`
- `style-loader@^2.0.0`
- `css-loader@^5.2.7`
- `http-server@^14.1.1`

Install all packages with Yarn:

```bash
yarn install
```

Install one package at a time with Yarn:

```bash
yarn add vue@^2.7.16
yarn add -D webpack@^4.46.0 webpack-cli@^3.3.12 webpack-dev-server@^3.11.3 vue-loader@^15.10.2 vue-template-compiler@^2.7.16 html-webpack-plugin@^4.5.2 style-loader@^2.0.0 css-loader@^5.2.7 http-server@^14.1.1
```

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
- JavaScript/TypeScript syntax reference snippets: `snippets.ts`
- Debugging playbook and mindset glossary: `error-glossary.md`
- Daily debugging behaviors: `top-10-debugging-habits.md`
- Annotated single-file component walkthrough: `vue-sfc-walkthrough.vue`

You can split additional demos into new components under `src/components/` and import them into `App.vue`.

## Function-level documentation in source files

Function/method comments are included in:

- `src/main.js`
- `src/App.vue`
- `src/components/PropsEventsDemo.vue`
- `src/components/ComputedWatchDemo.vue`
- `src/components/ConditionalListDemo.vue`

These comments describe each function's purpose and how state/data flows through it.

## How to read a .vue file (beginner primer)

A Vue Single File Component (SFC) typically has three top-level blocks:

- `<template>`: structure (HTML-like markup)
- `<script>`: behavior (state, methods, computed, watchers)
- `<style>`: presentation (CSS)

You can think of it as: **what it looks like** + **how it behaves** + **how it is styled**.

### Common tags you will see often

- `<div>`: generic layout container
- `<section>`: semantic grouped section
- `<h1>`, `<h2>`: headings
- `<p>`: paragraph text
- `<label>` + `<input>`: form pairing
- `<button>`: clickable action
- `<ul>` + `<li>`: unordered lists
- `<strong>`: emphasized/important inline text

### What `<style scoped>` means

- `scoped` tells Vue to scope those CSS rules to this component only.
- Under the hood, Vue rewrites selectors so styles do not leak globally.
- Use scoped styles for component-local UI.
- Use non-scoped styles when you intentionally want global styling.

### CSS selector syntax you will see

- `.className` → selects elements by class
- `#idName` → selects element by id
- `tagname` (for example `button`) → selects by tag
- `.parent .child` → descendant selector
- `.tab-btn.active` → element that has both classes
- `input[type="number"]` → attribute selector

### Why a period appears in different places

- In CSS, `.` means class selector (`.demo-card`).
- In JavaScript, `.` means property access (`this.count`).

Same symbol, different language context.

## How to use snippets.ts

Use `snippets.ts` as a reference-first learning file.

Suggested order (beginner → advanced):

1. Basic function definitions
2. Parameters and return patterns
3. Objects, arrays, tuples
4. Conditionals and switch
5. Loops and array helpers (`map`, `filter`, `reduce`)
6. Type aliases, unions, intersections
7. Classes and generics
8. Async/await and Promise patterns
9. Null handling (`?.` and `??`)
10. Vue 2 specific patterns (directives, events, component communication)
11. Vue navigation patterns (no-router option vs vue-router option)
12. Error recognition and debugging mindset (`error-glossary.md`)
13. Daily debugging habits (`top-10-debugging-habits.md`)
14. Annotated SFC walkthrough (`vue-sfc-walkthrough.vue`)

How to practice with it:

- Copy one section into a temporary `.ts` file and modify values.
- Predict output before running, then verify.
- Rewrite one function in another style (for example: declaration → arrow).
- Add one custom example per section to make it your own reference.

Quick challenge path:

- Beginner: change array examples and log the results.
- Intermediate: add a new union type and update one function to use it.
- Advanced: create a small typed workflow that combines generics + async + error handling.
