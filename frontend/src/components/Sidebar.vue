<script setup>
import { Icon } from "@iconify/vue";
</script>
<template>
  <div class="flex md:flex-col space-y-4">
    <router-link
      to="/post"
      :class="[
        $route.path === '/post' ? 'bg-[#E2E2E2]  px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:post-outline" class="inline-block mr-2" /><span
        class="text-blue-800 hover:text-[#C59728]"
        >New Post</span
      ></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/design' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:design" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]"
        >Design</span
      ></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/game' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:gamepad-variant" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Game</span></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/voicetotext' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:voice" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">
        Voice to Text</span
      ></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/market' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:chart-line" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]"
        >Marketing</span
      ></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/job' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:briefcase" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Job </span></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/ad' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:announcement" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Ad</span></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/signlanguage' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:language" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]"
        >Sign Language</span
      ></router-link
    >
    <h1 class="font-semibold text-xl">Other</h1>
    <router-link
      to=""
      :class="[
        $route.path === '/follower' ? 'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md' : '',
        'px-2',
        'rounded-md',
      ]"
      ><Icon icon="mdi:account-multiple" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">
        Follower</span
      ></router-link
    >
    <router-link
      to=""
      :class="[
        $route.path === '/student' ? 'bg-[#E2E2E2] px-2 py-2 text-[#C59728] rounded-md' : '',
         
      ]"
      ><Icon icon="mdi:school" class="inline-block mr-2" /><span
        class="text-blue-800 hover:text-[#C59728]"
      >
        Student
      </span></router-link
    >
    <button
      class="bg-[#F4F4F4] border-2 border-[#4267B2] border-opacity-10 text-blue-800 px-6 py-1 rounded-xl hover:bg-teal-600 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent hover:text-white"
    >
      <Icon icon="mdi:logout" class="inline-block mr-2" /> Logout
    </button>
  </div>
</template>
