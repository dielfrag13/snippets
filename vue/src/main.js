import Vue from 'vue';
import App from './App.vue';

new Vue({
  // Renders the root App component into the mount element.
  render: function (h) {
    return h(App);
  }
}).$mount('#app');
