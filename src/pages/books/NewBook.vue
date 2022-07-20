<template>
  <div class="light-bg page-container">
    <div class="dark-bg header-bg">
      <header>
        <div class="new-book-container">
          <h1 class="page-title">Adicionar Livro</h1>
        </div>
        <router-link class="intro-img" to="/"
          ><img src="@/assets/images/Intro.svg" alt="Minha Estante"
        /></router-link>
      </header>
      <book-registration-form></book-registration-form>
    </div>
  </div>
</template>

<script>
  import BookRegistrationForm from '@/components/books/BookRegistrationForm.vue';

  export default {
    components: {
      BookRegistrationForm,
    },
  };
</script>

<style scoped>
  header {
    box-sizing: border-box;
    display: flex;
    justify-content: center;
  }
  .header-bg {
    width: 100%;
    max-height: 23rem;
  }

  .page-title {
    margin: 60px 0 72px 0;
    font-family: 'Archivo';
    font-weight: 700;
    font-size: 36px;
    line-height: 42px;
    color: #ffffff;
  }

  .new-book-container {
    width: 80%;
  }

  .intro-img {
    position: absolute;
    right: 92px;
    top: 52px;
    width: 50px;
  }
</style>
