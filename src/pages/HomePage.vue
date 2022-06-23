<template>
  <section>
    <h1>HOME</h1>
    <base-button :display="'block'" :size="'big'" >Cadastrar</base-button>
  </section>
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
