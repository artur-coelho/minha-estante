<template>
  <div class="card">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    props: {
      title: { type: String, required: false, default: '' },
    },
    data() {
      return {};
    },
  };
</script>

<style scoped>
  .card {
    background: #ffffff;
    border: 1px solid #e6e6f0;
    border-radius: 8px;
    padding: 2rem 104px;
    margin: 0 auto;
    max-width: 80%;
  }
</style>
