<template>
  <div class="dark-bg login-container">
    <section class="left-half">
      <h1 class="product-title">Minha Estante</h1>
      <h2 class="product-subtitle">sua plataforma de livros online</h2>
    </section>
    <section class="right-half">
      <div class="form-container">
        <div class="login-title">
          <h2>Login</h2>
        </div>
        <login-form @submit="login"></login-form>
      </div>
      <div class="login-footer">
        <span>Não possui sua estante digital?</span>
        <router-link to="/register">Cadastre-se</router-link>
      </div>
    </section>
    <img class="login-illustration" src="@/assets/images/login-image.svg" alt="woman choosing a book">
  </div>
</template>

<script>
  import LoginForm from '@/components/auth/LoginForm.vue';

  export default {
    components: {
      LoginForm,
    },
    methods: {
      login(data) {
        console.log(data)
      }
    }
  };
</script>

<style scoped>
  .login-container {
    display: flex;
    flex-direction: row;
  }
  .left-half {
    width: 53%;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-top: 15rem;
    margin-right: 10rem;
  }

  .right-half {
    background-color: #f0f0f7;
    width: 47%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .form-container {
    width: 22rem;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .login-title {
    width: 100%;
    display: flex;
    justify-content: flex-start;
  }

  .login-title h2 {
    font-family: 'Poppins';
    font-weight: 600;
    font-size: 36px;
    line-height: 36px;
    color: #1a1a23;
  }

  .login-footer {
    width: 22rem;
    margin-bottom: 3rem;
  }

  .login-footer span {
    display: block;
    font-family: 'Poppins';
    font-weight: 400;
    font-size: 16px;
    color: #6a6180;
  }

  .login-footer a {
    font-weight: 600;
    color: #4A80F0;
  }

  .login-illustration {
    width: 436px;
    position: absolute;
    bottom: 0;
    left: 33%;
  }
</style>
