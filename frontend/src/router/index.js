import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Encrypt from "../views/Encrypt.vue";
import Decrypt from "../views/Decrypt.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/encrypt",
    name: "Encrypt",
    component: Encrypt,
  },
  {
    path: "/decrypt",
    name: "Decrypt",
    component: Decrypt,
  }
  
];

const router = new VueRouter({
  routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active"
});

export default router;
