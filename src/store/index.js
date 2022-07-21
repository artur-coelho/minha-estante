import { createStore } from 'vuex';

import booksModule from './books/index.js';

const store = createStore({
  modules: {
    books: booksModule,
  },
  state() {
    return {
      userId: '',
    };
  },
  getters: {
    userId(state) {
      return state.userId;
    },
  },
});

export default store;
