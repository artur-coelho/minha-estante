<template>
  <form-card title="Dados do livro">
    <form class="" @submit.prevent="saveBook">
      <input class="basic-input" type="text" placeholder="ISBN" />
      <input class="basic-input" type="text" placeholder="ISBN" />
    </form>
  </form-card>
</template>

<script>
  export default {};
</script>

<style>
  .basic-input {
    width: 33rem;
    padding: 20px;
    margin-right: 28px;
    background: #fafafc;
    border: 1px solid #e6e6f0;
    border-radius: 8px;
  }

  .basic-input::placeholder {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 24px;
    color: #9c98a6;
  }
</style>
