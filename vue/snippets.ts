/*
  snippets.ts
  Purpose: quick syntax reference for JavaScript + TypeScript constructs used in this repo
  Notes:
  - This file is for learning/reference only and is not imported by the Vue app.
*/

// ---------------------------------
// 0) Decision cheatsheet (what to open when)
// ---------------------------------

// This is different from a table of contents:
// - TOC tells you where things are.
// - Decision cheatsheet tells you what to use for a specific problem.

// If you need to define reusable behavior -> start at section 1.
// If your function call sites feel messy -> section 2.
// If your data shape is unclear -> section 3.
// If branching logic is getting hard to follow -> section 4.
// If you're transforming collections -> section 5.
// If your types feel repetitive or too loose -> section 6.
// If values should come from a fixed set -> section 7.
// If state + behavior should stay bundled -> section 8.
// If one algorithm should work for many types safely -> section 9.
// If logic involves network/timers/promises -> section 10.
// If undefined/null data causes runtime errors -> section 11.
// If you need better lookup/uniqueness structures -> section 12.
// If failures need controlled handling -> section 13.
// If building Vue 2 components/patterns -> section 14.
// If choosing app navigation strategy -> section 15.
// If deciding what to expose from this file -> section 16.

// ---------------------------------
// 1) Basic function definitions
// ---------------------------------

// Used for: defining reusable behavior with named/function-expression/arrow styles.
// Solves: copy/paste logic and unclear intent by centralizing behavior into callable units.
// Mindset: choose readability first; pick one style consistently unless syntax needs differ.

// Named function declaration.
function add(a: number, b: number): number {
  return a + b;
}

// Anonymous function expression assigned to a const.
const multiply = function (a: number, b: number): number {
  return a * b;
};

// Arrow function (short form and explicit return).
const square = (value: number): number => value * value;
const divide = (a: number, b: number): number => {
  if (b === 0) {
    throw new Error('Cannot divide by zero');
  }
  return a / b;
};

// ---------------------------------
// 2) Parameters and return patterns
// ---------------------------------

// Used for: controlling function inputs (optional/default/rest) and output typing.
// Solves: brittle call sites and argument-count confusion.
// Mindset: design function signatures as mini APIs with safe defaults.

// Optional parameter (?) and default parameter (=).
function greet(name: string = 'World', punctuation?: string): string {
  const suffix = punctuation ? punctuation : '!';
  return `Hello, ${name}${suffix}`;
}

// Rest parameters gather remaining arguments into an array.
function sumAll(...values: number[]): number {
  return values.reduce((total, value) => total + value, 0);
}

// ---------------------------------
// 3) Objects, arrays, and tuples
// ---------------------------------

// Used for: modeling structured data (objects), collections (arrays), and fixed-shape pairs (tuples).
// Solves: loose data handling by making shape/intent explicit.
// Mindset: pick the narrowest shape that matches real constraints.

interface User {
  id: number;
  name: string;
  isAdmin: boolean;
}

const user: User = {
  id: 1,
  name: 'Kurt',
  isAdmin: false
};

// Array of numbers.
const numbers: number[] = [1, 2, 3, 4, 5];

// Tuple: fixed length and type order.
const point2D: [number, number] = [10, 20];

// Spread copies/combines arrays and objects.
const moreNumbers = [...numbers, 6, 7];
const updatedUser = { ...user, isAdmin: true };

// Destructuring pulls values out by position/key.
const [firstNumber, secondNumber] = numbers;
const { name: userName, isAdmin } = updatedUser;

// ---------------------------------
// 4) Conditionals and switch
// ---------------------------------

// Used for: branching behavior based on state or input values.
// Solves: unclear control flow by making decision logic explicit.
// Mindset: prefer simple, exhaustive branches over clever one-liners.

function roleLabel(role: 'viewer' | 'editor' | 'admin'): string {
  switch (role) {
    case 'viewer':
      return 'Read-only access';
    case 'editor':
      return 'Can edit content';
    case 'admin':
      return 'Full access';
    default:
      return 'Unknown role';
  }
}

const accessMessage = isAdmin ? 'Admin access enabled' : 'Standard access';

// ---------------------------------
// 5) Loops and iteration helpers
// ---------------------------------

// Used for: traversing and transforming collections.
// Solves: manual repetitive logic and ad-hoc aggregation code.
// Mindset: use `map/filter/reduce` for transformations; loops for side-effect-heavy flows.

for (let i = 0; i < numbers.length; i += 1) {
  // Classic index-based loop.
  const value = numbers[i];
  void value;
}

for (const value of numbers) {
  // for..of iterates array values.
  void value;
}

numbers.forEach((value, index) => {
  // forEach runs a callback for each item.
  void value;
  void index;
});

const evenNumbers = numbers.filter((value) => value % 2 === 0);
const doubledNumbers = numbers.map((value) => value * 2);
const totalNumbers = numbers.reduce((total, value) => total + value, 0);

// ---------------------------------
// 6) Type aliases, unions, intersections
// ---------------------------------

// Used for: naming complex types and composing multiple type possibilities.
// Solves: duplicated or hard-to-read type signatures across code.
// Mindset: model real-world variability explicitly instead of using `any`.

// Type alias: gives a reusable name to a type expression.
// Here, Id can be either a string or a number.
type Id = string | number;

// Generic type alias:
// - `<T>` declares a type parameter named T.
// - It looks template-like, but this is type parameterization (not string templating).
// - T is just a placeholder chosen by the author; it is not built in.
// - You can rename it to something clearer (for example `<DataType>`).
type ApiSuccess<T> = {
  ok: true;
  data: T;
};

type ApiFailure = {
  ok: false;
  error: string;
};

// Generic union:
// - Success branch carries `data: T`
// - Failure branch carries `error: string`
type ApiResult<T> = ApiSuccess<T> | ApiFailure;

// Examples of "where T comes from":
// You provide T at usage time by writing ApiSuccess<SomeType>.
type ExampleStringSuccess = ApiSuccess<string>;
type ExampleUserSuccess = ApiSuccess<User>;
type ExampleNumberArrayResult = ApiResult<number[]>;

type Timestamped = {
  createdAt: Date;
};

type UserWithTimestamp = User & Timestamped;

function parseId(id: Id): string {
  return String(id);
}

// ---------------------------------
// 7) Enums and literal unions
// ---------------------------------

// Used for: constraining values to a small known set.
// Solves: typo-prone string values and inconsistent status/level vocabularies.
// Mindset: make invalid states unrepresentable with narrow value sets.

enum LogLevel {
  Info = 'info',
  Warn = 'warn',
  Error = 'error'
}

function logMessage(level: LogLevel, message: string): void {
  // Backticks (`...`) create a template literal string.
  // `${...}` injects expressions into that string.
  // This solves string concatenation noise and improves readability.
  console.log(`[${level}] ${message}`);
}

// ---------------------------------
// 8) Classes and access modifiers
// ---------------------------------

// Used for: bundling related state + behavior with visibility rules (`private`, etc).
// Solves: scattered state mutation by centralizing invariants in methods.
// Mindset: use classes when object identity/lifecycle matters; otherwise prefer plain functions/objects.

class Counter {
  private count: number;

  constructor(initialValue: number = 0) {
    this.count = initialValue;
  }

  increment(step: number = 1): void {
    this.count += step;
  }

  getValue(): number {
    return this.count;
  }
}

// ---------------------------------
// 9) Generics
// ---------------------------------

// Used for: writing reusable typed logic without losing type safety.
// Solves: duplicate implementations for different types and overuse of `any`.
// Mindset (use): when algorithm is identical across types but shape should remain precise.
// Mindset (avoid): when only one concrete type is ever expected (keep it simple then).

function identity<T>(value: T): T {
  return value;
}

function firstItem<T>(items: T[]): T | undefined {
  return items[0];
}

const firstUser = firstItem<User>([user]);
void firstUser;

// ---------------------------------
// 10) Async/await and Promise
// ---------------------------------

// Used for: modeling asynchronous work (network, timers, file/IO operations).
// Solves: callback nesting and unreadable async control flow.
// Mindset: treat async flows as data pipelines with explicit success/failure handling.

function wait(ms: number): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function fetchGreeting(): Promise<string> {
  await wait(50);
  return 'Hello from async function';
}

async function runAsyncExample(): Promise<void> {
  try {
    const message = await fetchGreeting();
    console.log(message);
  } catch (error) {
    console.error('Async example failed:', error);
  }
}

// ---------------------------------
// 11) Null handling and optional chaining
// ---------------------------------

// Used for: safely reading potentially missing values and setting sensible fallbacks.
// Solves: runtime crashes from null/undefined access.
// Mindset: assume incomplete data at boundaries and guard intentionally.

type Settings = {
  theme?: {
    mode?: 'light' | 'dark';
  };
};

const settings: Settings = {};

// Optional chaining safely traverses nested optional properties.
const themeMode = settings.theme?.mode;

// Nullish coalescing provides fallback for null/undefined only.
const resolvedTheme = themeMode ?? 'light';
void resolvedTheme;

// ---------------------------------
// 12) Map/Set examples
// ---------------------------------

// Used for: keyed lookup collections (`Map`) and uniqueness constraints (`Set`).
// Solves: O(n) repeated array scans and duplicate-value bugs.
// Mindset: pick data structures for access pattern, not habit.

const countsByWord = new Map<string, number>();
countsByWord.set('vue', 2);
countsByWord.set('typescript', 1);

const uniqueTags = new Set<string>(['vue', 'typescript', 'vue']);
void countsByWord;
void uniqueTags;

// ---------------------------------
// 13) Try/catch/finally
// ---------------------------------

// Used for: controlled error handling around risky operations.
// Solves: uncaught exceptions that crash flows without context.
// Mindset: fail predictably; log actionable context; recover when appropriate.

function parseJsonSafely(jsonText: string): unknown {
  try {
    return JSON.parse(jsonText);
  } catch (error) {
    console.error('Invalid JSON:', error);
    return null;
  } finally {
    // finally runs whether parsing succeeded or failed.
    console.log('parseJsonSafely completed');
  }
}

// ---------------------------------
// 14) Vue 2 specific patterns
// ---------------------------------

// Used for: Vue 2 component architecture (Options API, directives, events, slots).
// Solves: inconsistent component communication and state ownership.
// Mindset: props down, events up, and keep each component focused.

// Vue 2 uses the Options API with `data` as a function that returns per-instance state.
const vue2OptionsApiSnippet = `
export default {
  name: 'ExampleComponent',
  props: {
    start: {
      type: Number,
      default: 0
    }
  },
  data: function () {
    return {
      count: this.start,
      message: 'Hello Vue 2'
    };
  },
  computed: {
    doubled: function () {
      return this.count * 2;
    }
  },
  watch: {
    count: function (nextValue, previousValue) {
      console.log('count changed', previousValue, '->', nextValue);
    }
  },
  methods: {
    increment: function () {
      this.count += 1;
    }
  },
  created: function () {
    console.log('component created');
  },
  mounted: function () {
    console.log('component mounted in DOM');
  }
};
`;

// Template directives commonly used in Vue 2 components.
const vue2TemplateDirectiveSnippet = `
<template>
  <section>
    <p v-if="isVisible">Now you see me</p>
    <p v-else>Now hidden</p>

    <ul>
      <li v-for="item in items" :key="item.id">{{ item.label }}</li>
    </ul>

    <input v-model="message" type="text" />
    <button @click="submit" :disabled="isSaving">Save</button>

    <p :class="{ active: isActive }" :style="{ color: textColor }">
      Dynamic class/style binding
    </p>
  </section>
</template>
`;

// Vue 2 custom component `v-model` convention uses `value` prop + `input` event.
const vue2ComponentVModelSnippet = `
export default {
  name: 'TextInput',
  props: {
    value: {
      type: String,
      default: ''
    }
  },
  methods: {
    onInput: function (event) {
      this.$emit('input', event.target.value);
    }
  },
  template: \
    '<input :value="value" @input="onInput" type="text" />'
};

// Parent usage:
// <TextInput v-model="username" />
`;

// Props-down, events-up pattern for parent/child communication.
const vue2PropsEventsSnippet = `
// Child:
this.$emit('saved', { id: 1, title: 'Post' });

// Parent template:
// <ChildComponent :post-id="activePostId" @saved="handleSaved" />
`;

// Scoped slots in Vue 2 use slot-scope syntax.
const vue2ScopedSlotSnippet = `
<!-- child -->
<slot :user="user"></slot>

<!-- parent -->
<ChildComponent>
  <template slot-scope="slotProps">
    {{ slotProps.user.name }}
  </template>
</ChildComponent>
`;

// Dynamic components with optional keep-alive cache.
const vue2DynamicComponentSnippet = `
<keep-alive>
  <component :is="activeView"></component>
</keep-alive>
`;

// Key modifiers and event modifiers are common Vue 2 template patterns.
const vue2EventModifierSnippet = `
<form @submit.prevent="save">
  <input @keyup.enter="save" />
  <button @click.stop="openMenu">Open</button>
</form>
`;

// ---------------------------------
// 15) Navigation pattern: no vue-router vs vue-router
// ---------------------------------

// Used for: choosing app navigation strategy based on complexity and URL needs.
// Solves: overengineering tiny apps or underengineering growing ones.
// Mindset: start minimal, switch to router when URL-state and route lifecycle become requirements.

// No-vue-router option:
// - Best for very small apps, demos, or internal tools.
// - Uses local component/app state to switch views.
// - Zero extra dependency and straightforward setup.
// - Tradeoff: no URL-based navigation/history by default.
const vue2NoRouterNavigationSnippet = `
<template>
  <div>
    <button @click="activeView = 'home'">Home</button>
    <button @click="activeView = 'about'">About</button>

    <HomeView v-if="activeView === 'home'" />
    <AboutView v-else-if="activeView === 'about'" />
  </div>
</template>

<script>
import HomeView from './HomeView.vue';
import AboutView from './AboutView.vue';

export default {
  name: 'AppWithoutRouter',
  components: { HomeView, AboutView },
  data: function () {
    return {
      activeView: 'home'
    };
  }
};
</script>
`;

// Vue-router option:
// - Best when you need shareable URLs, browser history, route guards, nested routes.
// - Adds router setup and route mapping, but scales much better for multi-page apps.
const vue2VueRouterNavigationSnippet = `
// router.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from './HomeView.vue';
import AboutView from './AboutView.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: HomeView },
    { path: '/about', component: AboutView }
  ]
});

// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';

new Vue({
  router,
  render: function (h) {
    return h(App);
  }
}).$mount('#app');

// App.vue
// <router-link to="/">Home</router-link>
// <router-link to="/about">About</router-link>
// <router-view />
`;

// Side-by-side guidance:
// - Choose no-router when your app has a few pseudo-pages and you want minimal setup.
// - Choose vue-router when URL state, deep linking, and navigation scalability matter.
const vue2RoutingDecisionNotes = `
No vue-router:
- Pros: minimal setup, fast to start, great for demos/MVPs.
- Cons: no built-in URL state, hard to scale navigation complexity.

With vue-router:
- Pros: proper route management, shareable links, browser navigation support.
- Cons: additional dependency and setup overhead.
`;

// No-vue-router with hash fragment option:
// - Adds URL-like navigation state without pulling in vue-router.
// - Good middle ground for tiny apps that still need bookmarkable pseudo-pages.
// - Tradeoff: manual hash parsing and less robust routing features.
const vue2HashNoRouterSnippet = `
<template>
  <div>
    <a href="#/home">Home</a>
    <a href="#/about">About</a>

    <HomeView v-if="activeHashRoute === '/home'" />
    <AboutView v-else-if="activeHashRoute === '/about'" />
    <NotFoundView v-else />
  </div>
</template>

<script>
import HomeView from './HomeView.vue';
import AboutView from './AboutView.vue';
import NotFoundView from './NotFoundView.vue';

function normalizeHashRoute() {
  var raw = window.location.hash.replace(/^#/, '');
  return raw || '/home';
}

export default {
  name: 'HashNavigationWithoutRouter',
  components: { HomeView, AboutView, NotFoundView },
  data: function () {
    return {
      activeHashRoute: normalizeHashRoute()
    };
  },
  created: function () {
    this.handleHashChange = this.syncRouteFromHash.bind(this);
    window.addEventListener('hashchange', this.handleHashChange);
  },
  beforeDestroy: function () {
    window.removeEventListener('hashchange', this.handleHashChange);
  },
  methods: {
    syncRouteFromHash: function () {
      this.activeHashRoute = normalizeHashRoute();
    }
  }
};
</script>
`;

// ---------------------------------
// 16) Module exports
// ---------------------------------

// Used for: exposing selected symbols for import in other files.
// Solves: accidental globals and unclear module boundaries.
// Mindset: export intentionally; keep module surface area small and purposeful.

export {
  add,
  multiply,
  square,
  divide,
  greet,
  sumAll,
  roleLabel,
  parseId,
  logMessage,
  Counter,
  identity,
  firstItem,
  wait,
  fetchGreeting,
  runAsyncExample,
  parseJsonSafely,
  numbers,
  moreNumbers,
  evenNumbers,
  doubledNumbers,
  totalNumbers,
  user,
  updatedUser,
  point2D,
  accessMessage,
  vue2OptionsApiSnippet,
  vue2TemplateDirectiveSnippet,
  vue2ComponentVModelSnippet,
  vue2PropsEventsSnippet,
  vue2ScopedSlotSnippet,
  vue2DynamicComponentSnippet,
  vue2EventModifierSnippet,
  vue2NoRouterNavigationSnippet,
  vue2VueRouterNavigationSnippet,
  vue2RoutingDecisionNotes,
  vue2HashNoRouterSnippet
};
