<template>
  <form-card title="Dados do livro">
    <form class="" @submit.prevent="saveBook">
      <div class="form-header">
        <h3 class="form-title">Dados do Livro</h3>
        <hr />
      </div>
      <div class="book-data-one">
        <input class="basic-input" type="text" placeholder="ISBN" />
        <input class="basic-input" type="text" placeholder="Nome do Livro" />
        <input
          class="basic-input"
          type="text"
          placeholder="Selecione o gênero"
        />
        <input class="basic-input" type="text" placeholder="Status" />
        <input class="basic-input" type="text" placeholder="Editora" />
        <input class="basic-input" type="text" placeholder="Edição" />
        <input
          class="basic-input"
          type="text"
          placeholder="Selecione o tipo de capa"
        />
        <input class="basic-input" type="text" placeholder="Total de páginas" />
        <input class="basic-input" type="text" placeholder="Classificação" />
        <input class="basic-input" type="text" placeholder="Idioma" />
      </div>
      <textarea
        class="basic-input"
        id="description"
        rows="5"
        v-model.trim="description"
      ></textarea>
      <div class="book-data-two">
        <base-toggle label="Foi um presente?"></base-toggle>
        <base-toggle label="Faz parte de uma série?"></base-toggle>
        <input class="basic-input" type="text" placeholder="Número da série" />
      </div>
      <input type="date" name="" id="">
    </form>
  </form-card>
</template>

<script>
  export default {
    data() {
      return {
        description: '',
      };
    },
  };
</script>

<style>
  hr {
    border: 1px solid #e6e6f0;
  }

  .form-header {
    margin-bottom: 4rem;
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
    grid-template-columns: 0.5fr 0.5fr 1fr;
    column-gap: 28px;
  }
</style>
