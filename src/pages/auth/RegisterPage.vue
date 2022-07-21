<template>
  <div class="dark-bg page-container register-container">
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
import axios from "axios";
import RegisterForm from '@/components/auth/RegisterForm.vue';

export default {
  components: {
    RegisterForm,
  },
  methods: {
    register(user) {
      axios.post("http://0.0.0.0:8000/user", user).then(() => {
        this.$router.push({ path: "/login" })
      })
    },
  },
};
</script>
<style scoped>
.register-container {
  flex-direction: row;
}

.left-half {
  background-color: #f0f0f7;
  width: 47%;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-container {
  width: 22rem;
}

.register-title {
  margin-bottom: 2rem;
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
