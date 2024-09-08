<template>
    <div id="header">
        header
    </div>
    <div id="header_height_adjust"></div>
</template>

<script>
export default {
    name: 'HeaderComponent',
}
</script>

<style scoped lang="scss">
$height: 24px;

.header_height_adjust {
    height: $height;
}

#header {
    background-color: #404040;
    color: white;
    position: fixed;
    top: 0;
    z-index: 9999;
    width: 100%;
    height: $height;
    padding: 2px;
    overflow-x: auto;
    overflow-y: unset;
    white-space: nowrap;
}
</style>
