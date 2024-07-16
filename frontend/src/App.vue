<script setup>
import NavbarView from "./components/NavbarView.vue";
import { Icon } from "@iconify/vue";
import Sidebar from "./components/Sidebar.vue";
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div>
    <header>
      <div class="wrapper">
        <NavbarView />
      </div>
    </header>
    <main class="mt-[35vh] hidden md:block">
      <Sidebar class="md:fixed left-[7vw]" />
    </main>
    <div class="mt-[35vh] md:mt-0 md:ml-[23vw] lg:ml-[18vw] md:mr-[4vw]">
      <RouterView />
    </div>
  </div>
</template>
