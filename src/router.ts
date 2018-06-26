import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import New from "./views/New.vue";
import Post from "./views/Post.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/new",
      name: "new",
      component: New
    },
    {
      path: "/post/:id",
      name: "post",
      component: Post
    },
    {
      path: "/",
      name: "home",
      component: Home
    },
  ],
  mode: "history"
});
