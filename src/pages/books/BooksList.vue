<template>
  <div class="page-container light-bg">
    <header class="dark-bg header-bg">
      <div class="books-list-container">
        <h1 class="page-title">Meus Livros</h1>
        <base-button link to="/newBook">Adicionar Livro</base-button>
      </div>
      <router-link class="intro-img" to="/"><img src="@/assets/images/Intro.svg" alt="Minha Estante" /></router-link>
    </header>
    <base-card>
      <table>
        <tr>
          <th>ISBN</th>
          <th>Nome</th>
          <th>Gênero</th>
        </tr>
        <tr v-for="book in books" :key="book.isbn">
          <td>{{ book.isbn }}</td>
          <td>{{ book.nome }}</td>
          <td>{{ book.genero }}</td>
        </tr>
      </table>
    </base-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      books: [
        {
          isbn: 'b1',
          name: 'Harry Potter',
          author: 'J.K',
          numberOfPages: 500,
        },
        {
          isbn: 'b2',
          name: 'Senhor dos anéis',
          author: 'Tolkien',
          numberOfPages: 1000,
        },
      ],
    };
  },
  mounted() {
    this.get_livros()
  },
  methods: {
    get_livros() {
      axios.get("http://0.0.0.0:8000/livros/").then(response => {
        this.books = response.data
      })
    }
  }
};
</script>

<style scoped>
.header-bg {
  width: 100%;
  max-height: 23rem;
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.books-list-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 64%;
}

.page-title {
  margin: 60px 0 72px 0;
  font-family: 'Archivo';
  font-weight: 700;
  font-size: 36px;
  line-height: 42px;
  color: #ffffff;
}

.intro-img {
  position: absolute;
  right: 92px;
  top: 52px;
  width: 50px;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 60rem;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
