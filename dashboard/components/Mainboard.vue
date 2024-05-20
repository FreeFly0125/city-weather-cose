<template lang="">
    <div class="flex text-white justify-between pt-12 pb-4">
        <div class="flex items-center">
            <p class="text-4xl">Locations</p>
        </div>
        <div class="flex items-center">
            <button class="bg-cyan-100 text-gray-950 text-xl px-6 py-4 rounded-lg hover:bg-cyan-800">+ Add Location</button>
        </div>
    </div>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table class="w-full text-sm text-left text-gray-400">
            <thead class="text-xs text-gray-400 uppercase bg-gray-700">
                <tr class="h-12">
                    <th scope="col" class="px-6 py-3">
                        Location
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Temperature
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Rainfall
                    </th>
                    <th scope="col" class="px-6 py-3">
                        <span class="sr-only">Delete</span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr class="bg-gray-800 border-b border-gray-700 hover:bg-gray-600">
                    <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                        London
                    </th>
                    <td class="px-6 py-4">
                        15 °C
                    </td>
                    <td class="px-6 py-4">
                        20 mm
                    </td>
                    <td class="px-6 py-4 text-right">
                        <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
