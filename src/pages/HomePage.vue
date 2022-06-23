<template>
<div class="backGroundHome">
  <header class="home-header">
    <div class="home-content">
      <h1 class="product-title">Minha Estante</h1>
      <h2 class="product-subtitle">sua plataforma de livros online</h2>
      <div class="buttons-container">
        <base-button link to="/login" :size="'big'">LOGIN</base-button>
        <base-button link to="/register" :size="'big'" :variant="'orange'">CADASTRAR</base-button>
      </div>
    </div>
    <div>
      <img src="@/assets/images/home-image.svg" alt="Home Image">
    </div>
  </header>
  <footer></footer>
</div>
</template>

<script>
  import BaseButton from '@/components/ui/BaseButton.vue';

  export default {
    name: 'HomePage',
    components: {
      BaseButton,
      
    },
  };
</script>

<style>
.backGroundHome {
  display: flex;
  background-color: #1A1A23;
  height: 100vh;
}

.home-header {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 166px auto 136px auto;
  padding: 2rem 11rem;
}

.home-content {
  margin-right: 84px;
}

.buttons-container {
  display: flex;
  margin-top: 72px;
  margin-left: 28px;
}
</style>