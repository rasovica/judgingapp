<template>
    <div class="post">
        wtf
        {{ post.url }}
    </div>
</template>

<script lang="ts">
    import { Vue } from "vue-property-decorator";

    export default class Post extends Vue {
        post: IPost = {
            images: []
        };
    }
</script>