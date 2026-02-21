<template>
  <section class="demo-card">
    <h2>Computed + Watch Demo</h2>

    <label>
      Temperature (°C):
      <input v-model.number="celsius" type="number" />
    </label>

    <p>Computed Fahrenheit: <strong>{{ fahrenheit }}</strong>°F</p>
    <p>Watch log: {{ watchLog }}</p>
  </section>
</template>

<script>
export default {
  name: 'ComputedWatchDemo',
  data: function () {
    // Holds raw input and a readable log produced by the watcher.
    return {
      celsius: 20,
      watchLog: 'Waiting for change...'
    };
  },
  computed: {
    // Converts Celsius input to Fahrenheit and formats to one decimal place.
    fahrenheit: function () {
      return ((this.celsius * 9) / 5 + 32).toFixed(1);
    }
  },
  watch: {
    // Records transitions whenever the source value changes.
    celsius: function (nextValue, prevValue) {
      this.watchLog = 'celsius changed from ' + prevValue + ' to ' + nextValue;
    }
  }
};
</script>

<style scoped>
.demo-card {
  border: 1px solid #e7e7e7;
  border-radius: 8px;
  padding: 16px;
  background: #fff;
}

input {
  margin-left: 8px;
  padding: 6px 8px;
  width: 120px;
}
</style>
