<template>
  <div class="home-page">
    <header class="fat-header">
      <div id="nav">
        <router-link to="/new" class="left lime-button">New post</router-link>
        <input type="text" class="center" placeholder="Images, #tags, @users oh my!"/>
        <router-link to="/login" class="right lime-button">Sign up</router-link>
        <router-link to="/register" class="right white-link">Sign in</router-link>
      </div>
    </header>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import JudgeImage from "@/components/JudgeImage.vue";

@Component({
  components: {
    JudgeImage
  }
})
export default class Home extends Vue {
  mounted() {}
}
</script>

<style lang="scss" scoped>

</style>