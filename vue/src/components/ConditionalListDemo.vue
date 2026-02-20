<template>
  <section class="demo-card">
    <h2>Conditional + List Demo</h2>

    <div class="controls">
      <label>
        New item:
        <input v-model="newItem" type="text" placeholder="Add a task" />
      </label>
      <button @click="addItem">Add</button>
      <button @click="showList = !showList">
        {{ showList ? 'Hide list' : 'Show list' }}
      </button>
    </div>

    <p v-if="items.length === 0">No items yet.</p>

    <ul v-if="showList && items.length > 0">
      <li v-for="item in items" :key="item.id">
        {{ item.text }}
      </li>
    </ul>

    <p v-else-if="!showList">List is hidden.</p>
  </section>
</template>

<script>
export default {
  name: 'ConditionalListDemo',
  data: function () {
    return {
      newItem: '',
      showList: true,
      nextId: 3,
      items: [
        { id: 1, text: 'Learn v-if / v-else-if' },
        { id: 2, text: 'Learn v-for rendering' }
      ]
    };
  },
  methods: {
    addItem: function () {
      var trimmed = this.newItem.trim();
      if (!trimmed) {
        return;
      }

      this.items.push({ id: this.nextId, text: trimmed });
      this.nextId += 1;
      this.newItem = '';
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

.controls {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
}

input {
  margin-left: 8px;
  padding: 6px 8px;
}

button {
  padding: 6px 10px;
  cursor: pointer;
}

ul {
  margin: 12px 0 0;
  padding-left: 18px;
}
</style>
