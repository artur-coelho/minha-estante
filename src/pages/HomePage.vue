<template>
  <div class="dark-bg page-container">
    <header class="home-header">
      <div class="home-content">
        <h1 class="product-title">Minha Estante</h1>
        <h2 class="product-subtitle">sua plataforma de livros online</h2>
        <div class="buttons-container">
          <base-button link to="/login" size="big">LOGIN</base-button>
          <base-button link to="/register" size="big" :variant="'orange'"
            >CADASTRAR</base-button
          >
        </div>
      </div>
      <div>
        <img src="@/assets/images/home-image.svg" alt="Home Image" />
      </div>
    </header>
    <footer class="home-footer">
      <div>
        <a class="icon-button" target="_blank" href="https://youtube.com"
          ><img src="@/assets/icons/youtube.svg" alt="youtube"
        /></a>
        <a class="icon-button" target="_blank" href="https://whatsapp.com"
          ><img src="@/assets/icons/whatsapp.svg" alt="whatsapp"
        /></a>
        <a class="icon-button" target="_blank" href="https://instagram.com"
          ><img src="@/assets/icons/instagram.svg" alt="instagram"
        /></a>
      </div>
      <p class="copyright-text">© 2022 - Todos os direitos reservados</p>
      <div>
        <span class="footer-intro">Minha Estante</span>
        <img
          class="footer-drawn"
          src="@/assets/images/home-footer-drawn.svg"
          alt="footer-drawn"
        />
      </div>
    </footer>
  </div>
</template>

<script>
  export default {
    name: 'HomePage',
  };
</script>

<style scoped>
  .icon-button {
    text-decoration: none;
    cursor: pointer;
    margin-right: 15px;
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
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .copyright-text {
    display: flex;
    color: #ffffff;
  }

  .footer-drawn {
    position: absolute;
    bottom: 14px;
    left: 0;
  }

  .footer-intro {
    position: absolute;
    bottom: 72px;
    left: 44px;
    font-family: 'Birthstone Bounce', cursive;
    font-weight: 400;
    font-size: 32px;
    color: #ffffff;
  }
</style>
