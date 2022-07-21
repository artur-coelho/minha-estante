<template>
  <form-card>
    <form @submit.prevent="saveBook">
      <div class="form-header">
        <h3 class="form-title">Dados do Livro</h3>
        <hr />
      </div>
      <div class="book-data-one">
        <input v-model="book.isbn" class="basic-input" type="int" placeholder="ISBN" />
        <input v-model="book.name" class="basic-input" type="text" placeholder="Nome do Livro" />
        <input v-model="book.genre" class="basic-input" type="text" placeholder="Selecione o gênero" />
        <input v-model="book.status" class="basic-input" type="text" placeholder="Status" />
        <input v-model="book.publishingCompany" class="basic-input" type="text" placeholder="Editora" />
        <input v-model="book.edition" class="basic-input" type="text" placeholder="Edição" />
        <input v-model="book.coverType" class="basic-input" type="text" placeholder="Selecione o tipo de capa" />
        <input v-model="book.numberOfPages" class="basic-input" type="text" placeholder="Total de páginas" />
        <input v-model="book.rating" class="basic-input" type="text" placeholder="Classificação" />
        <input v-model="book.language" class="basic-input" type="text" placeholder="Idioma" />
      </div>
      <textarea placeholder="Descrição" class="basic-input" id="description" rows="5"
        v-model.trim="book.description"></textarea>
      <div class="book-data-two">
        <base-toggle label="Possui dedicatória?"></base-toggle>
        <base-toggle label="Faz parte de uma série?"></base-toggle>
        <input class="basic-input" type="text" placeholder="Número da série" />
      </div>
      <div class="book-data-three">
        <base-toggle label="Possui autógrafo?"></base-toggle>
        <base-toggle label="Foi um presente?"></base-toggle>
        <input class="basic-input" type="text" placeholder="Nome de quem presenteou" />
        <input v-model="book.date" class="basic-input" type="datetime-local" name="" id="" placeholder="Data" />
      </div>
      <div class="form-header">
        <h3 class="form-title">Dados do Autor</h3>
        <hr />
      </div>
      <div class="author-data">
        <input class="basic-input" type="text" placeholder="Nome do autor" />
        <input class="basic-input" type="file" />
        <div>
          <h4>Gênero</h4>
          <div class="checkbox-author">
            <div>
              <input type="checkbox" name="man" id="man" value="man" />
              <label for="man">Masculino</label>
            </div>
            <div>
              <input type="checkbox" name="woman" id="woman" value="woman" />
              <label for="woman">Feminino</label>
            </div>
          </div>
        </div>
      </div>
      <div class="form-header">
        <h3 class="form-title">Minha Estante</h3>
        <hr />
      </div>
      <div class="bookcase-data">
        <select class="basic-input" placeholder="Selecione a estante" name="bookcase" id="bookcase">
          <option value="bookcase1">Estante 1</option>
          <option value="bookcase2">Estante 2</option>
          <option value="bookcase3">Estante 3</option>
        </select>
        <select class="basic-input" placeholder="Selecione a prateleira" name="shelf" id="shelf">
          <option value="shelf1">Prateleira 1</option>
          <option value="shelf2">Prateleira 2</option>
          <option value="shelf3">Prateleira 3</option>
        </select>
      </div>
      <div class="button-container">
        <base-button>Salvar Cadastro</base-button>
      </div>
    </form>
  </form-card>
</template>

<script>
export default {
  emits: ['submit'],
  data() {
    return {
      book: {
        isbn: null,
        name: '',
        genre: '',
        status: '',
        publishingCompany: '',
        edition: '',
        coverType: '',
        numberOfPages: null,
        rating: '',
        language: '',
        description: '',
        date: ''
      },

    };
  },
  methods: {
    saveBook() {
      console.log(this.book)
      const registerData = {
        usuario_id: 1,
        isbn: this.book.isbn,
        nome: this.book.name,
        genero: this.book.genre,
        editora: this.book.publishingCompany,
        edicao: this.book.edition,
        tipo_capa: this.book.coverType,
        descricao: this.book.description,
        data_cadastro: this.book.date,
      };
      this.$emit('submit', registerData);
    },
  },
};
</script>

<style scoped>
hr {
  border: 1px solid #e6e6f0;
}

.form-header {
  margin-bottom: 40px;
}

.form-title {
  margin-bottom: 20px;

  font-family: 'Archivo', sans-serif;
  font-weight: 600;
  font-size: 24px;
  color: #32264d;
}

.basic-input {
  width: 100%;
  padding: 20px;
  background: #fafafc;
  border: 1px solid #e6e6f0;
  border-radius: 8px;
}

.basic-input::placeholder {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  color: #9c98a6;
}

.book-data-one {
  margin-bottom: 30px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 28px;
  row-gap: 30px;
}

.book-data-two {
  margin-top: 30px;
  display: grid;
  grid-template-columns: 0.4fr 0.4fr 1.2fr;
  column-gap: 28px;
}

.book-data-three {
  margin-top: 30px;
  margin-bottom: 40px;
  display: grid;
  grid-template-columns: 0.4fr 0.4fr 0.7fr 0.5fr;
  column-gap: 28px;
}

.author-data {
  margin-bottom: 48px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 28px;
}

h4,
label {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 400;
  color: #9c98a6;
}

.checkbox-author {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

input[type='checkbox'] {
  display: inline;
  width: auto;
  border: none;
  margin-right: 0.5rem;
}

.bookcase-data {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 28px;
}

.button-container {
  margin-top: 6rem;
  display: flex;
  justify-content: flex-end;
}
</style>
