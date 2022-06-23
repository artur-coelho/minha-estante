<template>
  <button v-if="!link" :class="[size, variant, display]">
    <slot></slot>
  </button>
  <router-link v-else :to="to" :class="[size, variant, display]">
    <slot></slot>
  </router-link>
</template>

<script>
  export default {
    props: {
      size: { type: String, required: false, default: 'small' },
      variant: { type: String, required: false, default: 'primary' },
      display: { type: String, required: false, default: 'flex' },
      link: { type: Boolean, required: false, default: false },
      to: { type: String, required: false, default: '/' },
    },
  };
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&display=swap');

  button,
  a {
    text-decoration: none;
    font: inherit;
    font-family: 'Archivo', sans-serif;
    color: white;
    cursor: pointer;
    border: none;
    border-radius: 8px;
    margin-right: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  a:hover,
  a:active,
  button:hover,
  button:active {
    background-color: #1e51ba;
    border-color: #1e51ba;
  }

  .primary {
    background-color: #4a80f0;
  }

  .orange {
    background-color: #f2994a;
  }

  .small {
    padding: 1rem 0;
    font-weight: 600;
    font-size: 16px;
  }

  .big {
    width: 250px;
    height: 100px;
    padding: 2rem 0;
    font-weight: 700;
    font-size: 26px;
    margin-right: 26px;
  }

  .orange:hover,
  .orange:active {
    background-color: #d17728;
  }

  .flex {
    display: flex;
  }

  .block {
    display: block !important;
    width: 100% !important;
  }
</style>
