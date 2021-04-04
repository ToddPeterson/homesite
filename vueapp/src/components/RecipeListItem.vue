<template>
    <div class="container">
        <div class="content">
            <h2 class="recipe-title">{{ recipe.title }}</h2>
            <p class="recipe-desc">{{ recipe.description }}</p>
            <a href="#" class="recipe-btn">See Recipe</a>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        recipe: Object
    }
};
</script>

<style scoped>
.container {
    margin-bottom: 3em;
}

.recipe-title {
    margin-bottom: .7em;
}

.recipe-desc {
    max-width: 36em;
    margin-bottom: 1em;
}

.recipe-btn {
    text-decoration: none;
    background: black;
    color: white;
    font-size: 1.15em;
    padding: .4em 1em;
    font-weight: 700;
}
</style>