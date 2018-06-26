<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
body {
  margin: 0;
  font-family: "Poxima Nova Regular", "Helvatica Neue", Helvatica, Arial, sans-serif;
}

.fat-header {
  height: 50px;
  padding: 20px;
  background-color: #2e3035;
}

.thin-header {
  height: 50px;
  line-height: 50px;
  background-color: #34373c;
}

.home-page {
  background-color: #2e3035;
  width: 100vw;
  height: 100vh;
}

.right {
  float: right;
}

.white-link {
  color: white;
  text-decoration: none;
  padding: 0 20px;
}

.center {
  width: 400px;
  position: fixed;
  padding: 5px 20px;
  margin: 15px auto auto;
  top: 0;
  left: 0;
  right: 0;
  border-radius: 5px;
  border: none;
  background-color: hsla(0,0%,100%,0.25)
}

.lime-button {
  @extend .white-link;
  background-color: #1bb76e;
  border-radius: 5px;
  padding-top: 5px;
  padding-bottom: 5px;
  margin-top: -5px;
}

.drag-area {
  padding: 50px 30px;
  background-color: #45484f;
  width: 50vw;
  margin: 0 auto;
  border: 1px black solid;
  color: white;
  text-align: center;
  cursor: pointer;
}

.hidden {
  display: none;
}

.small-nav {
  width: 53vw;
  margin: 0 auto;
}


.hover-effect {
  transition: background-color 1000ms;
  border-radius: 25px;
  padding: 0 10px;
  line-height: normal;
  margin: 15px 0;
}

.hover-effect:hover {
  background-color: gray;
}

.data {
  background-color: #141518;
  display: block;
  overflow: auto;
}

.post {
  width: 60vw;
  margin: 30px auto;
  position: relative;
}

.post-images {
  width: 70%;
}

.post-image {
  width: 100%;
}

.post-image-image {
  padding: 0;
  width: 100%;
}

.post-image-image img{
  width: 100%;
  height: 100%;
}

.post-image input{
  width: 100%;
}

.post-image-description {
  width: 100%;
  background-color: #2c2f34;
  padding: 20px;
  color: #8a8a8a;
  font-size: 18px;
  font-weight: 400;
  margin: -10px 0 0;
  box-sizing: border-box;
}

.post-title {
  background-color: #2c2f34;
  width: 100%;
  color: #8a8a8a;
  margin: 0;
  font-size: 18px;
  font-weight: 400;
  line-height: 60px;
  padding-left: 20px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  box-sizing: border-box;
}

.post-add-more {
  width: 100%;
  text-align: center;
  color: blue;
  margin: 20px 0;
  cursor: pointer;
}

.side-panel {
  position: fixed;
  top: 10%;
  right: 15vw;
  width: 20%;
}

.line {
  border-bottom: 1px solid #2c2f34;
  margin-top: 20px;
}

.post-link {
  border: 1px solid #2c2f34;
  position: relative;
  height: 40px;
}

.link{
  background-color: black;
  color:#f2f2f2;
  padding: 10px;
  width: 55%;
  border: none;
  font: inherit;
  @extend .all-select
}

.copy {
  position: absolute;
  top: 0;
  right: 0;
  width: 45%;
  text-align: center;

  background-color: rgb(44,47,52);
  color: gray;
  line-height: 40px;
  text-overflow: clip;

  @extend .no-select
}

.copy:hover {
  background-color: #494a4f;
  color:#f2f2f2;
}

.link::selection {
  background: #1bb76e;
}

.link::-moz-selection {
  background: #1bb76e;
}

.post-social {
  text-align: center;
  padding: 20px;
}

.social-icon {
  width: 30px;
  height: 30px;
  border-radius: 15px;
  background: white;
  margin: 10px;
}

.all-select {
  -webkit-user-select: all;
  -moz-user-select: all;
  -ms-user-select: all;
  user-select: all;
}

.no-select {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.post-controls {
  color:#f2f2f2;
  background-color: #2c2f34;
  padding: 10px;
  border-radius: 10px;
}

.action {
  margin: 20px
}

.action:hover {
  background-color: #8a8a8a;
}

.red-action {
  @extend .action;

  color: red;
}

.uploader {
  height: calc(100vh - 50px);
  margin: 50px;
}
</style>
