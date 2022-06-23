<template>
  <button v-if="!link" :class="[variant]">
    <img :src="`@/assets/icons/${iconImg}`" :alt="iconImg">
  </button>
  <router-link v-else :to="to" :class="[variant]">
    <img :src="`@/assets/icons/${iconImg}`" :alt="altText">
  </router-link>
</template>

<script>
export default {
    name: 'IconButton',
    props: {
        variant: {type: String, default: 'white'},
        iconImg: {type: String, default: ''},
        altText: {type: String, default: ''},
        link: {type: Boolean, default: false}
    }
}
</script>
 
<style>
button,
a {
    text-decoration: none;
    cursor: pointer;
    border: none;
}

.white {
    color: white;
}

.black {
    color: black;
}
</style>