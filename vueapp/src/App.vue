<template>
    <div class="container">
        <Menu class="menu" />
        <div class="content">
            <ul class="categories">
                <li class="category">Favorites</li>
                <li class="category">Meals</li>
                <li class="category">Cuisine</li>
                <li class="category">Quick</li>
                <li class="category">All</li>
            </ul>
        </div>
    </div>
</template>

<script>
import Menu from "./components/Menu.vue";

export default {
    name: "App",
    components: {
        Menu
    }
};
</script>

<style>
#app {
    font-family: "Montserrat", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    font-size: 16px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.menu {
    background: #fcf7c9;
    display: block;
    height: 100vh;
    width: 350px;
}
</style>
