<template>
  <div class="card">
    <div v-if="title" class="form-header">
      <h3 class="form-title">{{ title }}</h3>
      <hr />
    </div>
    <slot> </slot>
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
  hr {
    border: 1px solid #e6e6f0;
  }
  .card {
    background: #ffffff;
    border: 1px solid #e6e6f0;
    border-radius: 8px;
    padding: 2rem 104px;
    margin: 0 auto;
    max-width: 80%;
  }
  .form-header {
    margin-bottom: 4rem;
  }
  .form-title {
    margin-bottom: 20px;

    font-family: 'Archivo', sans-serif;
    font-weight: 600;
    font-size: 24px;
    color: #32264d;
  }
</style>
