export default {
  state() {
    return {
      books: [{ nome: 'Harry Potter' }],
    };
  },
  mutations: {
    registerBook(state, payload) {
      state.books.push(payload);
    },
  },
  actions: {
    registerBook(context, data) {
      context.commit('registerBook', data);
    },
  },
  getters: {
    books(state) {
      return state.books;
    },
  },
};
