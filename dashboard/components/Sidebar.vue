<template>
    <div class="fixed top-0 right-0 w-full md:w-1/3 h-full bg-gray-800 p-8 overflow-y-auto text-white">
        <button class="absolute top-4 right-4 text-gray-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                </path>
            </svg>
        </button>
        <h2 class="text-2xl font-bold mb-4">London</h2>
        <div class="grid grid-cols-1 md:grid-cols-1 gap-4 rounded-20">
            <h3 class="text-lg">This Week</h3>
            <div class="bg-gray-700 p-6 rounded-2xl shadow">
                <div class="flex flex-row justify-between">
                    <div class="flex flex-row justify-content gap-6">
                        <div class="row-span-3 flex justify-center">
                            <img alt="Cloud" class="w-12" />
                        </div>
                        <div
                            class="items-center flex justify-center text-gray-200 font-bold text-3xl">
                            2024-05-17
                        </div>
                    </div>
                    <div class="col-span-4 text-right">
                        <div class="text-gray-200 flex items-center">Min . &nbsp {{
                            15 }}°C</div>
                        <div class="text-gray-200 flex items-center">Max . &nbsp {{
                            20 }}°C</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
