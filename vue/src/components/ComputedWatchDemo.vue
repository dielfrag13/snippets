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
    return {
      celsius: 20,
      watchLog: 'Waiting for change...'
    };
  },
  computed: {
    fahrenheit: function () {
      return ((this.celsius * 9) / 5 + 32).toFixed(1);
    }
  },
  watch: {
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
