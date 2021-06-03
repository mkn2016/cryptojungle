<template>
  <div class="container has-text-centered">
    <sweet-modal ref="modal" icon="error" hide-close-button overlay-theme="dark" modal-theme="dark" title="Error">
      <span>{{alertMessage}}</span>
      <button slot="button" class="has-background-danger has-text-white" @click="closeModal">Exit</button>
    </sweet-modal>
    <section class="level">
      <div class="level-left">
        <div class="level-item has-text-centered">
          <navigation-link :to="home"></navigation-link>
        </div>
      </div>
      <div class="level-item">
        <div class="column is-4">
          <h1 class="is-size-3">
            Crypto Jungle
          </h1>
          <sub-title-heading />
        <main-form @showModal="showModal($event)"/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import MainForm from '../components/MainForm.vue'
import SubTitleHeading from '../components/SubTitleHeading.vue'
import NavigationLink from '../components/NavigationLink.vue'

export default {
  data () {
    return {
      alertMessage: null,
      home: "/"
    }
  },
  components: {
    MainForm,
    NavigationLink,
    SubTitleHeading
  },
  methods: {
    showModal(alertMessage) {
      this.alertMessage = alertMessage
      this.$refs.modal.open()
    },
    closeModal() {
      this.$refs.modal.close()
    }
  }
}
</script>