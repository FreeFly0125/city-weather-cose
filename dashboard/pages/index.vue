<script setup lang="ts">
import store from '~/store';

const isShowSidebar = computed(() => store.state.isShowSidebar);

</script>

<template>
    <div class="w-full h-full bg-gray-950 px-48">
        <Headerbar />
        <div class="w-full h-[calc(100vh-112px)] items-center justify-center">
            <Mainboard />
            <NewLocationModal />
        </div>
        <Sidebar v-if="isShowSidebar"/>
    </div>
</template>
