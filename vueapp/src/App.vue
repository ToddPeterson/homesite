<template>
    <div class="main-container">
        <Menu class="menu" />
        <div class="main-content">
            <ul class="categories">
                <li class="category active">Favorites</li>
                <li class="category">Meals</li>
                <li class="category">Cuisine</li>
                <li class="category">Quick</li>
                <li class="category">All</li>
            </ul>
            <input type="text" class="searchbox" placeholder="Search" />
            <div class="recipe-list">
                <RecipeListItem v-for="recipe in recipes" :key="recipe.id" :recipe="recipe"/>
            </div>
        </div>
    </div>
</template>

<script>
import Menu from "./components/Menu.vue";
import RecipeListItem from "./components/RecipeListItem.vue";

export default {
    name: "App",
    components: {
        Menu,
        RecipeListItem
    },
    data() {
        return {
            recipes: [
                {
                    title: "Spicy Shrimp Pilaf",
                    description:
                        "Use the highest quality basmati rice you can find for a perfectly fluffy and fragrant pilaf.",
                    id: 1
                },
                {
                    title: "Mushroom-Farro Soup",
                    description:
                        "This cozy vegetarian soup delivers all the savory richness of mushroom-barley without meat or beef broth thanks to a few umami-heavy pantry ingredients.",
                    id: 2
                }
            ]
        };
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
    width: 320px;
}

.main-container {
    display: flex;
}

.main-content {
    padding: 5em 3em;
}

.categories {
    list-style: none;
    display: flex;
    margin-bottom: 1em;
}

.category {
    font-size: 1.5em;
    font-weight: 300;
}

.category + .category {
    margin-left: 2em;
}

.category.active {
    font-weight: 700;
}

.searchbox {
    width: 36em;
    height: 2.4em;
    border: 1px solid black;
    border-radius: 4px;
    padding-left: 0.8em;
    font-size: 1.2em;
    font-family: "Montserrat", Helvetica, Arial, sans-serif;
    margin-bottom: 2em;
}
</style>
