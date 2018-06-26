<template>
    <img v-bind:src="imageSrc">
</template>


<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { imageCdn } from "../constants";

@Component
export default class JudgeImage extends Vue {
  @Prop() private imageFile!: string;

  imageSrc = "";

  constructor() {
    super();

    this.imageSrc = imageCdn + this.imageFile;

    console.log(this.imageSrc);
  }
}
</script>

<style scoped>
</style>
