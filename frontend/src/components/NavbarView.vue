<script setup>
import { Icon } from "@iconify/vue";
import { ref } from "vue";

const showSidebar = ref(false);
</script>

<template>
  <header class="flex flex-col fixed top-0 w-full">
    <!-- Top Header -->
    <div class="flex justify-between px-[6vw] py-6 md:py-0 items-center bg-[#008A8A]">
      <img src="../assets/logo.jpg" class="w-[6vw] h-[6vw]" alt="Logo" />
      <p class="text-white text-sm sm:text-xl md:text-2xl xl:text-3xl">
        Connect, Share and Engage with friends
      </p>
      <div class="flex gap-3">
        <button class="bg-[#F4F4F4] border-2 border-[#4267B2] border-opacity-10 text-blue-800 px-4 rounded-xl md:hidden hover:bg-teal-600 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent hover:text-white">
          <Icon icon="mdi:logout" class="inline-block mr-2" /> Logout
        </button>
        <Icon class="w-[4vw] h-[4vw]" icon="mdi:account" />
      </div>
    </div>

    <!-- Main Navigation -->
    <nav class="flex flex-col sm:flex-row gap-10 p-4 bg-[#F1F1F1] justify-between items-center px-[7vw]">
      <div class="flex gap-11">
        <RouterLink to="/">
          <Icon class="w-7 h-7" icon="mdi:account-plus" />
        </RouterLink>
        <RouterLink to="/post">
          <Icon class="w-7 h-7" icon="mdi:account-group" />
        </RouterLink>
        <RouterLink to="/post">
          <Icon class="w-7 h-7" icon="mdi:chat" />
        </RouterLink>
        <RouterLink to="/post">
          <Icon class="w-7 h-7" icon="mdi:bell" />
        </RouterLink>
        <button @click="showSidebar = !showSidebar" class="md:hidden">
          <Icon class="w-[4vw] h-[4vw]" icon="mdi:menu" />
        </button>
      </div>

      <div class="relative">
        <input type="text" class="px-4 py-3 w-[80vw] sm:w-[40vw] lg:w-[30vw] rounded-xl border-2 bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent" placeholder="Search" />
        <button class="absolute inset-y-0 right-0 px-4 text-teal-600">
          <svg class="h-5 w-5" fill="none" stroke="black" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
        </button>
      </div>
    </nav>

    <!-- Sidebar -->
    <div v-if="showSidebar" class="fixed top-0 left-0 w-full h-full bg-gray-800 bg-opacity-50 z-10 md:hidden">
      <div class="bg-white w-full mt-[9vh] p-6 overflow-y-auto transition-transform duration-300 ease-in-out" :class="{ '-translate-x-full': !showSidebar }">
        <button @click="showSidebar = false" class="absolute top-24 right-4">
          <Icon class="w-6 h-6" icon="mdi:close" />
        </button>
        <div class="flex flex-wrap items-center justify-center gap-6 space-y-4">
          <router-link @click="showSidebar = false" to="/post" active-class="border-1 bg-gray-200 px-3 py-1 rounded-md">
            <Icon icon="mdi:post-outline" class="inline-block mr-2" />
            <span class="text-blue-800">New Post</span>
          </router-link>
       
        </div>
      </div>
    </div>
  </header>
</template>

