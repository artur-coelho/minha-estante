<template>
  <div class="card">
    <slot> </slot>
  </div>
</template>

<style scoped>
  .card {
    background: #ffffff;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
    padding: 1rem;
    margin: 0 auto;
    max-width: 90%;
  }
</style>
