<template>
    <div class="new-images">
        <header class="thin-header">
            <div id="nav" class="small-nav">
                <router-link to="/" class="left white-link hover-effect">JudgeMy.Pics</router-link>
                <router-link to="/new" class="left lime-button" exact>New post</router-link>
                <router-link to="/" class="right white-link hover-effect">sign up</router-link>
                <router-link to="/" class="right white-link hover-effect">sign in</router-link>
                <router-link to="/" class="right hover-effect">S</router-link>
            </div>
        </header>
        <div class="data">
            <div class="uploader" v-if="post.images.length === 0">
                <label for="files">
                    <div class="drag-area" v-on:drop.prevent="drop" v-on:dragover.prevent="dragover">
                        <p><b>Choose a file</b> or drag a file here.</p>
                    </div>
                </label>
                <input type="file" id="files" class="hidden"/>
            </div>
            <div v-else class="post">
                <div class="post-images">
                    <h1 contenteditable="true" class="post-title" v-on:click="removePlaceHolderTitle">Give this post a title...</h1>
                    <div v-for="(image, index) in post.images" class="post-image">
                        <div class="post-image-image">
                            <img :src="image.base64"/>
                        </div>
                        <div class="post-image-description" v-if="image.description" contenteditable="true">
                            {{ image.description }}
                        </div>
                        <div class="post-image-description" v-else contenteditable="true">
                            Add a description, #tags or @mention
                        </div>
                    </div>
                    <div class="post-add-more">Add more images</div>
                </div>
                <div class="side-panel">
                    <div class="tags">
                        <div>Chocholate</div>
                        <input type="checkbox"/>
                        Mature
                    </div>
                    <div class="line"></div>
                    <div class="post-link">
                        <input class="link" :value="post.url" readonly type="text"/>
                        <div class="copy">Copy</div>
                    </div>
                    <div class="post-social">
                        <span class="social-icon">F</span>
                        <span class="social-icon">T</span>
                        <span class="social-icon">P</span>
                        <span class="social-icon">R</span>
                    </div>
                    <div class="post-controls">
                        <div class="action">Add more images</div>
                        <div class="action">Embed post</div>
                        <div class="action">Post privacy</div>
                        <div class="red-action">Delete post</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Vue } from "vue-property-decorator";
import { new_post } from "../api";

export default class New extends Vue {
  post: IPost = {
        images: []
  };

  drop(event: DragEvent) {
    const self = this;
    if (event.dataTransfer.items) {
      for (let i = 0; i < event.dataTransfer.items.length; i++) {
        if (event.dataTransfer.items[i].kind === "file") {
          const file = event.dataTransfer.items[i].getAsFile();
          const reader = new FileReader();
          if (file) {
              reader.readAsDataURL(file);
              reader.onload = function() {
                  self.post.images.push({base64: String(reader.result)});
                  self.$forceUpdate();
                  self.new_post();
              };
              reader.onerror = function() {
                  console.log(reader.error);
              };
          }
        }
      }
    } else {
      for (let i = 0; i < event.dataTransfer.files.length; i++) {
        const file = event.dataTransfer.files[i];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function() {
            self.post.images.push({base64: reader.result});
            self.$forceUpdate();
            self.new_post();
        };
        reader.onerror = function() {
          console.log(reader.error);
        };
      }
    }
  }

  new_post() {
      new_post(this.post.title).then((response) => {
          this.$router.push({name: 'post', params: {id: response.data.post_id}})
      }).catch(console.error);
  }

  dragover() {
    return false;
  }

  removePlaceHolderTitle($event: Event) {
      this.post.title = '';
      this.$forceUpdate();
  }
}
</script>

<style lang="scss" scoped>

</style>
