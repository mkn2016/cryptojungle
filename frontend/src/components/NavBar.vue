<template>
    <nav class="navbar">
        <div class="container">
        <div class="navbar-brand">
            <span class="navbar-burger" data-target="navbarMenuHeroB">
            <span></span>
            <span></span>
            </span>
        </div>
        <div id="navbarMenuHeroB" class="navbar-menu">
            <div class="navbar-end">
                <nav-bar-item />
                <nav-bar-item>
                    <i class="fab fa-github"></i>
                </nav-bar-item>
            </div>
        </div>
        </div>
    </nav>
</template>

<script>
import NavBarItem from "../components/NavBarItem.vue"

export default {
  name: "Home",
  data () {
    return {
      
    }
  },
  components: {
    NavBarItem
  },
  methods: {
  }
};
</script>