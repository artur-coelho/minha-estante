<template>
  <form @submit.prevent="submitForm" class="login-form">
    <input type="email" class="base-input top-input" placeholder="E-mail" />
    <input
      type="password"
      class="base-input bottom-input"
      placeholder="Senha"
    />
    <div class="form-footer">
      <div>
        <input
          type="checkbox"
          name="remember-me"
          id="remember-me"
          v-model="rememberMe"
        />
        <label class="remember-label" for="remember-me">Lembrar-me</label>
      </div>
      <router-link class="forgot-psw-link" to="/forgotPassword"
        >Esqueci minha senha</router-link
      >
    </div>
    <base-button display="block">Entrar</base-button>
  </form>
</template>

<script>
  export default {
    data() {
      return {
        rememberMe: false,
      };
    },
    methods: {
      submitForm() {},
    },
  };
</script>

<style>
  .login-form {
    width: 100%;
  }

  .base-input {
    width: 100%;
    background: #fafafc;
    display: block;
    padding: 22px;
    border: 1px solid #e6e6f0;

    font-family: 'Poppins';
    font-size: 16px;
    color: #6a6180;
  }

  .top-input {
    border-radius: 8px 8px 0px 0px;
  }

  .bottom-input {
    border-radius: 0px 0px 8px 8px;
  }

  .form-footer {
    margin: 24px 0 40px 0;
    display: flex;
    justify-content: space-between;
  }

  .remember-label {
    margin-left: 1rem;
    font-size: 14px;
    line-height: 24px;
    color: #9c98a6;
  }

  .forgot-psw-link {
    text-decoration: none;
    font-family: 'Poppins';
    font-size: 14px;
    line-height: 24px;
    text-align: right;
    color: #9c98a6;
  }
</style>
