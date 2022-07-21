<template>
  <form @submit.prevent="submitForm" class="login-form">
    <input
      type="text"
      class="base-input top-input"
      placeholder="Nome"
      v-model="firstName"
    />
    <input
      type="text"
      class="base-input"
      placeholder="Sobrenome"
      v-model="lastName"
    />
    <input
      type="email"
      class="base-input"
      placeholder="E-mail"
      v-model="email"
    />
    <input
      type="password"
      class="base-input bottom-input"
      placeholder="Senha"
      v-model="password"
    />
    <base-button display="block">Concluir cadastro</base-button>
  </form>
</template>

<script>
  export default {
    emits: ['submit'],
    data() {
      return {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
      };
    },
    methods: {
      submitForm() {
        const registerData = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
        };
        this.$emit('submit', registerData);
      },
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
    margin-bottom: 40px;
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
