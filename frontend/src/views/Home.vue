<template>
  <div class="container has-text-centered">
    <section class="level">
      <div class="level-left">
        <div class="level-item has-text-centered">
          <navigation-link :to="encrypt">
            <template #col1>
              <i class="fas fa-arrow-circle-left"></i>
            </template>
            <template #col2>
              <span>Encrypt</span>
            </template>
          </navigation-link>
        </div>
      </div>
      <div class="level-item has-text-centered">
        <div class="rows">
          <div class="row">
            <span class="title">Let's Get Started...</span>
          </div>
          <div class="row">
            <router-link to="/" data-tooltip="Go to Home">
              <img src="../assets/images/logo.png" width="200" height="200" alt="Logo">
            </router-link>
          </div>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item has-text-centered">
          <navigation-link :to="decrypt">
            <template #col1>
              <div class="column">
                <span>Decrypt</span>
              </div>
            </template>
            <template #col2>
            <div class="column">
              <span class="icon">
                <i class="fas fa-arrow-circle-right"></i>
              </span>
            </div>
            </template>
          </navigation-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import NavigationLink from '../components/NavigationLink.vue'

export default {
  data () {
    return {
      decrypt: "/decrypt",
      encrypt: "/encrypt"
    }
  },
  components: {
    NavigationLink
  },
}
</script>