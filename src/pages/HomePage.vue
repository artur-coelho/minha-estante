<template>
  <div class="home-bg">
    <header class="home-header">
      <div class="home-content">
        <h1 class="product-title">Minha Estante</h1>
        <h2 class="product-subtitle">sua plataforma de livros online</h2>
        <div class="buttons-container">
          <base-button link to="/login" :size="'big'">LOGIN</base-button>
          <base-button link to="/register" :size="'big'" :variant="'orange'"
            >CADASTRAR</base-button
          >
        </div>
      </div>
      <div>
        <img src="@/assets/images/home-image.svg" alt="Home Image" />
      </div>
    </header>
    <footer class="home-footer">
      <icon-button :iconImg="'Vector.svg'"></icon-button>
      <a class="icon-button" target="_blank" href="https://youtube.com"><img src="@/assets/icons/youtube.svg" alt="youtube"></a>
      <a class="icon-button" target="_blank" href="/"><img src="@/assets/icons/whatsapp.svg" alt="whatsapp"></a>
      <a class="icon-button" target="_blank" href="/"><img src="@/assets/icons/instagram.svg" alt="instagram"></a>
    </footer>
  </div>
</template>

<script>
  import BaseButton from '@/components/ui/BaseButton.vue';
  import IconButton from '@/components/ui/IconButton.vue';

  export default {
    name: 'HomePage',
    components: {
      BaseButton,
      IconButton,
    },
  };
</script>

<style>
  .icon-button {
    text-decoration: none;
    cursor: pointer;
  }

  .home-bg {
    display: flex;
    background-color: #1a1a23;
    height: 100%;
    width: fit-content;
    flex-direction: column;
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

  .home-footer {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
