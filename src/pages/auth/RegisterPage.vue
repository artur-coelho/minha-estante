<template>
  <div class="dark-bg register-container">
    <section class="left-half">
      <div class="form-container">
        <h2 class="register-title">Cadastro</h2>
        <register-form @submit="register"></register-form>
      </div>
    </section>
    <section class="right-half">
      <h1 class="product-title">Minha Estante</h1>
      <h2 class="product-subtitle">sua plataforma de livros online</h2>
    </section>
  </div>
</template>

<script>
  import RegisterForm from '@/components/auth/RegisterForm.vue';

  export default {
    components: {
      RegisterForm,
    },
    methods: {
      register(data) {
        console.log(data);
      },
    },
  };
</script>

<style scoped>
  .register-container {
    display: flex;
    flex-direction: row;
  }
  .left-half {
    background-color: #f0f0f7;
    width: 47%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .form-container {
    width: 22rem;
  }

  .register-title {
    font-family: 'Poppins';
    font-weight: 600;
    font-size: 36px;
    line-height: 36px;
    color: #1a1a23;
  }

  .right-half {
    width: 53%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>
