<template>
  <section class="demo-card">
    <h2>Props + Events Demo</h2>
    <p>
      Parent value:
      <strong>{{ parentMessage }}</strong>
    </p>

    <child-editor
      :initial-message="parentMessage"
      @message-change="onMessageChange"
    />
  </section>
</template>

<script>
var ChildEditor = {
  name: 'ChildEditor',
  props: {
    initialMessage: {
      type: String,
      default: ''
    }
  },
  data: function () {
    return {
      localValue: this.initialMessage
    };
  },
  watch: {
    initialMessage: function (nextValue) {
      this.localValue = nextValue;
    }
  },
  methods: {
    emitChange: function () {
      this.$emit('message-change', this.localValue);
    }
  },
  template: `
    <div class="child-box">
      <label>
        Child input:
        <input v-model="localValue" type="text" placeholder="Edit message" />
      </label>
      <button @click="emitChange">Send update to parent</button>
    </div>
  `
};

export default {
  name: 'PropsEventsDemo',
  components: {
    ChildEditor: ChildEditor
  },
  data: function () {
    return {
      parentMessage: 'Hello from parent'
    };
  },
  methods: {
    onMessageChange: function (nextMessage) {
      this.parentMessage = nextMessage;
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

.child-box {
  margin-top: 10px;
  display: flex;
  gap: 10px;
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
</style>
