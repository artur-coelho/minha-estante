<template>
  <router-view></router-view>
</template>

<script>
  export default {
    name: 'App',
  };
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Birthstone+Bounce&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

  * {
    margin: 0;
    box-sizing: border-box;
  }

  html {
    font-family: 'Poppins', sans-serif;
  }

  body {
    margin: 0;
  }

  .page-container {
    display: flex;
    min-height: 100vh;
    width: 100vw;
    flex-direction: column;
  }

  .dark-bg {
    background-color: #1a1a23;
  }

  .light-bg {
    background-color: #f0f0f7;
  }

  .product-title {
    margin: 0;
    font-family: 'Birthstone Bounce', cursive;
    font-weight: 400;
    font-size: 100px;
    line-height: 136px;
    color: #fffafa;
  }

  .product-subtitle {
    margin: 0 28px;
    width: 426px;
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
    font-size: 35px;
    line-height: 52px;
    color: #bdd6d2;
  }
</style>
