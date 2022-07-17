<template>
  <section class="dark-bg login-container">
    <div class="left-half">
      <h1 class="product-title">Minha Estante</h1>
      <h2 class="product-subtitle">sua plataforma de livros online</h2>
    </div>
    <div class="right-half">
      <login-form></login-form>
    </div>
  </section>
</template>

<script>
  import LoginForm from '@/components/auth/LoginForm.vue';

  export default {
    components: {
      LoginForm,
    },
  };
</script>

<style scoped>
  .login-container {
    display: flex;
    flex-direction: row;
  }
  .left-half {
    width: 50%;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-top: 15rem;
    margin-right: 10rem;
  }

  .right-half {
    background-color: #f0f0f7;
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
</style>
