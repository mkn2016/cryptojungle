<template>
    <form class="box control rows" ref="form" @submit.prevent="onSubmit">
        <div class="row field">
            <div class="control is-expanded">
            <div class="file is-right is-info is-fullwidth">
                <label class="file-label">
                <input class="file-input is-info" type="file" name="file" ref="file" @change="fileSelected">
                <span class="file-cta">
                    <span class="file-icon">
                    <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label">
                    Upload file…
                    </span>
                </span>
                <span class="file-name has-text-info is-clipped subtitle">
                  {{file}}
                </span>
                </label>
            </div>
            </div>
        </div>
        <div class="row field">
            <div class="control is-expanded has-icons-left">
            <input class="input is-info has-text-info" type="password" v-model="password" placeholder="Password|Passphrase">
            <span class="icon is-small is-left has-text-info">
                <i class="fas fa-lock"></i>
            </span>
            </div>
        </div>
        <div class="row field">
            <div class="control is-expanded">
            <button class="button is-info is-fullwidth" type="submit">Encrypt</button>
            </div>
        </div>
    </form>
</template>

<script>
import Vue from 'vue'

export default {
  data () {
    return {
      file: "",
      password: "",
    }
  },
  methods: {
    fileSelected(e) {
      this.file = e.target.files[0].name
    },
    showModal(alertMessage) {
      this.$emit('showModal', alertMessage)
    },
    onSubmit() {
      const file = this.$refs.file.files[0]

      if (!file) {
        this.$emit('showModal', "No file has been chosen")
        return;
      } else if (file.size > 1024 * 1024) {
        this.$emit('showModal', "File too big (> 1MB)")
        return;
      } else if (file.type !== "application/pdf") {
        this.$emit('showModal', "File must be of type (pdf)")
        return;
      } else if (!this.password) {
        this.$emit('showModal', "Password or Passphrase is required")
        return;
      } else {
        Vue.$toast.open(
          "File Sent To Server Successfully",
          {
            position: "top-right"
          }
        );
      }
    }
  }
}
</script>