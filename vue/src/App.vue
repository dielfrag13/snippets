<template>
  <div class="app">
    <h1>{{ title }}</h1>
    <p>Hello, {{ name }} 👋</p>

    <label>
      Update your name:
      <input v-model="name" type="text" placeholder="Type a name" />
    </label>

    <div class="counter">
      <button @click="count--">-</button>
      <span>Count: {{ count }}</span>
      <button @click="count++">+</button>
    </div>

    <p>{{ computedMessage }}</p>

    <div class="demo-stack">
      <div class="tab-nav">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          class="tab-btn"
          :class="{ active: activeTab === tab.key }"
          @click="setActiveTab(tab.key)"
        >
          {{ tab.label }}
        </button>
      </div>

      <p class="remembered-tab">Last remembered tab: {{ activeTabLabel }}</p>

      <div class="tab-panel">
        <PropsEventsDemo v-show="activeTab === 'props'" />
        <ComputedWatchDemo v-show="activeTab === 'computed'" />
        <ConditionalListDemo v-show="activeTab === 'conditional'" />
      </div>
    </div>
  </div>
</template>

<script>
import PropsEventsDemo from './components/PropsEventsDemo.vue';
import ComputedWatchDemo from './components/ComputedWatchDemo.vue';
import ConditionalListDemo from './components/ConditionalListDemo.vue';

var TAB_STORAGE_KEY = 'vue2-reactive-playground.active-tab';

export default {
  name: 'App',
  components: {
    PropsEventsDemo: PropsEventsDemo,
    ComputedWatchDemo: ComputedWatchDemo,
    ConditionalListDemo: ConditionalListDemo
  },
  data: function () {
    // Provides top-level state used by the intro UI and demo tab switcher.
    return {
      title: 'Vue 2 Reactive UI',
      name: 'World',
      count: 0,
      activeTab: 'props',
      tabs: [
        { key: 'props', label: 'Props/Events' },
        { key: 'computed', label: 'Computed/Watch' },
        { key: 'conditional', label: 'Conditional/List' }
      ]
    };
  },
  created: function () {
    // Restores the last selected tab from localStorage when the app loads.
    var persistedTab = this.loadActiveTab();
    if (persistedTab) {
      this.activeTab = persistedTab;
    }
  },
  computed: {
    // Returns a small message proving that computed properties react to changes.
    computedMessage: function () {
      return this.count % 2 === 0
        ? 'Even count: reactive updates are working.'
        : 'Odd count: still reactive!';
    },

    // Returns the display label for the currently active (and remembered) tab.
    activeTabLabel: function () {
      var selectedTab = this.tabs.find(
        function (tab) {
          return tab.key === this.activeTab;
        }.bind(this)
      );

      return selectedTab ? selectedTab.label : this.activeTab;
    }
  },
  watch: {
    // Persists the currently selected tab whenever it changes.
    activeTab: function (nextTab) {
      this.saveActiveTab(nextTab);
    }
  },
  methods: {
    // Handles tab button clicks and updates the visible demo section.
    setActiveTab: function (tabKey) {
      if (this.isValidTab(tabKey)) {
        this.activeTab = tabKey;
      }
    },

    // Validates that a tab key exists in the configured tabs list.
    isValidTab: function (tabKey) {
      return this.tabs.some(function (tab) {
        return tab.key === tabKey;
      });
    },

    // Reads tab state from localStorage and returns null when missing/invalid.
    loadActiveTab: function () {
      var storedValue = localStorage.getItem(TAB_STORAGE_KEY);
      return this.isValidTab(storedValue) ? storedValue : null;
    },

    // Writes the selected tab key to localStorage for future sessions.
    saveActiveTab: function (tabKey) {
      localStorage.setItem(TAB_STORAGE_KEY, tabKey);
    }
  }
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f7f7f7;
}

.app {
  max-width: 560px;
  margin: 48px auto;
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
}

h1 {
  margin-top: 0;
}

input {
  margin-left: 8px;
  padding: 6px 8px;
}

.counter {
  margin-top: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.demo-stack {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.tab-nav {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tab-btn {
  border: 1px solid #d5d5d5;
  background: #f3f3f3;
}

.tab-btn.active {
  background: #e5e5e5;
  font-weight: 600;
}

.tab-panel {
  margin-top: 6px;
}

.remembered-tab {
  margin: 2px 0 0;
  color: #555;
  font-size: 14px;
}

button {
  padding: 6px 10px;
  cursor: pointer;
}
</style>
