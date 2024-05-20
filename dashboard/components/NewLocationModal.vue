<template lang="">
    <div class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75 transition-all duration-500 text-white">
        <div class="bg-gray-800 p-8 rounded-lg shadow w-96">
            <div class="flex justify-between">
                <div class="text-white-800">
                    <h2 class="text-2xl font-bold mb-4">Add Location</h2>
                </div>
                <div class="text-white-800">                            
                    <button class="text-gray-200" @click="visibilityModal">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>

            
            <form @submit.prevent="insertNewLocation">
                <div class="gap-6 mb-4">
                    <div class="relative">
                        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                            </svg>
                        </div>
                        <input
                            v-model="locationName"
                            type="search"
                            id="default-search"
                            class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Locations"
                            required />
                    </div>
                </div>
                <button class="bg-gray-700 hover:bg-gray-400 text-white px-4 py-2 w-full rounded-lg"
                    type="submit">
                    Add Location
                </button>
            </form>
            
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
import store from '~/store';

export default {
    data() {
        return {
            locationName: '',
        };
    },

    methods: {
        ...mapActions(['createLocation', 'changeVisibilityModal']),
        insertNewLocation() {
            if (this.locationName.trim()) {
                store.dispatch('createLocation', this.locationName);
                this.locationName = '';
            }
        },
        visibilityModal() {
            store.dispatch('changeVisibilityModal', false);
        }
    },
};
</script>
