<template>
    <div id="app">
        <Index :title="title" :desc="desc"/>
    </div>
</template>

<script>
import Index from "./components/Index/Index.vue";

export default {
    name: "app",
    components: {
        Index
    },
    data() {
        return {
            title: "Paste everywhere",
            desc: ["与朋友们共享数据。", "跨设备传输数据。", "你的操作不会被记录。", "你的隐私被充分尊重。"]
        };
    }
};
</script>

<style>
#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
