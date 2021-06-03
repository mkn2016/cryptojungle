<template>
  <section class="hero is-fullheight is-link">
    <nav-header>
      <slot name="header">
        <nav-bar />
      </slot>
    </nav-header>
    <main-content />
  </section>
</template>

<script>
import NavBar from "./components/NavBar.vue"
import MainContent from "./components/MainContent.vue"
import NavHeader from "./components/NavHeader.vue"

export default {
  name: "Home",
  components: {
    NavBar,
    MainContent,
    NavHeader
  },
  methods: {
  }
};
</script>

<style></style>
