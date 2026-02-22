<template>
  <!--
    TEMPLATE = UI STRUCTURE LAYER

    Python analogy:
    - Think of this like a tiny declarative view description instead of print statements.
    - `{{ ... }}` is expression interpolation (like f-strings, but in HTML context).

    C analogy:
    - This is not imperative drawing code; it's a declarative "what the UI should be" tree.
    - Vue performs the efficient DOM updates when bound data changes.
  -->
  <section class="walkthrough-card">
    <h2>{{ title }}</h2>

    <!-- v-model = two-way binding for form inputs -->
    <label>
      Name:
      <input v-model="name" type="text" placeholder="Type your name" />
    </label>

    <!-- Event binding with @click -->
    <button @click="increment">Clicked {{ count }} times</button>

    <!-- Computed property usage -->
    <p>{{ greeting }}</p>

    <!-- Conditional rendering -->
    <p v-if="count >= 5">You clicked 5 or more times.</p>
    <p v-else>Keep clicking to reach 5.</p>
  </section>
</template>

<script>
/*
  SCRIPT = BEHAVIOR + STATE LAYER

  Python analogy:
  - `data()` is like initializing instance attributes in __init__.
  - `methods` are like instance methods.
  - `computed` is like a read-only @property derived from state.

  C analogy:
  - `data` is your mutable state struct.
  - `methods` are functions that mutate/read that state.
  - `computed` is derived value (recomputed based on dependencies).
*/
export default {
  name: 'VueSfcWalkthrough',

  // data() returns component-local state.
  data: function () {
    return {
      title: 'Annotated Vue SFC Walkthrough',
      name: 'World',
      count: 0
    };
  },

  // computed values are derived from state and cached by Vue until dependencies change.
  computed: {
    greeting: function () {
      return 'Hello, ' + this.name + ' 👋';
    }
  },

  // methods are event handlers or imperative actions.
  methods: {
    increment: function () {
      this.count += 1;
    }
  }
};
</script>

<style scoped>
/*
  STYLE = PRESENTATION LAYER

  `scoped` means Vue rewrites selectors so they apply only to this component.
  Useful for avoiding accidental global CSS collisions.
*/
.walkthrough-card {
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  padding: 16px;
  background: #fff;
  max-width: 520px;
}

label {
  display: inline-block;
  margin: 10px 0;
}

input {
  margin-left: 8px;
  padding: 6px 8px;
}

button {
  margin-top: 8px;
  padding: 6px 10px;
  cursor: pointer;
}
</style>
